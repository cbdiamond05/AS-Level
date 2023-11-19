from tkinter import*
import tkinter.messagebox as box
window=Tk()
window.title('Message Box Example')
def dialog():
    var=box.askyesno('Message Box','Proceed?')
    if var==1:
        box.showinfo('Yes Box','Proceeding...')
    else:
        box.showwarnig('No Box','Cancelling...')
btn=Button(window,text='Click',command=dialog)
btn.pack(padx=150,pady=50)
window.mainloop()

from tkinter import*
import tkinter.messagebox as box
window=Tk()
window.title('Entry Example')
frame=Frame(window)
entry=Entry(frame)
def dialog():
    box.showinfo('Greetings','Welcome',+entry.get())
btn=Button(frame,text='Enter Name',command=dialog)
btn.pack(side=RIGHT,padx=5)
entry.pack(side=LEFT)
frame.pack(padx=20,pady=20)
window.mainloop()

from tkinter import*                  #No.3 MISSING INSTRUCTION#
import tkinter.messagebox as box
window=Tk()
window.title('Listbox Example')
listbox=Listbox(frame)
list.insert(1,'HTML5 in easy steps')
list.insert(2,'CSS3 in easy steps')
list.insert(3,'JavaScript in easy steps')
def dialog():
    box.showinfo('Selection','Your choice: '+\
    listbox.get(listbox.curselection()))
btn=Button(frame,text='Choose',command=dialog)
btn.pack(side=RIGHT,padx=50)
listbox.pack(side=LEFT)
frame.pack(padx=30,pady=30)
window.mainloop()

from tkinter import*
import tkinter.messagebox as box
window=Tk()
window.title('Radio Button Example')
frame=Frame(window)
book=StringVar()
radio_1=Radiobutton(frame,text='HTML5',\
        variable=book,value='HTML5 in easy steps')
radio_2=Radiobutton(frame,text='CSS3',\
        variable=book,value='CSSE in easy steps')
radio_3=RadioButton(frame,text='JS',\
        variable=book,value='JavaScript in easy steps')
radio_1.select()
def dialog():
    box.showinfo('Selection',\
    'Your Choice: \n'+book.get())
btn=Button(frame,text='Choose',command=dialog)
btn.pack(side=RIGHT,padx=5)
radio_1.pack(side=LEFT)
radio_2.pack(side=LEFT)
radio_3.pack(side=LEFT)
frame.pack(padx=30,pady=30)
window.mainloop()

from tkinter import*
import tkinter.messagebox as box
window=Tk()
window.title('Check Button Example')
frame=Frame(window)
var_1=IntVar()
var_2=IntVar()
var_3=IntVar()
book_1=Checkbutton(frame,text='HTML5',\
        variable=var_1,onvalue=1,offvalue=0)
book_2=Checkbutton(frame,text='CSS3',\
        variable=var_2,onvalue=1,offvalue=0)
book_3=Checkbutton(frame,text='JS',\
        variable=var_3,onvalue=1,offvalue=0)
def dialog():
    str='Your Choice:'
    if var_1.get==1:str+='\nHTML5 in easy steps'
    if var_2.get==1:str+='\nCSS3 in easy steps'
    if var_3.get==1:str+='\nJavaScript in easy steps'
    box.showinfo('Selection',str)
btn=Button(frame,text='Choose',command=dialog)
btn.pack(side=RIGHT,padx=5)
book_1.pack(side=LEFT)
book_2.pack(side=LEFT)
book_3.pack(side=LEFT)
frame.pack(padx=30,pady=30)
window.mainloop()

from tkinter import*
import tkinter.messagebox as box
window=Tk()
window.title('Image Example')
img=PhotoImage(file='python.gif')
label-Label(windoe,image=img,bg='yellow')
small_img=PhotoImage.subsample(img,x=2,y=2)
btn=Button(window,image=small_img)
txt=Text(window,width=25,height=7)
txt.image_craete('1.0',image=small_img)
txt.insert('1.1','Python Fun!')
can=\
Canvas(window,width=100,height=100,bg='cyan')
can.create_iamge((50,50),image=small_img)
can.create_line(0,0,100,100,width=25,fill='yellow')
label.pack(siade=TOP)
btn.pack(side=LEFT,padx=10)
txt.pack(side=LEFT)
can.pack(side=LEFT,padx=10)
window.mainloop()



#Green Booklet
from random import random,sample
num=random()
print('Random Integer 0-9: ',num)
nums=[];i=0
while i<6:
    nums.append(int(random()*10)+1)
    i+=1
print('Random Multiple Integers 1-10: ',nums)
nums=sample(rand(1,49),6)
print('Random Integer Sample 1-49: ',nums)

from tkinter import*
window=Tk()
img=PhotoImage(file='logo.gif')
imgLbl=Label(window,image=img)
label1=Label(window,relief='groove',width=2)
label2=Label(window,relief='groove',width=2)
label3=Label(window,relief='groove',width=2)
label4=Label(window,relief='groove',width=2)
label5=Label(window,relief='groove',width=2)
label6=Label(window,relief='groove',width=2)
gatBtn=Button(window)
resBtn=Button(window)
imgLbl.grid()
label1.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()
label6.grid()
getBtn.grid()
resBtn.grid()
window.mainloop()

imgLbl.grid(row=1,column=1,rowspan=2)
label1.grid(row=1,column=2,padx=10)
label2.grid(row=1,column=3,padx=10)
label3.grid(row=1,column=4,padx=10)
label4.grid(row=1,column=5,padx=10)
label5.grid(row=1,column=6,padx=10)
label6.grid(row=1,column=7,padx=(10,20))
getBtn.grid(row=2,column=2,columnspan=4)
resBtn.grid(row=2,column=6,columnspan=2)

label1.configure(text='...')
label2.configure(text='...')
label3.configure(text='...')
label4.configure(text='...')
label5.configure(text='...')
label6.configure(text='...')
resBtn.configure(state=DISABLED)
