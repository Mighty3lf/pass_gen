from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# --------------------------------------- FUNCTIONS ---------------------------------------------

def add_function():
    web_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    new_data = {
        web_text: {
                "email": email_text,
                "password": password_text,
        }

    }
    
    if len(web_text) == 0 or len(email_text) == 0 or len(password_text) == 0:
        messagebox.showerror(title="Ooops", message="You should fill out the fields!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
            
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating new data
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                    # saving data
                    json.dump(data, data_file, indent=4)
                
        finally:      
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    
    

# ------------------------------------ PASSWORD -------------------------------------------

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

def generate_pass():
    password_list = [random.choice(letters) for _ in range(nr_letters)]\
    + [random.choice(symbols) for _ in range(nr_symbols)]\
    + [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = [char for char in password_list]
    password = "".join(password)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ----------------------------------------- GUI ------------------------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
password_img = PhotoImage(file=r"C:\Users\Sami\OneDrive\Ambiente de Trabalho\PY\pass_gen\logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

website = Label(text="Website", bg="white")
website.grid(row=1, column=0)
website_entry = Entry(width=53)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email = Label(text="Email/Username:", bg="white")
email.grid(row=2,column=0)
email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sami_parkkali@hotmail.com")

password = Label(text="Password", bg="white")
password.grid(row=3,column=0)
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)

generate = Button(text="Generate Password", bg="lightblue", command=generate_pass)
generate.grid(row=3, column=2)

add = Button(text="Add", bg="white", width=45, command=add_function)
add.grid(column=1, row=4, columnspan=2)

def search():
    try:
        with open("data.json", "r") as file:
            f = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="NOT FOUND", message="Can't find that password!")
    else:
        if website_entry.get() == "":
           messagebox.showerror(title="Keep calm", message="Qual é o site cão de caça?")
        else:
            dados = f[website_entry.get()]
            passe = dados['password']
            email = dados["email"]
            messagebox.showinfo(title=dados, message=f"E-mail: {email}\nPassword: {passe}")

search = Button(text="Search", bg="red", width=13, command=search)
search.grid(column=2, row=1)







window.mainloop()