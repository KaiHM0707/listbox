from tkinter import *

def insert_data():
    extract = inputbox.get()
    if extract:
        l1.insert(END, extract)
        inputbox.delete(0, END)
    

    

scr = Tk()
scr.geometry("300x250")
scr.title("Places to go")
sign = Label(scr, text="places:")
inputbox = Entry(scr, text="what's in the list?")
inputbox.pack(side=BOTTOM)
sign.pack()
#Create a list
l1 = Listbox(scr, height=10, width=15, bg="lightgreen", fg="black", font="Helvetica", activestyle="dotbox")
#l1.insert(1,"Seattle")
##l1.insert(2,"London")
#l1.insert(3,"Germany")
#l1.insert(4,"Tokyo")
#l1.insert(5,"Bozeman")
#l1.insert(6,"Silicon valley")

#insighting items using loops
data = ["Apple", "Computer", "Phone", "Wallet", "Water"]
for i in data:
    l1.insert(END, i)
l1.pack()

insert_but = Button(scr, text="Insert", command=insert_data)
insert_but.pack(side=LEFT)
delete_but = Button(scr, text="Delete")
delete_but.pack(side=RIGHT)
getdata_but = Button(scr, text="Get Data")
getdata_but.pack(side=TOP)







scr.mainloop()