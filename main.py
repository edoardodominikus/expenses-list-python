import sys
from datetime import*
import pycategories
import pyrecord
import tkinter
from tkinter import ttk 
from tkinter import messagebox
categories = pycategories.Categories()
records = pyrecord.Records()



#root
root = tkinter.Tk()
#frame
f=tkinter.Frame(root,width = 1000, height = 500)
f.pack_propagate(0)
f.pack()


#entry
e1 = tkinter.Entry(f,bd = 5)
e1.pack()
e1.place(x = 120,y = 20)

e2 = tkinter.Entry(f,bd = 5)
e2.pack()
e2.place(x = 550,y = 70)

e3 = tkinter.Entry(f,bd = 5)
e3.pack()
e3.place(x = 550, y = 130)

e4 = tkinter.Entry(f,bd = 5)
e4.pack()
e4.place(x = 550, y = 190)

e5 = tkinter.Entry(f,bd = 5)
e5.pack()
e5.place(x = 550, y = 220)
#button
b0 = tkinter.Button(f,text = 'Quit',command = root.destroy)
b0.pack()
b0.place(x = 670,y = 20)

def cari():
  category = e1.get()
  target_categories = categories.find_subcategories(category)
  
  temp = list(filter(lambda n : n.category in target_categories ,records._records))
  
        # print("Date"+" "*10+"Categories"+" "*5+"Description"+" "*5+"Amount")
        # print("=================================")
        # for i in temp:
        #     print(f"{i.date:<20s}{i.category:<20s} {i.description:^20s} {str(i.amount):>20s}")
    
        # print("=================================")
  total = 0
  for i in temp:
    total = total + i.amount
  var.set('The total amount above is %d'%total)
  square.delete(0,"end")
  for j,i in enumerate(temp):
       square.insert(j,i.date +" "+i.category +" " + i.description +" " + str(i.amount))
b1 = tkinter.Button(f,text = 'Find',command = cari)
b1.pack()
b1.place(x = 300,y = 20)

def hapus():
  e1.delete(0,tkinter.END)
  var.set("Now you have %d dollars"%records._initial_money)
  square.delete(0,"end")
  for j,i in enumerate(records._records):
            square.insert(j,i.date +" "+i.category +" " + i.description +" " + str(i.amount))
  

b2 = tkinter.Button(f,text = 'Reset',command = hapus)
b2.pack()
b2.place(x = 360,y = 20)


def money_start():
  upd = int(e2.get())
  records.money(upd)
  var.set("Now you have %d dollars"%records.get_money())
  e2.delete(0,"end")

  
b3 = tkinter.Button(f,text = 'Update',command = money_start)
b3.pack()
b3.place(x = 660,y = 100)

def hapus():
  try:
    index = square.curselection()[0]
    records.delete(index)
    square.delete(0,"end")

    for j,i in enumerate(records._records):
       square.insert(j,i.date +" "+i.category +" " + i.description +" " + str(i.amount))
  except IndexError:
    
    messagebox.showerror("Error","Error, please select the index!")


b4 = tkinter.Button(f,text = 'Delete',command = hapus)
b4.pack()
b4.place(x = 290,y = 360)




#e4.get().strip().split("-")[0]
def tambah():
  
  if(len(e3.get())==0):
    records.add(combo.get().strip().split("-")[1]+" "+ e4.get()+" "+e5.get(),categories)

  else:
    try:
      date.fromisoformat(e3.get())
      records.add(e3.get() +" "+combo.get().strip().split("-")[1]+" "+ e4.get()+" "+e5.get(),categories)
    except ValueError:
      messagebox.showerror("Error","The format of date should be YYYY-MM-DD.Fail to add a record.")
      
    


  square.delete(0,"end")

  for j,i in enumerate(records._records):
       square.insert(j,i.date +" "+i.category +" " + i.description +" " + str(i.amount))

  e3.delete(0,"end")
  e4.delete(0,"end")
  e5.delete(0,"end")
  combo.delete(0,"end")
  var.set("Now you have "+str(records.get_money())+ " dollars")
b5 = tkinter.Button(f,text = 'Add a record',command = tambah)

b5.pack()
b5.place(x = 620,y = 260)
#label
find = tkinter.Label(f,text = 'Find Category')
find.pack()
find.place(x = 20, y = 20)


var = tkinter.StringVar()
var.set("Now you have "+str(records.get_money())+ " dollars")
balance = tkinter.Label(f,textvariable = var)
balance.pack()
balance.place(x = 50, y = 370)

money = tkinter.Label(f,text = 'Initial Money')
money.pack()
money.place(x = 450, y = 70)

datee = tkinter.Label(f,text = 'Date')
datee.pack()
datee.place(x = 450, y = 130)

categoryy = tkinter.Label(f,text = 'Category')
categoryy.pack()
categoryy.place(x = 450, y = 160)

desc = tkinter.Label(f,text = 'Description')
desc.pack()
desc.place(x = 450, y = 190)

amountt = tkinter.Label(f,text = 'Amount')
amountt.pack()
amountt.place(x = 450, y = 220)


#listbox
square = tkinter.Listbox(f,height = 15, width = 40,)
global j
for j,i in enumerate(records._records):
            square.insert(j,i.date +" "+i.category +" " + i.description +" " + str(i.amount))

square.pack()
square.place(x = 50, y = 75)
#scrollbar
scrollbar = tkinter.Scrollbar(f)
scrollbar.pack(side="right", fill="y")
scrollbar.config(command=square.yview)
#scrollbar.config(yscrollcommand = scrollbar.set) 


square.config(yscrollcommand=scrollbar.set)
#combobox
def categ():
  combo["value"] = ['-expense','  -food', '   -meal', '   -snack', '   -drink', '  -transportation', '   -bus', '   -railway', '  -income', '   -salary', '   -bonus']
combo = ttk.Combobox(f,postcommand = categ)

combo.pack()
combo.place( x = 550, y = 160)

tkinter.mainloop()
records.save()
      
# while True:
#     command = input("What do you want to do(add / view / delete / view categories / find / exit)?")
#     if command == 'add':
#         record = input('Add an expense or income record with description and amount:\n')
#         records.add(record, categories)
#     elif command == 'view':
#         records.view()
#     elif command == 'delete':
#         delete_record = input("Which record do you want to delete? ")
#         records.delete(delete_record)
#     elif command == 'view categories':
#         categories.view()
#     elif command == 'find':
#         category = input('Which category do you want to find? ')
#         target_categories = categories.find_subcategories(category)
#         records.find(target_categories)
#     elif command == 'exit':
#         records.save()
#         break
#     else:
#         sys.stderr.write('Invalid command. Try again.\n')
