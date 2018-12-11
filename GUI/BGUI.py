from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
import signal,os
import preprocess


default_text={'eg :- Anurag kashyap,Karan Johar,etc' : 'eg :- Anurag kashyap,Karan Johar,etc', 'eg :- Shahrukh khan, Siddarth Malhotra etc' : 'eg :- Shahrukh khan, Siddarth Malhotra etc','eg :- Romance,action,thrill etc' : 'eg :- Romance,action,thrill etc','eg :- Baahubali, Ra.one, etc':'eg :- Baahubali, Ra.one, etc',"In crores eg : 70,60":"In crores eg : 70,60"}
drop_year =['2000', '2001', '2004', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
Certi =['UG','A','S','12A','15','18','Not Rated','PG','U','Unrated']
runtime =['0-90','90-120','120-150','150-180','180+']

class MainGUI:

    def __init__(self,master):
        self.root = master
        self.frame = Frame(master)
        self.frame.pack(fill =(BOTH))
        self.initializer()
##        self.set_frame()

    def initializer(self):
        self.label_1 = Label(self.frame,text="Movie Name",font="Helvetica 14 bold")
        self.label_2 = Label(self.frame,text="Genre",font="Helvetica 14 bold")
        self.label_3 = Label(self.frame,text="Star Cast",font="Helvetica 14 bold")
        self.label_4 = Label(self.frame,text="Director",font="Helvetica 14 bold")
        self.label_5 = Label(self.frame,text="Budget",font="Helvetica 14 bold")
        self.label_6 = Label(self.frame,text="Runtime",font="Helvetica 14 bold")
        
        self.entry_1 = Entry(self.frame)
        self.entry_1.insert(0,"eg :- Baahubali, Ra.one, etc")
        self.entry_1.config(fg="grey")
        self.entry_1.bind('<FocusIn>',  self.on_entry_click)
        self.entry_1.bind('<FocusOut>',  lambda event, a = "eg :- Baahubali, Ra.one, etc" : self.on_focusout(event, a))

        self.entry_2 = Entry(self.frame)
        self.entry_2.insert(0,"eg :- Romance,action,thrill etc")
        self.entry_2.config(fg="grey")
        self.entry_2.bind('<FocusIn>',  self.on_entry_click)
        self.entry_2.bind('<FocusOut>',  lambda event, a = "eg :- Romance,action,thrill etc" : self.on_focusout(event, a))

        self.entry_3 = Entry(self.frame)
        self.entry_3.insert(0,"eg :- Shahrukh khan, Siddarth Malhotra etc")
        self.entry_3.config(fg="grey")
        self.entry_3.bind('<FocusIn>',  self.on_entry_click)
        self.entry_3.bind('<FocusOut>',  lambda event, a = "eg :- Shahrukh khan, Siddarth Malhotra etc" : self.on_focusout(event, a))

        self.entry_4 = Entry(self.frame)
        self.entry_4.insert(0,"eg :- Anurag kashyap,Karan Johar,etc")
        self.entry_4.config(fg="grey")
        self.entry_4.bind('<FocusIn>',  self.on_entry_click)
        self.entry_4.bind('<FocusOut>',  lambda event, a = "eg :- Anurag kashyap,Karan Johar,etc" : self.on_focusout(event, a))

        
        self.entry_5 = Entry(self.frame)
        self.entry_5.insert(0,"In crores eg : 70,60")
        self.entry_5.config(fg="grey")
        self.entry_5.bind('<FocusIn>',  self.on_entry_click)
        self.entry_5.bind('<FocusOut>',  lambda event, a = "In crores eg : 70,60" : self.on_focusout(event, a))

        self.label_1.grid(row=2, sticky=W)
        self.label_2.grid(row=3, sticky=W)
        self.label_3.grid(row=4, sticky=W)
        self.label_4.grid(row=5, sticky=W)
        self.label_5.grid(row=6, sticky=W)

        self.entry_1.grid(row=2,columnspan=4,column=1)
        self.entry_2.grid(row=3,columnspan=4,column=1)
        self.entry_3.grid(row=4,columnspan=4,column=1)
        self.entry_4.grid(row=5,columnspan=4,column=1)
        self.entry_5.grid(row=6,columnspan=4,column=1)
        
        self.year = StringVar()
        self.runtime =StringVar()
        self.runtime.set('0-90')
##        self.Certification = StringVar()
##        self.Certification.set('UG')
        self.year.set('2000')
##        print(self.year.get())
        self.popupMenu = OptionMenu(self.frame, self.year, *drop_year)
        self.popupMenu3 = OptionMenu(self.frame, self.runtime, *runtime)
##        self.popupMenu2 = OptionMenu(self.frame, self.Certification, *Certi)
        self.popupMenu.grid(row=7,column=1)
        self.popupMenu3.grid(row=8,column=1)
##        self.popupMenu2.grid(row=7,column=1)
        self.drop1 = Label(self.frame,text="Year",font="Helvetica 14 bold")
        self.drop1.grid (row=7,column=0,sticky=W)
        self.drop3 = Label(self.frame,text="Runtime",font="Helvetica 14 bold")
        self.drop3.grid (row=8,column=0,sticky=W)
##        self.drop2 = Label(self.frame,text="Certification",font="Helvetica 14 bold")
##        self.drop2.grid (row=7,column=0,sticky=W)

        
        self.button =Button(self.frame, text= "Predict")
        self.button.bind('<Button-1>',self.Predict)

        self.button.grid(row=11,column=0,sticky=W)

        self.label_6 = Label(self.frame,text="Verdict -> ",font="Helvetica 14 bold")
        self.label_6.grid(row=13, sticky=W)

        self.Verdict = StringVar()
        self.Verdict.set("None")
        self.Verdict2 = StringVar()
        self.Verdict2.set("None")
        self.label_7 = ttk.Label(self.frame,textvariable=self.Verdict,font="Helvetica 14 ")
        self.label_7.grid(row=13,column=1,sticky=W)
        self.label_8 = ttk.Label(self.frame,textvariable=self.Verdict2,font="Helvetica 14 ")
        self.label_8.grid(row=13,column=4,sticky=E)

    def Predict(self,event):
        ''' function calling and updating variable Verdict'''
        self.result1 = preprocess.classify(self.entry_1.get(),self.entry_2.get(),self.entry_3.get(),self.entry_4.get(),self.year.get(),self.entry_5.get(),self.runtime.get())
        self.Verdict.set(self.result)
        if(self.result1[0]=="Flop !!"):
            self.result=1
        elif(self.result1[0]=="Hit !!"):
            self.result=2
        elif(self.result1[0]=="SuperHit !!"):
            self.result=3
        self.result = preprocess.revenue(self.entry_5.get(),self.result[1])
        self.Verdict2.set(round(self.result[0],2))
    
    def on_entry_click(self, event):

         if event.widget.config('fg') [4] == 'grey':
              event.widget.delete(0, "end" ) # delete all the text in the entry
              event.widget.insert(0, '') #Insert blank for user input
              event.widget.config(fg = 'black')

    def on_focusout(self, event, a):

        if event.widget.get() == '':
                event.widget.insert(0, default_text[a])
                event.widget.config(fg = 'grey')


if __name__=="__main__":

    root =Tk()
    root.wm_title("Bollywood Success Prediction")
    root.call("wm", "attributes", ".", "-alpha", "0.95") # Window Opacity 0.0-1.0
    x =int(2*root.winfo_screenwidth()/3)
    y =int(root.winfo_screenheight()/3)
    print(y)

##    root.config(bg='#a1dbcd')
    root.geometry('360x260+{0}+{1}'.format(x,y))
    start_GUI = MainGUI(root)
    root.mainloop()
        
        
