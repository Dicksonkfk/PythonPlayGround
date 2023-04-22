from tkinter import *
from tkinter import messagebox

# Initialize the values of counter for array of fertilizers
i = 0

screen = Tk()
screen.geometry("500x500")
screen.title("Login Screen")
#heading = Label(text="Income Form", bg="grey", fg="black", width="500", height="3")
#heading.pack()

# Getting User Input via Income Form
l1 =Label(screen, text='Username')
l2 =Label(screen, text='Password')
income_text = Label(screen, text="Monthly Income: RM" )

l1.grid(row=0, column=0, padx=5, pady=5)
l2.grid(row=1, column=0, padx=5, pady=5)
income_text.grid(row=2, column=0, padx=5, pady=5)

username= StringVar()
password = StringVar()
income = IntVar()

user= Entry(screen, textvariable=username, font=(8))
pwd= Entry(screen, textvariable=password, font=(8), show='*')
income_entry = Entry(screen, textvariable=income, font=(8))

user.grid(row=0, column=1)
pwd.grid(row=1, column=1)
income_entry.grid(row=2, column=1)

# Create an array for selections of fertilizer
fertilizer = [
    "Ammonium-T ",
    "Nitrogen-I ",
    "Inhibitors ",
    "Phosphorus ",
    "Potassium ",
    "Sulphur ",
    "Nitrogen ",
    "Micronutrient "
]
choices = StringVar()
choices.set(fertilizer[0])

drop = OptionMenu(screen, choices, *fertilizer)
drop.grid(row=5, column=0, padx=5, pady=5)


def selected(event):
    myLabel = Label(screen, text=selected.get()).pack()

dropButton = Button(screen, text="Select fertilizer from list", command=selected)


def login():
    if username.get()=='admin' and password.get()=='admin':
        messagebox.showinfo(title='Login Status', message='You have Logged in as admin.')
        btn1['state'] = 'normal'
    else:
        messagebox.showerror(title='Login Error', message='Invalid Credentials!')


def process():
    i = 0
    if income.get() > 0:
        if income.get()>= 6000:
            messagebox.showinfo(title="Expert Suggestion",
                                message="You could use " + fertilizer[1] + " Fertilizer!")

        elif income.get() in range(5001, 5999):
            messagebox.showinfo(title="Expert Suggestion",
                                message="You could use " + fertilizer[0] + " Fertilizer!")

        elif income.get() in range(4001, 5000):
            messagebox.showinfo(title="Expert Suggestion",
                                message="You could use " + fertilizer[2] + " Fertilizer!")

        elif income.get() in range(3001, 4000):
            status = messagebox.askyesno(title="Question",
                                            message="We have found you " +fertilizer[6]+ "Fertilizer")
            if status == True:
                messagebox.showinfo(title="Expert Suggestion",
                                    message="You have chosen " + fertilizer[6] + " Fertilizer!")
            else:
                messagebox.showinfo(title="Expert Suggestion",
                                    message="You have chosen " + fertilizer[5] + " Fertilizer!")

        elif income.get() in range(2001, 3000):
            status = messagebox.askyesno(title="Question",
                                            message="We have found you " + fertilizer[3] + "Fertilizer")
            if status == True:
                messagebox.showinfo(title="Expert Suggestion",
                                    message="You have chosen " + fertilizer[3] + " Fertilizer!")
            else:
                messagebox.showinfo(title="Expert Suggestion",
                                    message="You have chosen " + fertilizer[4] + " Fertilizer!")

        elif income.get() in range(1, 2001):
            messagebox.showinfo(title="Expert Suggestion", message="You could use " + fertilizer[7] + " Fertilizer!")

    else:
        messagebox.showinfo(title="Error", message="You are not qualified to choose the fertilizer.")


btn = Button(screen,  command=login, text='Login', width="30", height="2" )
btn.place(x=55, y=150)
btn1 = Button(screen, text="Start Analysis", width="30", height="2", command=process, bg="grey")
btn1.place(x=55, y=250)
btn1['state']='disabled'

#btn2 = Button(screen, text="Expertise Suggestion", width="30", height="2", command="showMsg", bg="blue")
#btn2.place(x=105, y=650)

screen.mainloop()