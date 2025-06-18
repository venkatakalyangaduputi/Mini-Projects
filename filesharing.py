import socket
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os

# Server (Receiver) Function
def start_server():
    def server_thread():
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('0.0.0.0', 5001))
            server.listen(1)
            print("Waiting for connection...")
            
            conn, addr = server.accept()
            print(f"Connected to {addr}")
            
            file_info = conn.recv(1024).decode().split('|')
            if len(file_info) < 2:
                messagebox.showerror("Error", "Invalid file information received.")
                return
            
            file_name, file_size = file_info[0], int(file_info[1])
            print(f"Receiving file: {file_name} ({file_size} bytes)")
            
            with open(file_name, 'wb') as f:
                received = 0
                while received < file_size:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
                    received += len(data)
            
            messagebox.showinfo("Success", f"Received {file_name}")
            print("File received successfully.")
            conn.close()
            server.close()
        except Exception as e:
            messagebox.showerror("Server Error", str(e))
            print(f"Server error: {e}")
    
    threading.Thread(target=server_thread, daemon=True).start()
    messagebox.showinfo("Receiver Started", "Receiver is waiting for incoming files...")

# Client (Sender) Function
def send_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    ip_address = entry_ip.get().strip()
    if not ip_address:
        messagebox.showerror("Error", "Enter the receiver's IP address")
        return
    
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    print(f"Sending file: {file_name} ({file_size} bytes) to {ip_address}")
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip_address, 5001))
        client.send(f"{file_name}|{file_size}".encode())
        
        with open(file_path, 'rb') as f:
            while (data := f.read(1024)):
                client.send(data)
        
        messagebox.showinfo("Success", "File sent successfully")
        print("File sent successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        print(f"Client error: {e}")
    finally:
        client.close()

# GUI Setup
def start_app():
    start_button.pack_forget()
    instructions.pack_forget()
    
    tk.Label(root, text="Receiver's IP Address:", font=("Comic Sans MS", 30), bg="#000000").pack(pady=5)
    global entry_ip
    entry_ip = tk.Entry(root, font=("Comic Sans MS", 12), width=25,bg="black",fg="white")
    entry_ip.pack(pady=5)
    
    tk.Button(root, text="Send File", font=("Comic Sans MS", 20), command=send_file, bg="#4CAF50", fg="black", padx=10, pady=5).pack(pady=10)
    tk.Button(root, text="Start Receiver", font=("Comic Sans MS", 20), command=start_server, bg="#008CBA", fg="black", padx=10, pady=5).pack(pady=10)

root = tk.Tk()
root.title("File Sharing App")
root.geometry("800x300")
root.configure(bg="#f0f0f0")

instructions = tk.Label(root, text="Find your IP address using the following commands:\nWindows: ipconfig\nMac: ifconfig or hostname -I", font=("Comic Sans MS", 20), bg="#000000", wraplength=380, justify="center")
instructions.pack(pady=20)

start_button = tk.Button(root, text="Click Here to Start and you can share and recieve files with the help of ipaddress", font=("Comic Sans MS", 20), command=start_app, bg="#000000", fg="black", padx=10, pady=5)
start_button.pack(pady=10)

root.mainloop()
