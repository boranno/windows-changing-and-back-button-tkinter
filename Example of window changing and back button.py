from tkinter import *
root=Tk()
root.title("Example of window changing and back button")
root.geometry("800x350")

bg1=PhotoImage(file="background1.png")
bg2=PhotoImage(file="background2.png")

window_1=Frame(root)
window_1.grid(row=0,column=0)

window_2=Frame(root)
window_2.grid(row=0,column=0)


def show_frame(frame):
    frame.tkraise()


background1=Label(window_1,image=bg1)
background1.pack()

btn1=Button(window_1,text="2nd window",bg="black",fg="white",font=(15),activebackground="black",command=lambda:show_frame(window_2))
btn1.place(x=400,y=240)

background2=Label(window_2,image=bg2)
background2.pack()

btn2=Button(window_2,text="1st window",bg="black",fg="white",font=(15),activebackground="black",command=lambda:show_frame(window_1))
btn2.place(x=400,y=240)


show_frame(window_1)
root.mainloop()