
# def add(a,b):
#     res=a+b
#     return res
# def mul(a,b):
#     res = a*b
#     return res
# def div(a,b):
#     res = a/b
#     return res
# def sub(a,b):
#     res = a-b
#     return res
    
# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# while 1:
#     a=input("Select operation : ")
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     if a == '1':
#         print(num1, "+", num2, "=", add(num1, num2))

#     elif a == '2':
#         print(num1, "-", num2, "=", sub(num1, num2))

#     elif a == '3':
#         print(num1, "*", num2, "=", mul(num1, num2))

#     elif a == '4':
#         print(num1, "/", num2, "=", div(num1, num2))
#     else:
#         print("Invalid Input")
#     next = input("Let's do next calculation? (yes/no): ")
#     if next == "no":
#         break



import tkinter as tk
from tkinter import messagebox

def add():

        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")


def subtract():
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")

def multiply():
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")


def divide():
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
        else:
            result = num1 / num2
            result_label.config(text=f"Result: {result}")



root = tk.Tk()
root.title("Calculator")
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=0, column=1, padx=10, pady=10)
add_button = tk.Button(root, text="+", command=add)
add_button.grid(row=1, column=0, padx=10, pady=10)
subtract_button = tk.Button(root, text="-", command=subtract)
subtract_button.grid(row=1, column=1, padx=10, pady=10)
multiply_button = tk.Button(root, text="*", command=multiply)
multiply_button.grid(row=2, column=0, padx=10, pady=10)
divide_button = tk.Button(root, text="/", command=divide)
divide_button.grid(row=2, column=1, padx=10, pady=10)
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()