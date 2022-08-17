from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from functools import partial

#root widget--------------------------------------------------------------------

#creating root widget
root = Tk()
root.configure(bg="alice blue")
root.title('Hotel Management System')
#initial state of the window will be maximized
root.state('zoomed')

#assigning the weights of columns and rows in the grid for root widget
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=3)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=15)



#title frame--------------------------------------------------------------------


#creating the title frame and inserting it in root using grid
frame_title = LabelFrame(root, bg="DodgerBlue4")
frame_title.grid_propagate(False)
frame_title.grid(row=0, column=0, columnspan=2, stick="nsew")

frame_title.rowconfigure(0, weight=1)
frame_title.columnconfigure(0, weight=1)

#creating a label title in frame_title and inserting using grid
lab_title = Label(frame_title, text="Restaurant Managent System", font=("courier prime",50,"bold"), fg="white", bg="DodgerBlue4")
lab_title.grid_propagate(False)
lab_title.grid(row=0, column=0, stick="nsew")



#button frame-------------------------------------------------------------------


#creating frame_buttons in root
frame_buttons = LabelFrame(root, bg="LemonChiffon")
frame_buttons.grid_propagate(False)
frame_buttons.grid(row=1, column=0, columnspan=2, stick="nsew")

frame_buttons.rowconfigure(0, weight=1)


#function for list box of menu items
def show(event):
    global img
    #getting index of selected item
    n=listbox_menu.curselection()

    #forgeting labels that need to be replaced
    for label in top.grid_slaves():
        if int(label.grid_info()["row"]) < 2 and int(label.grid_info()["column"]) == 1:
            label.grid_forget()

    #creating new image label based on selected index in listbox
    img = Image.open("Images/"+menu_items_list[n[0]]+".png")
    img = img.resize((500,500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label_menu_img=Label(top,image=img,bg="alice blue")
    label_menu_img.grid(row=1,column=1,pady=5)
    #creating new item name label based on selected index in listbox
    label_item_name = Label(top, text=menu_items_list[n[0]],font=("courier prime",30,"bold"),fg="DodgerBlue4",bg="alice blue")
    label_item_name.grid(row=0,column=1,pady=5)


#for new window (Menu details)
def open1():
    #using global variables for use in other methods
    global listbox_menu
    global top
    global img
    #creating window
    top=Toplevel()
    top.configure(bg="alice blue")
    top.title("Menu Details")

    #creating a listbox in top window
    listbox_menu=Listbox(top,bg="alice blue")
    listbox_menu.grid(row=0,column=0,rowspan=3,stick=N+S)

    #adding all the images in listbox
    for imgname in menu_items_list:
        listbox_menu.insert(END,imgname)

    #initial item name
    label_item_name = Label(top, text=menu_items_list[0],font=("courier prime",30,"bold"), fg="DodgerBlue4",bg="alice blue")
    label_item_name.grid(row=0,column=1,pady=5)
    #showing initial image
    img = Image.open("Images/"+menu_items_list[0]+".png")
    img = img.resize((500,500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label_menu_img=Label(top,image=img,bg="alice blue")
    label_menu_img.grid(row=1,column=1,pady=5)

    #calling show method to show selected image
    listbox_menu.bind("<<ListboxSelect>>",show)

    #exit button for top
    button_exit_top = Button(top, text="Back to Home Page", command=top.destroy, fg="white", bg="DodgerBlue4", borderwidth=5,padx=5,pady=5)
    button_exit_top.grid(row=2,column=1,pady=5)


#menu_details_button in frame_button
button_menu_details = Button(frame_buttons,text="Menu Details",command=open1, height=2, width=20, bg="#F0F8FF")
button_menu_details.grid_propagate(False)
button_menu_details.grid(row=0, column=0, padx=5, pady=5)


#about_us_button in frame_button
def about_us():
    global img1

    #creating new window
    top1=Toplevel()
    #top1.state('zoomed')
    top1.title("About Us")
    top1.configure(bg="#F0F8FF")
    
    #configuring weights in grid system
    top1.columnconfigure(0,weight=1)
    top1.rowconfigure(0,weight=1)
    top1.rowconfigure(1,weight=1)
    top1.rowconfigure(2,weight=1)
    top1.rowconfigure(3,weight=1)

    #getting info from text file
    info = ""
    with open('Aboutus.txt','r') as f1:
        lines = f1.readlines()
        for line in lines:
            info = info + line
    
    #displaying image
    img1 = Image.open("Images/about.png")
    img1 = img1.resize((300,300), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    #displaying title,info and back button
    Label(top1,text="About Us",font=("courier prime",50,"bold"), fg="white", bg="DodgerBlue4").grid(row=0,column=0,sticky="nsew")
    Label(top1,image=img1,bg="#F0F8FF").grid(row=1,column=0,pady=10,sticky="nsew")
    Label(top1,text=info,bg="#F0F8FF").grid(row=2,column=0,pady=10,sticky="nsew")
    Button(top1,text="Back to Home Page",command=top1.destroy,padx=10,pady=7,fg="white",bg="DodgerBlue4",borderwidth=5).grid(row=3,column=0)


#about us button will open about us window
button_about_us = Button(frame_buttons,text="About us", command=about_us, height=2, width=20, bg="#F0F8FF")
button_about_us.grid_propagate(False)
button_about_us.grid(row=0, column=1, padx=5, pady=5)

#exit_root_button in frame_button
button_exit_root = Button(frame_buttons,text="Quit", command=root.destroy, height=2, width=20, bg="#F0F8FF")
button_exit_root.grid_propagate(False)
button_exit_root.grid(row=0, column=2, padx=5, pady=5)



#menu frame---------------------------------------------------------------------


#creating menu frame
frame_menu = LabelFrame(root, bg="alice blue")
frame_menu.grid_propagate(False)
frame_menu.grid(row=2, column=0, stick="nsew")

frame_menu.rowconfigure(0, weight=1)
frame_menu.columnconfigure(0, weight=99)
frame_menu.columnconfigure(1, weight=1)

#creating a canvas in menu frame to use scroll bar on
canvas = Canvas(frame_menu,bg="alice blue")
canvas.grid_propagate(False)
canvas.grid(row=0,column=0, stick="nsew")
#scroll bar for canvas
scroll_bar = ttk.Scrollbar(frame_menu, orient="vertical", command=canvas.yview)
scroll_bar.grid_propagate(False)
scroll_bar.grid(row=0,column=1, stick="nsew")

canvas.configure(yscrollcommand=scroll_bar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox('all')))

#frame inside canvas that will have all the widgets
frame_canvas = Frame(canvas,bg="alice blue")
canvas.create_window((0,0), window=frame_canvas)

#when clicking a checkbox corresponding textbox will change its state
def check_1(i):
    if str(textbox[i]['state']) == 'disabled':
        textbox[i].configure(state=NORMAL)
        textbox[i].focus()
    elif str(textbox[i]['state']) == 'normal':
        textbox[i].delete('0',END)
        textbox[i].configure(state=DISABLED)


#getting menu item names and price from text file
menu_items_list=[]
menu_items_price_list=[]
with open('Items.txt','r') as f2:
    lines=f2.readlines()
    for line in lines:
        line = line.strip('\n')
        words = line.split(',')
        menu_items_list.append(words[0])
        menu_items_price_list.append(int(words[1]))

#holds the entry(text box) object for each menu item quantity
textbox=[]
#holds the checkbutton object for each menu item
Checkbox=[]
#list of tkinter variables for checkbutton
var = []
for i in range(16):
    var.append(IntVar())

#label for headers in frame_canvas
label_check = Label(frame_canvas, text="Item Name",font=20,fg="black",bg="alice blue")
label_check.grid(row=0,column=0,stick=W,padx=20)
label_q = Label(frame_canvas, text="Qty",font=20,fg="black",bg="alice blue")
label_q.grid(row=0,column=1,stick=W,padx=20)
label_pr = Label(frame_canvas, text="Price",font=20,fg="black",bg="alice blue")
label_pr.grid(row=0,column=3,stick=W,padx=20)

#displaying all menu items and its related widgets on frame_menu
for i in range(0,len(menu_items_list)):
    #creating entry objects, putting it in grid and appending it to textbox list
    e=Entry(frame_canvas,width=10,state=DISABLED,fg="black",font=20,bg="LemonChiffon")
    e.insert(0,"0")
    e.grid(row=i+1,column=1,stick=W,padx=20)
    textbox.append(e)
    #creating checkbutton objects, putting it in grid and appending it to textbox list
    c=Checkbutton(frame_canvas,text=menu_items_list[i],font=15,bg="alice blue",fg="DodgerBlue4",variable=var[i],height=3,command=partial(check_1,i))
    Checkbox.append(c)
    c.grid(row=i+1,column=0,stick=W,padx=20)
    #label to display price of each item
    label_price = Label(frame_canvas, text=str(menu_items_price_list[i])+" Rs.",font=15,fg="DodgerBlue4",bg="alice blue")
    label_price.grid(row=i+1,column=3,stick=W,padx=20)


#calculates and shows the bill of the order placed in bill frame
def show_bill():
    #forgeting unwanted labels
    for label in frame_bill.grid_slaves():
        if int(label.grid_info()["row"]) > 4:
            label.grid_forget()
        
    final_price=0
    for i in range(len(menu_items_list)):
        #checking validity of amount entered
        if str(textbox[i]['state']) == 'normal':
            if not textbox[i].get().isnumeric():
                #displaying error message for invalid amount and setting bill and menu frame to initial look
                messagebox.showerror("Error", "Invalid : Amount of Item can only be Integer geater than 0")
                for label in frame_bill.grid_slaves():
                    if int(label.grid_info()["row"]) > 4:
                        label.grid_forget()
                for i in range(0,len(menu_items_list)):
                    textbox[i].delete('0',END)
                    textbox[i].configure(state=DISABLED)
                    var[i].set(0)
                return

            if int(textbox[i].get())<0:
                #displaying error message for invalid amount and setting bill and menu frame to initial look
                messagebox.showerror("Error", "Invalid : Amount of Item can only be Integer geater than 0")
                for label in frame_bill.grid_slaves():
                    if int(label.grid_info()["row"]) > 4:
                        label.grid_forget()
                for i in range(0,len(menu_items_list)):
                    textbox[i].delete('0',END)
                    textbox[i].configure(state=DISABLED)
                    var[i].set(0)
                return
            else:
                #menu item name
                label_menu_item = Label(frame_bill, text=str(menu_items_list[i]),bg="alice blue",fg="grey",font=12)
                label_menu_item.grid_propagate(False)
                label_menu_item.grid(row=i+5,column=0,padx=10,pady=1)

                #amount of item ordered
                label_amount = Label(frame_bill, text=str(textbox[i].get())+"x",bg="alice blue",fg="grey",font=12)
                label_amount.grid_propagate(False)
                label_amount.grid(row=i+5,column=1,padx=10,pady=1)
                #price of the item
                label_item_price = Label(frame_bill, text=str(menu_items_price_list[i]),bg="alice blue",fg="grey",font=12)
                label_item_price.grid_propagate(False)
                label_item_price.grid(row=i+5,column=2,padx=10,pady=1)

                #total price of each item
                total=float(menu_items_price_list[i])*int(textbox[i].get())
                label_total=Label(frame_bill,text="= "+str(total),font=12,bg="alice blue",fg="grey")
                label_total.grid_propagate(False)
                label_total.grid(row=i+5,column=3,padx=10,pady=1)

                final_price+=total

    label_line1 = Label(frame_bill, text="_____________________________________",font=20,fg="black",bg="alice blue")
    label_line1.grid_propagate(False)
    label_line1.grid(row=i+6,column=0,columnspan=4,padx=3)
    #final price label
    label_final_price = Label(frame_bill, text="Total : "+str(final_price),font=20,fg="black",bg="alice blue")
    label_final_price.grid_propagate(False)
    label_final_price.grid(row=i+7,column=3,pady=10,stick="nsew")
    #setting the widgets in menu to initial states
    for i in range(0,len(menu_items_list)):
        textbox[i].delete('0',END)
        textbox[i].configure(state=DISABLED)
        var[i].set(0)


#submit button will show the bill from ordered items
submit_button=Button(frame_canvas,text="submit order",bg="DodgerBlue4",fg="white",font=15,command=show_bill,borderwidth=5)
submit_button.grid(row=len(menu_items_list)+3,column=0,columnspan=5,pady=10)

#frame bill---------------------------------------------------------------------

#creating bill frame
frame_bill = LabelFrame(root, bg="alice blue")
frame_bill.grid_propagate(False)
frame_bill.grid(row=2, column=1, stick="nsew")

frame_bill.columnconfigure(0,weight=1)
frame_bill.columnconfigure(1,weight=1)
frame_bill.columnconfigure(2,weight=1)
frame_bill.columnconfigure(3,weight=1)

#labels for the restaurant name and headers in bill
label_name= Label(frame_bill, text="JDK Restaurant",font=("courier prime",30,"bold"),fg="DodgerBlue4",bg="alice blue")
label_name.grid_propagate(False)
label_name.grid(row=0,column=0,columnspan=4,pady=10,stick="nsew")
label_check = Label(frame_bill, text="Item Name",font=20,fg="black",bg="alice blue")
label_check.grid_propagate(False)
label_check.grid(row=1,column=0,padx=6,pady=3,stick="nsew")
label_q = Label(frame_bill, text="Qty",font=20,fg="black",bg="alice blue")
label_q.grid_propagate(False)
label_q.grid(row=1,column=1,padx=6,pady=3,stick="nsew")
label_pr = Label(frame_bill, text="Price",font=20,fg="black",bg="alice blue")
label_pr.grid_propagate(False)
label_pr.grid(row=1,column=2,padx=6,pady=3,stick="nsew")
label_prt = Label(frame_bill, text="Total Price",font=20,fg="black",bg="alice blue")
label_prt.grid_propagate(False)
label_prt.grid(row=1,column=3,padx=6,pady=3,stick="nsew")
label_line = Label(frame_bill, text="_____________________________________",font=20,fg="black",bg="alice blue")
label_line.grid_propagate(False)
label_line.grid(row=2,column=0,columnspan=4,pady=3,stick="nsew")


root.mainloop()