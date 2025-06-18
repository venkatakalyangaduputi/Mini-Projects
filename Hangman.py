import random
import tkinter as tk
from tkinter import messagebox

def guess_word(category):
    global word, guessed, attempts
    word = random.choice(category)
    guessed = ["_" if ch != " " else " " for ch in word]
    attempts = 6
    word_label.config(text=" ".join(guessed))
    guess_entry.delete(0, tk.END)
    attempts_label.config(text=f"Attempts left: {attempts}")
    submit_button.config(state=tk.NORMAL)
    canvas.delete("all") 
def check_guess():
    global attempts
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)
    
    if not guess or len(guess) != 1:
        messagebox.showwarning("Warning", "Please enter a single letter!")
        return
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts left: {attempts}")
        draw_hangman(attempts) 
    word_label.config(text=" ".join(guessed))
    
    if "_" not in guessed:
        messagebox.showinfo("Congratulations!", f"You won! The word was: {word}")
        submit_button.config(state=tk.DISABLED)
    elif attempts == 0:
        messagebox.showerror("Game Over", f"Game over! The word was: {word}")
        submit_button.config(state=tk.DISABLED)

def start_game(category):
    guess_word(category)
    attempts_label.config(text=f"Attempts left: {attempts}")
    submit_button.config(state=tk.NORMAL)

def draw_hangman(attempts):
    canvas.delete("all") 
    canvas.create_line(50, 180, 150, 180, width=4) 
    canvas.create_line(100, 180, 100, 50, width=4)  
    canvas.create_line(100, 50, 150, 50, width=4)   
    canvas.create_line(150, 50, 150, 70, width=4)   

    if attempts <= 5:
        canvas.create_oval(135, 70, 165, 100, width=4)  
    if attempts <= 4:
        canvas.create_line(150, 100, 150, 140, width=4) 
    if attempts <= 3:
        canvas.create_line(150, 110, 130, 130, width=4) 
    if attempts <= 2:
        canvas.create_line(150, 110, 170, 130, width=4) 
    if attempts <= 1:
        canvas.create_line(150, 140, 130, 170, width=4) 
    if attempts == 0:
        canvas.create_line(150, 140, 170, 170, width=4) 

fruits =["apple", "banana", "cherry", "orange", "grapes","mango", "pineapple",
    "strawberry", "watermelon", "blueberry","kiwi", "peach", "papaya", "pomegranate", "guava","pear", 
    "plum", "lychee", "fig", "coconut",
    "apricot", "blackberry", "cranberry", "date", "dragonfruit",
    "elderberry", "gooseberry", "jackfruit", "lemon", "lime",
    "mandarin", "mulberry", "nectarine", "olive", "passionfruit",
    "persimmon", "quince", "raspberry", "starfruit", "tamarind",
    "boysenberry", "cantaloupe", "honeydew", "carambola", "soursop",
    "longan", "rambutan", "sapodilla", "durian", "ackee",
    "jabuticaba", "bilberry", "marionberry", "salak", "feijoa",
    "cherimoya", "medlar", "breadfruit", "goji berry", "miracle fruit"
]

vegetables = [
    "carrot", "broccoli", "cabbage", "spinach", "potato",
    "tomato", "onion", "cucumber", "pumpkin", "lettuce",
    "cauliflower", "radish", "beetroot", "brinjal", "capsicum",
    "peas", "zucchini", "asparagus", "celery", "artichoke",
    "okra", "corn", "mushroom", "turnip", "yam",
    "leek", "fennel", "chayote", "swiss chard", "shallot",
    "bitter gourd", "bottle gourd", "drumstick", "coriander", "mint",
    "parsley", "spring onion", "kale", "sweet potato", "red cabbage",
    "green beans", "soybean", "arugula", "watercress", "endive",
    "collard greens", "radicchio", "parsnip", "mustard greens", "kohlrabi",
    "chicory", "bok choy", "daikon", "malabar spinach", "fenugreek leaves"
]
sports = [
    "soccer", "basketball", "cricket", "tennis", "badminton",
    "volleyball", "baseball", "hockey", "golf", "rugby",
    "table tennis", "swimming", "boxing", "wrestling", "karate",
    "taekwondo", "judo", "gymnastics", "cycling", "skiing",
    "snowboarding", "skateboarding", "surfing", "archery", "fencing",
    "weightlifting", "track and field", "marathon", "pole vault", "long jump",
    "high jump", "triple jump", "shot put", "discus throw", "javelin throw",
    "rowing", "canoeing", "kayaking", "sailing", "diving",
    "horse racing", "equestrian", "motorsport", "Formula 1", "rally racing",
    "speed skating", "ice hockey", "bobsleigh", "handball", "netball",
    "snooker", "billiards", "chess", "esports", "rock climbing"
]
Animals = [
    "lion", "tiger", "elephant", "giraffe", "zebra",
    "kangaroo", "panda", "cheetah", "leopard", "bear",
    "wolf", "fox", "rabbit", "deer", "monkey",
    "gorilla", "chimpanzee", "hippopotamus", "rhinoceros", "buffalo",
    "camel", "horse", "donkey", "cow", "goat",
    "sheep", "dog", "cat", "mouse", "rat",
    "squirrel", "bat", "otter", "beaver", "coyote",
    "dolphin", "whale", "shark", "octopus", "jellyfish",
    "penguin", "eagle", "owl", "peacock", "flamingo",
    "parrot", "sparrow", "hawk", "vulture", "ostrich",
    "cobra", "python", "crocodile", "alligator", "tortoise",
    "lizard", "chameleon", "frog", "toad", "newt"
]
cricketers = [
    "sachin tendulkar", "virat kohli", "ms dhoni", "rohit sharma", "rahul dravid",
    "sourav ganguly", "sunil gavaskar", "kapil dev", "yuvraj singh", "anil kumble",
    "shikhar dhawan", "hardik pandya", "jasprit bumrah", "ravindra jadeja", "ravichandran ashwin",
    "kl rahul", "bhuvneshwar kumar", "mohammed shami", "suresh raina", "vvs laxman",
    "steve smith", "david warner", "pat cummins", "mitchell starc", "glenn maxwell",
    "ricky ponting", "shane warne", "adam gilchrist", "michael clarke", "brett lee",
    "jacques kallis", "ab de villiers", "hashim amla", "dale steyn", "graeme smith",
    "faf du plessis", "kagiso rabada", "shaun pollock", "makhaya ntini", "allan donald",
    "joe root", "ben stokes", "jofra archer", "james anderson", "stuart broad",
    "eoin morgan", "alastair cook", "andrew flintoff", "kevin pietersen", "ian botham",
    "kane williamson", "trent boult", "tim southee", "brendon mccullum", "ross taylor",
    "daniel vettori", "martin guptill", "chris gayle", "brian lara", "shivnarine chanderpaul",
    "courtney walsh", "curtly ambrose", "andre russell", "dwayne bravo", "jason holder",
    "muttiah muralitharan", "kumar sangakkara", "mahela jayawardene", "lasith malinga", "sanath jayasuriya",
    "arjuna ranatunga", "tillakaratne dilshan", "angelo mathews", "inzamam-ul-haq", "wasim akram",
    "waqar younis", "shoaib akhtar", "babar azam", "shaheen afridi", "shadab khan",
    "mohammad rizwan", "younis khan", "misbah-ul-haq", "saqlain mushtaq", "imran khan"
]

indian_heros = [
    "shah rukh khan", "salman khan", "aamir khan", "akshay kumar", "hrithik roshan",
    "ranbir kapoor", "ranveer singh", "ajay devgn", "saif ali khan", "varun dhawan",
    "tiger shroff", "sidharth malhotra", "vicky kaushal", "kartik aaryan", "rajkummar rao",
    "nawazuddin siddiqui", "ayushmann khurrana", "sunny deol", "bobby deol", "john abraham",
    "farhan akhtar", "arjun kapoor", "emraan hashmi", "shahid kapoor", "abhishek bachchan",
    "amitabh bachchan", "dhanush", "vijay", "suriya", "kamal haasan",
    "rajinikanth", "prabhas", "mahesh babu", "allu arjun", "ram charan",
    "jr ntr", "nagarjuna", "pawan kalyan", "chiranjeevi", "vikram",
    "karthi", "siva karthikeyan", "fahadh faasil", "mohanlal", "mammootty",
    "dulquer salmaan", "nivin pauly", "yash", "darshan", "punith rajkumar",
    "upendra", "ravi teja", "nani", "vijay deverakonda", "rana daggubati"
]



root = tk.Tk()
root.title("Hangman Game")
root.geometry("500x650")

tk.Label(root, text="Welcome to Hangman Game!", font=("Times New Roman", 20, "bold")).pack(pady=10)
word_label = tk.Label(root, text="", font=("Times New Roman", 16))
word_label.pack(pady=10)
attempts_label = tk.Label(root, text="Attempts left: 6", font=("Times New Roman", 20))
attempts_label.pack()

guess_entry = tk.Entry(root, font=("Times New Roman", 16), width=5)
guess_entry.pack(pady=5)
submit_button = tk.Button(root, text="Guess", font=("Times New Roman", 16), command=check_guess, state=tk.DISABLED)
submit_button.pack(pady=5)

# Category buttons
categories = [("Fruits", fruits), ("Vegetables", vegetables), ("Sports", sports),
              ("Animals", Animals), ("Cricketers", cricketers), ("Indian Heroes", indian_heros)]

for name, category in categories:
    tk.Button(root, text=name, font=("Times New Roman", 16), width=15, command=lambda c=category: start_game(c)).pack(pady=2)

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

root.mainloop()
