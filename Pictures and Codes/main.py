from tkinter import messagebox
from tkinter import *
from tkinter import ttk
def gasolineAdd():
    global allPetrol
    newpetrolname = admin_frame_petrol_add_Entry.get()
    newpetrolprice = addpriceentry.get()
    if newpetrolname in allPetrol.keys():
        messagebox.showerror("Error", "Petrol is available under this name")
    else:
        newpetroladd = {
                newpetrolname:{
                "Name": f"{newpetrolname}",
                "Price": newpetrolprice

                 },
        }
        allPetrol.update(newpetroladd)
        comboboxrefresh()
        check_price_Refresh()
        print(allPetrol)

def deletePetrol():
    global allPetrol
    global allFood
    delete = admin_Frame_delete_Entry.get()
    if delete in allPetrol.keys():
       allPetrol.pop(delete)
       comboboxrefresh()
       print(allPetrol)
    if delete in allFood.keys():
        allFood.pop(delete)
        comboboxrefresh()
        print(allFood)

gasolinePrice = 0
fastfoodPrice = 0
total = 0

def check_price_Refresh():
    price_calculation_Fastfood()
    price_calculation_Petrol()


def check_Price():
    global gasolinePrice
    price_calculation_Petrol()
    price_Label = Label(guest_Frame, text=f"{gasolinePrice}", font=("Comic Sans MS", 10))
    price_Label.place(relx=0.10, rely=0.29,width=60,height=30)
    print(gasolinePrice)

def price_calculation_Petrol():
    global gasolinePrice
    ischeck_litr_or_price = x.get()
    ischeck_gasoline = y.get()
    miqdar = entryint.get()
    for i in allPetrol.keys():
        if ischeck_gasoline == allPetrol[i]['Name'] and ischeck_litr_or_price == "Litr":
            gasolinePrice += (miqdar * allPetrol[i]['Price'])
        elif ischeck_gasoline == allPetrol[i]['Name'] and ischeck_litr_or_price == "Price":
            gasolinePrice += (miqdar / allPetrol[i]['Price'])

def price_calculation_Fastfood():
    global fastfoodPrice
    ischeck_fastfood = f.get()
    amount = int_f.get()
    for i in allFood.keys():
        if ischeck_fastfood == allFood[i]['Name']:
            fastfoodPrice += (amount * allFood[i]['Price'])

def check_Fastfood_Price():
    global fastfoodPrice
    price_calculation_Fastfood()
    fastfoodprice_Label = Label(guest_Frame, text=f"{fastfoodPrice}", font=("Comic Sans MS", 10))
    fastfoodprice_Label.place(relx=0.60, rely=0.23,width=60,height=30)
    print(fastfoodPrice)

def refresh_fastfood_Price_Label():
    fastfoodprice_Label = Label(guest_Frame, text=f"{fastfoodPrice}", font=("Comic Sans MS", 10))
    fastfoodprice_Label.place(relx=0.60, rely=0.23, width=60, height=30)

def refresh_Price_Label():
    price_Label = Label(guest_Frame, text=f"{gasolinePrice}", font=("Comic Sans MS", 10))
    price_Label.place(relx=0.10, rely=0.29, width=60, height=30)


def resetPrice():
    global gasolinePrice
    gasolinePrice = 0
    refresh_Price_Label()

def resetfastfoodPrice():
    global fastfoodPrice
    fastfoodPrice = 0
    refresh_fastfood_Price_Label()

def comboboxrefresh():
    y = StringVar()
    selectpetrol = ttk.Combobox(guest_Frame, textvariable=y, state="readonly", values=list(allPetrol))
    selectpetrol.place(relx=0.10, rely=0.09, width=90, height=30)
    f = StringVar()
    selectFastFood = ttk.Combobox(guest_Frame, textvariable=f, state="readonly", values=list(allFood.keys()))
    selectFastFood.place(relx=0.63, rely=0.08, width=90, height=30)


def admin_login_frame_menu_back():
    admin_login_frame.forget()
    admin_register_frame.forget()
    first_Frame.pack(expand=True, fill=BOTH)

def registermenu():
    admin_login_frame.forget()
    admin_register_frame.pack(expand=True, fill=BOTH)

def registerback():
    admin_register_frame.forget()
    admin_login_frame.forget()
    first_Frame.pack(expand=True, fill=BOTH)


def adminframeback():
    admin_Frame.forget()
    admin_register_frame.forget()
    admin_login_frame.forget()
    first_Frame.pack(expand=True, fill=BOTH)

def guestMenu():
    admin_Frame.forget()
    first_Frame.forget()
    guest_Frame.pack(expand=True, fill=BOTH)

def adminMenu():
    first_Frame.forget()
    guest_Frame.forget()
    admin_Frame.forget()
    admin_register_frame.forget()
    admin_login_frame.pack(expand=True, fill=BOTH)


def guestBackButton():
    admin_Frame.forget()
    guest_Frame.forget()
    first_Frame.pack(expand=True,fill=BOTH)

flag = True
def my_showhide():
    global flag
    if flag == True:
        admin_password_showhide.config(text="Hide")
        admin_password_Entry.config(show='')
        flag = False
    else:
        admin_password_showhide.config(text="Show")
        admin_password_Entry.config(show='*')
        flag = True

def singIn():
   email = admin_email_Entry.get()
   password = admin_password_Entry.get()

   if email in allAdmin.keys():
       if password == allAdmin[email]['password']:
           admin_register_frame.forget()
           admin_login_frame.forget()
           admin_Frame.pack(expand=True,fill = BOTH)
       else:
           messagebox.showerror("Error", "The password entered is incorrect")
   else:
        messagebox.showerror("Error","Such an email does not exist!")


def checkRegister():
   email1 = register_email_Entry.get()
   password2 = register_password_Entry.get()
   name = register_name_Entry.get()
   surname = register_surname_Entry.get()



   if email1 in allAdmin.keys():
       messagebox.showerror("Error", "Such an email exists. ")
   elif len(name) < 3:
       messagebox.showerror("Error", "The name must contain at least 3 characters ")
   elif len(surname) < 3:
       messagebox.showerror("Error", "Surname must be at least 3 characters long ")
   elif email1.endswith("@gmail.com") == False and email1.endswith("@mail.ru") == False:
       messagebox.showerror("Error", "email must end with @gmail.com or @mail.ru!")
   elif len(password2) < 3:
       messagebox.showerror("Error", "password must have at least 3 characters")

   else:
       dict = {
           email1:{
               "name":name,
               "surname":surname,
               "email": email1,
               "password":password2,

           }
       }
       allAdmin.update(dict)
       messagebox.showinfo("Succesful",f"you have successfully registered")
       print(allAdmin)


def adminpanelcheck():
    global allPetrol

    print(allPetrol[admin_frame_petrol_Entry.get()]['Price'])
    for item in allPetrol.items():
        if item[0] == admin_frame_petrol_Entry.get():
            allPetrol[admin_frame_petrol_Entry.get()]['Price'] = int(admin_frame_size_Entry.get())


allPetrol = {
    "Ai-92": {
        "Name": "Ai-92",
        "Price": 1
    },
    "Ai-95": {
        "Name": "Ai-95",
        "Price": 2
    },
    "Ai-98": {
        "Name": "Ai-98",
        "Price": 2.50
    },
    "Dizel": {
        "Name": "Dizel",
        "Price": 0.80
    }
}
allAdmin = {
    "1": {
        "name": "Kenan",
        "surname": "Nuri",
        "email": "1",
        "password": "1",

    }

}

allFood = {
    "Hamburger": {
        "Name": "Hamburger",
        "Price": 3
    },
    "Hotdog": {
        "Name": "Hotdog",
        "Price": 2
    },
    "Hotcakes": {
        "Name": "Hotcakes",
        "Price": 1.50
    },
    "Cola": {
        "Name": "Cola",
        "Price": 1
    },
    "Cappucino": {
        "Name": "Cappucino",
        "Price": 2.50
    },
    "Americano": {
        "Name": "Americano",
        "Price": 3.50

    },

}

window = Tk()
window.title("Lukoil")
window.geometry("800x550+400+100")
window.resizable(False, False)

# Frame Start
first_Frame = Frame(window)
admin_Frame = Frame(window)
guest_Frame = Frame(window)
admin_login_frame = Frame(window)
admin_register_frame = Frame(window)

# Image Start
window_image = PhotoImage(file="lukoilwindowback (1).gif")
guest_Frame_image = PhotoImage(file="Lukoil_image_guest (1).gif")
icon_Photo = PhotoImage(file="icon (1).gif")
window.iconphoto(False, icon_Photo)
# Background_image
window_Background = Label(first_Frame, image=window_image)
window_Background.pack()
first_Frame.pack()
guest_Frame_image_background = Label(guest_Frame, image=guest_Frame_image)
guest_Frame_image_background.pack()

# Button

guest_Button = Button(first_Frame, text="Guest", activebackground="red", activeforeground="red",
                      font=("Comic Sans MS", 15), command=lambda: guestMenu())
guest_Button.place(relx=0.4, rely=0.10, width=100, height=40)
admin_Button = Button(first_Frame, text="Admin", activebackground="red", activeforeground="red", background="red",
                      font=("Comic Sans MS", 15), command=lambda: adminMenu())
admin_Button.place(relx=0.4, rely=0.20, width=100, height=40)
guest_Frame_back_button = Button(guest_Frame, text="Back", font=("Comic Sans MS", 10),
                                 command=lambda: guestBackButton())
guest_Frame_back_button.place(relx=0.01, rely=0.01)
pay_Button = Button(guest_Frame, text="Size", command=lambda: check_Price())
pay_Button.place(rely=0.30, relx=0.22, width=70, height=30)
reset_Button = Button(guest_Frame, text="Reset", font=("Comic Sans MS", 10), command=lambda: resetPrice())
reset_Button.place(relx=0.01, rely=0.36)
reset_fastfood_Button = Button(guest_Frame, text="Reset", font=("Comic Sans MS", 10),
                               command=lambda: resetfastfoodPrice())
reset_fastfood_Button.place(relx=0.50, rely=0.29)
fastfood_size_Button = Button(guest_Frame, text="Size", font=("Comic Sans MS", 10),
                              command=lambda: check_Fastfood_Price())
fastfood_size_Button.place(relx=0.71, rely=0.23, width=70, height=30)

# admin menu start
admin_text_email_Label = Label(admin_login_frame, text="Email:", font=("Comic Sans MS", 15))
admin_text_email_Label.place(relx=0.30, rely=0.30)
admin_text_password_Label = Label(admin_login_frame, text="Password:", font=("Comic Sans MS", 15))
admin_text_password_Label.place(relx=0.30, rely=0.40)

# admin menu entry
email_entry = StringVar()
admin_email_Entry = Entry(admin_login_frame, textvariable=email_entry)
admin_email_Entry.place(relx=0.44, rely=0.31, width=115, height=25)
password_entry = StringVar()
admin_password_Entry = Entry(admin_login_frame, textvariable=password_entry)
admin_password_Entry.place(relx=0.44, rely=0.41, width=115, height=25)
admin_password_showhide = Button(admin_login_frame, font=("Comic Sans MS", 15), command=lambda: my_showhide())
admin_password_showhide.place(relx=0.60, rely=0.41, width=50, height=25)

# Admin Login Frame Button
admin_Login_emailpassword_check_Button = Button(admin_login_frame, text="Login", cursor="hand2",
                                                font=("Comic Sans MS", 10), command=lambda: singIn())
admin_Login_emailpassword_check_Button.place(relx=0.44, rely=0.47, width=80, height=30)
admin_login_frame_back_Button = Button(admin_login_frame, text="Back", font=("Comic Sans MS", 10),
                                       command=lambda: admin_login_frame_menu_back())
admin_login_frame_back_Button.place(relx=0.01, rely=0.01)
admin_login_frame_register_Button = Button(admin_login_frame, text="Register", cursor="hand2",
                                           command=lambda: registermenu())
admin_login_frame_register_Button.place(relx=0.30, rely=0.50, width=80, height=30)

# Register Frame Start
register_name_Label = Label(admin_register_frame, text="Name", font=("Comic Sans MS", 15))
register_name_Label.place(relx=0.30, rely=0.25)
register_surname_Label = Label(admin_register_frame, text="Surname", font=("Comic Sans MS", 15))
register_surname_Label.place(relx=0.30, rely=0.35)
register_email_Label = Label(admin_register_frame, text="Email", font=("Comic Sans MS", 15))
register_email_Label.place(relx=0.30, rely=0.45)
register_password_Label = Label(admin_register_frame, text="Password", font=("Comic Sans MS", 15))
register_password_Label.place(relx=0.30, rely=0.55)

# Register Entry
register_name_Entry = Entry(admin_register_frame, font=("Comic Sans MS", 15, "bold"))
register_name_Entry.place(relx=0.45, rely=0.25)
register_surname_Entry = Entry(admin_register_frame, font=("Comic Sans MS", 15, "bold"))
register_surname_Entry.place(relx=0.45, rely=0.35)
register_email_Entry = Entry(admin_register_frame, font=("Comic Sans MS", 15, "bold"))
register_email_Entry.place(relx=0.45, rely=0.45)
register_password_Entry = Entry(admin_register_frame, font=("Comic Sans MS", 15, "bold"))
register_password_Entry.place(relx=0.45, rely=0.55)

# Register Button
register_back_Button = Button(admin_register_frame, text="Back", font=("Comic Sans MS", 10),
                              command=lambda: registerback())
register_back_Button.place(relx=0.01, rely=0.01)
register_signin_Button = Button(admin_register_frame, text="SignIn", font=("Comic Sans MS", 15, "bold"),
                                command=lambda: checkRegister())
register_signin_Button.place(relx=0.45, rely=0.61)

# Admin Frame
admin_frame_Petrol_Text = Label(admin_Frame, text="Petrol Name", font=("Comic Sans MS", 15))
admin_frame_Petrol_Text.place(relx=0.03, rely=0.10)
admin_frame_size_text = Label(admin_Frame, text="Size:", font=("Comic Sans MS", 15))
admin_frame_size_text.place(relx=0.03, rely=0.20)
admin_frame_delete_Text = Label(admin_Frame, text="Delete Name", font=("Comic Sans MS", 15))
admin_frame_delete_Text.place(relx=0.45, rely=0.10)
admin_frame_petrol_add_Text = Label(admin_Frame, text="Petrol Add ", font=("Comic Sans MS", 15))
admin_frame_petrol_add_Text.place(relx=0.20, rely=0.33)
admin_frame_petrol_add_name_text = Label(admin_Frame, text="Petrol Name Add", font=("Comic Sans MS", 15))
admin_frame_petrol_add_name_text.place(relx=0.03, rely=0.40)
admin_frame_petrol_Add_Price_Text = Label(admin_Frame, text="Petrol Price Add", font=("Comic Sans MS", 15))
admin_frame_petrol_Add_Price_Text.place(relx=0.03, rely=0.50)

# admin frame entry
admin_frame_petrol_Entry = Entry(admin_Frame, font=("Comic Sans MS", 10))
admin_frame_petrol_Entry.place(relx=0.22, rely=0.12)
admin_frame_size_Entry = Entry(admin_Frame, font=("Comic Sans MS", 10))
admin_frame_size_Entry.place(relx=0.22, rely=0.20)
admin_Frame_delete_Entry = Entry(admin_Frame, font=("Comic Sans MS", 10))
admin_Frame_delete_Entry.place(relx=0.45, rely=0.17)
admin_frame_petrol_add_Entry = Entry(admin_Frame, font=("Comic Sans MS", 10))
admin_frame_petrol_add_Entry.place(relx=0.25, rely=0.42)
addpriceentry = IntVar()
admin_frame_petrol_Add_Price_Entry = Entry(admin_Frame, textvariable=addpriceentry, font=("Comic Sans MS", 10))
admin_frame_petrol_Add_Price_Entry.place(relx=0.25, rely=0.51)
# admin frame button

admin_frame_size_change_Button = Button(admin_Frame, text="Change", command=lambda: adminpanelcheck())
admin_frame_size_change_Button.place(relx=0.23, rely=0.25)
admin_frame_back_Button = Button(admin_Frame, text="Back", font=("Comic Sans MS", 10), command=lambda: adminframeback())
admin_frame_back_Button.place(relx=0.01, rely=0.01)
admin_Frame_delete_Button = Button(admin_Frame, text="Delete", font=("Comic Sans MS", 10),
                                   command=lambda: deletePetrol())
admin_Frame_delete_Button.place(relx=0.45, rely=0.22)
admin_frame_petrol_add_Button = Button(admin_Frame, text="Add", font=("Comic Sans MS", 10),
                                       command=lambda: gasolineAdd())
admin_frame_petrol_add_Button.place(relx=0.25, rely=0.55)

# Guest Text Label
benzin_label = Label(guest_Frame, text="Petrol:", bg="red", fg="white", font=("Comic Sans MS", 15))
benzin_label.place(relx=0.01, rely=0.08)
text_Litr_or_price = Label(guest_Frame, text="Litr or Price:", bg="red", fg="white", font=("Comic Sans MS", 15))
text_Litr_or_price.place(relx=0.01, rely=0.15)
text_gasolineAmount_label = Label(guest_Frame, text="Amount Of Gasoline:", bg="red", fg="white",
                                  font=("Comic Sans MS", 15))
text_gasolineAmount_label.place(relx=0.01, rely=0.22)
text_Price_Label = Label(guest_Frame, text="Price:", bg="red", fg="white", font=("Comic Sans MS", 15))
text_Price_Label.place(relx=0.01, rely=0.29)
text_Fastfood_Label = Label(guest_Frame, text="FastFood:", bg="red", fg="white", font=("Comic Sans MS", 15))
text_Fastfood_Label.place(relx=0.50, rely=0.08)
text_fastfoodamount_Label = Label(guest_Frame, text="Amount Of Food:", bg="red", fg="white", font=("Comic Sans MS", 15))
text_fastfoodamount_Label.place(relx=0.50, rely=0.15)
text_Fastfood_price_Label = Label(guest_Frame, text="Price:", bg="red", fg="white", font=("Comic Sans MS", 15))
text_Fastfood_price_Label.place(relx=0.50, rely=0.22)

# Guest Frame Combobox Start

y = StringVar()
selectpetrol = ttk.Combobox(guest_Frame, textvariable=y, state="readonly", values=list(allPetrol.keys()))
selectpetrol.place(relx=0.10, rely=0.09, width=90, height=30)
x = StringVar()
select_litr_or_price = ttk.Combobox(guest_Frame, textvariable=x, state="readonly", values=["Litr", "Price"])
select_litr_or_price.place(relx=0.17, rely=0.16, width=90, height=30)
f = StringVar()
selectFastFood = ttk.Combobox(guest_Frame, textvariable=f, state="readonly", values=list(allFood.keys()))
selectFastFood.place(relx=0.63, rely=0.08, width=90, height=30)
# Guest Frame Entry Start

entryint = IntVar()
gasoline_amount_entry = Entry(guest_Frame, textvariable=entryint, font=("Comic Sans MS", 10))
gasoline_amount_entry.place(relx=0.26, rely=0.22, width=90, height=30)

int_f = IntVar()
fastfood_amount_Entry = Entry(guest_Frame, textvariable=int_f, font=("Comic Sans MS", 10))
fastfood_amount_Entry.place(relx=0.71, rely=0.15, width=90, height=30)
myListbox = Listbox(guest_Frame)
myListbox.place(relx=0.30, rely=0.65, width=250, height=200)
counter = 0
listBoxButton = Button(guest_Frame)

window.mainloop()
