import random
import tkinter as tk

root = tk.Tk()
root.geometry("400x500")
root.title("sang,kaghaz,gheychi")
root.resizable(width=False, height=False)
#######################################################################################3
Karbar_scor = 0
Comp_scor = 0
entekhabe_karbar = ""
entekhabe_comp = ""

#############################################################################


def user_choice(choice):
    skg = {"sang": 0, "kaghaz": 1, "gheychi": 2}
    return skg[choice]


def number_choice(number):
    skg = {0: "sang", 1: "kaghaz", 2: "gheychi"}
    return skg[number]


def choice_comp():
    return random.choice(["sang", "kaghaz", "gheyvhi"])


def result(karbar_choice, comp_choice):
    global Karbar_scor
    global Comp_scor
    user = user_choice(karbar_choice)
    comp = user_choice(comp_choice)
    if user == comp:
        print("mosavi shodin ke")
    elif (user - comp) % 3 == 1:
        print("aarin userr to bordi")
        Karbar += 1
    else:
        print("man bordam !!!!")
        Comp_scor += 1


###################################################################
formates = tk.Text(master=root, width=29, height=13, bg="red")
formates.grid(column=0, row=3)
formates.insert(tk.END, root)


###########################################################
def sang():
    global entekhabe_karbar
    global entekhabe_comp
    entekhabe_karbar = "sang"
    entekhabe_comp = choice_comp()
    result(entekhabe_karbar, entekhabe_comp)


def kaghaz():
    global entekhabe_karbar
    global entekhabe_comp
    entekhabe_karbar = "kaghaz"
    entekhabe_comp = choice_comp()
    result(entekhabe_karbar, entekhabe_comp)


def gheychi():
    global entekhabe_karbar
    global entekhabe_comp
    entekhabe_karbar = "gheychi"
    entekhabe_comp = choice_comp()
    result(entekhabe_karbar, entekhabe_comp)


btn_1 = tk.Button(root, text="sang", bg="gray", command=sang)
btn_1.grid(column=0, row=1)
btn_2 = tk.Button(root, text="kaghaz", bg="pink", command=kaghaz)
btn_2.grid(column=0, row=2)
btn_3 = tk.Button(root, text="gheychi", bg="yellow", command=gheychi)
btn_3.grid(column=0, row=3)
root.mainloop()
