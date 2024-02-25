from tkinter import *


def click():
       t1 = en1.get().lower()
       list1 = []
       list1.extend(t1)
       list1.reverse()
       x = ''.join(list1)
       if x == t1:
              l1.config(text='Palindrome', background='green', foreground='black')
       else:
              l1.config(text='Not Palindrome', background='red', foreground='black')


def click2():
       window.destroy()


window = Tk()
window.title("|^_^| Palindrome checker")
window.minsize(350, 150)
window.maxsize(350, 150)
en1 = Entry(window, background='lightyellow', foreground='black', width=50)
en1.pack(pady=5)
l1 = Label(window, text="")
l1.pack(pady=5)
b1 = Button(window, text="Check", background='green', foreground='black', width=20, command=click)
b1.pack(pady=5)
b2 = Button(window, text='Exit', background='red', foreground='black', width=20, command=click2)
b2.pack(pady=5)
window.mainloop()
