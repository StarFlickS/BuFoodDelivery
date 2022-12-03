import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno

from tkmacosx import Button


def ConnectToDataBase():
      '''
      Connect to database and create connection and cursor for the program
      '''
      global conn, cursor
      conn = sqlite3.connect("BuFoodDeliveryDatabase.db")
      cursor = conn.cursor()


def CreateWindowsFrame():
      '''
      Create Root frame also call Main Windows frame for the program
      '''
      root = Tk()
      root.title("Bu Food Delivery")
      x = root.winfo_screenwidth() / 2 - w / 2
      y = root.winfo_screenheight() / 2 - h / 2
      root.geometry("%dx%d+%d+%d" %(w, h, x, y))
      root.rowconfigure(0, weight=1)  # type: ignore
      root.columnconfigure(0, weight=1)
      
      return root


def LoginPage(root):
      '''
      Create Page for Login purpose by getting BUmail and password from user and check with the database for match information, if so user can use the program
      '''
      global gmail_ent, pwd_ent, loginFrame
      loginFrame = Frame(root, bg="#EDBA9B")
      loginFrame.rowconfigure((0,1,2), weight=1) # type: ignore
      loginFrame.columnconfigure(0, weight=1)
      loginFrame.grid(row=0, column=0, sticky="news")

      top = Frame(loginFrame, bg="#EDBA9B")
      top.rowconfigure(0, weight=1)
      top.columnconfigure(0, weight=1)
      top.grid(row=0, column=0, sticky="news")

      middle = Frame(loginFrame, bg="#EDBA9B")
      middle.rowconfigure((0, 1, 2), weight=1) # type: ignore
      middle.columnconfigure((0, 1), weight=3) # type: ignore
      middle.grid(row=1, column=0, sticky="news")

      bottom = Frame(loginFrame, bg="#EDBA9B")
      bottom.rowconfigure(0, weight=1)
      bottom.columnconfigure(0, weight=1)
      bottom.grid(row=2, column=0, sticky="news")

      # Header
      Label(top,
            text="Bu Food Delivery",
            bg="#EDBA9B",
            fg="white",
            font="Verdana 35 bold").grid(row=0, column=0, sticky='s', pady=20)

      # Middle Frame
      # Icon Image
      Label(middle,
            image=icon_img,
            bg="#EDBA9B").grid(row=0, columnspan=2)
      
      # Gmail Entry
      Label(middle,
            text="Bumail:",
            bg="#EDBA9B",
            fg="white",
            font="Verdana 20 bold").grid(row=1, column=0, sticky='e')
      gmail_ent = Entry(middle,
                        textvariable=gmail_spy,
                        width=18,
                        fg="white",
                        borderwidth=0,
                        highlightthickness=0,
                        font="verdana 20",
                        insertbackground="white")
      gmail_ent.grid(row=1, column=1, sticky='w')

      # Password Entry
      Label(middle,
            text="Password:",
            bg="#EDBA9B",
            fg="white",
            font="Verdana 20 bold").grid(row=2, column=0, sticky='e')
      pwd_ent = Entry(middle,
                        textvariable=pwd_spy,
                        width=18,
                        fg="white",
                        borderwidth=0,
                        highlightthickness=0,
                        font="verdana 20",
                        insertbackground="white",
                        show = "●")
      pwd_ent.grid(row=2, column=1, sticky='w')
      
      gmail_ent.focus_force()

      # Bottom Frame
      Button(bottom,
            text="Login",
            fg="black",
            font="verdana 25 bold",
            bg="#DB7634",
            width=250,
            height=50,
            borderless=1, # type: ignore
            command=loginclicked).grid(row=0, column=0)  # type: ignore


def MenuPage():
      global menuFrame, basket_button, menu
      # get data from Menu table in database
      menu = getMenuFromDatabase()
      
      menuFrame = Frame(root, bg="#EDBA9B")
      menuFrame.rowconfigure(0, weight=2)
      menuFrame.rowconfigure(1, weight=1)
      menuFrame.rowconfigure(2, weight=15)
      menuFrame.columnconfigure(0, weight=1)
      menuFrame.grid(row=0, column=0, sticky="news")

      top = Frame(menuFrame, bg="#EDBA9B")
      top.rowconfigure((0,1), weight=1) # type: ignore
      top.columnconfigure(0, weight=1)
      top.grid(row=0, column=0, sticky="news")

      middle = Frame(menuFrame, bg="#EDBA9B")
      middle.rowconfigure(0, weight=1)
      middle.columnconfigure((0,1,2), weight=1) # type: ignore
      middle.grid(row=1, column=0, sticky="news")

      bottom = Frame(menuFrame, bg="#EDBA9B")
      bottom.rowconfigure((0,1,2), weight=1) # type: ignore
      bottom.columnconfigure((0,1), weight=1) #type: ignore
      bottom.grid(row=2, column=0, sticky="news")

      # Top layer
      Label(top,
            text= "Find good\nfood around you",
            font="verdana 35 bold",
            bg="#EDBA9B",
            fg="white",
            justify=LEFT).grid(row=0, column=0, sticky='w', padx=15, pady=20)

      Label(top,
            text= "Menu",
            bg="white",
            fg="#EDBA9B",
            font="verdana 30",
            width=15).grid(row=1, column=0, sticky='n')

      # Middle 
      Button(middle,
             text="Food",
             bg="#DB7634",
             fg="white",
             font="verdana 15",
             borderless=1, # type: ignore
             highlightthickness=1).grid(row=0, column=1, sticky='n')

      # Bottom Layer

      buttonFrm1 = Frame(bottom, bg="white")
      buttonFrm2 = Frame(bottom, bg="white")
      buttonFrm3 = Frame(bottom, bg="white")
      buttonFrm4 = Frame(bottom, bg="white")
      buttonFrm1.rowconfigure((0,1,2), weight=1) # type: ignore
      buttonFrm2.rowconfigure((0,1,2), weight=1) # type: ignore
      buttonFrm3.rowconfigure((0,1,2), weight=1) # type: ignore
      buttonFrm4.rowconfigure((0,1,2), weight=1) # type: ignore
      buttonFrm1.columnconfigure(0, weight=1)
      buttonFrm2.columnconfigure(0, weight=1)
      buttonFrm3.columnconfigure(0, weight=1)
      buttonFrm4.columnconfigure(0, weight=1)
      buttonFrm1.grid(row=0, column=0, sticky="news", padx=20, pady=20)
      buttonFrm2.grid(row=0, column=1, sticky="news", pady=20, padx=20)
      buttonFrm3.grid(row=1, column=0, sticky="news", padx=20, pady=20)
      buttonFrm4.grid(row=1, column=1, sticky="news", pady=20, padx=20)

      Button(buttonFrm1,
             image=food1_img,
             font="verdana 30",
             bg="white",
             borderless=1, # type: ignore
             highlightthickness=1,
             command=lambda: AddFoodToBasketPage(menu[0][0], user_id)).grid(row=0, column=0, sticky="news")
      
      Button(buttonFrm2,
             image=food2_img,
             font="verdana 30",
             bg="white",
             borderless=1, # type: ignore
             highlightthickness=1,
             command=lambda: AddFoodToBasketPage(menu[1][0], user_id)).grid(row=0, column=0, sticky="news")
      
      Button(buttonFrm3,
             image=food3_img,
             font="verdana 30",
             bg="white",
             borderless=1, # type: ignore
             highlightthickness=1,
             command=lambda: AddFoodToBasketPage(menu[2][0], user_id)).grid(row=0, column=0, sticky="news")
      
      Button(buttonFrm4,
             image=food4_img,
             font="verdana 30",
             bg="white",
             borderless=1, # type: ignore
             highlightthickness=1,
             command=lambda: AddFoodToBasketPage(menu[3][0], user_id)).grid(row=0, column=0, sticky="news")

      # Name and price Label
      # Name Label
      Label(buttonFrm1,
            text=menu[0][1],
            bg="white",
            fg="#EDBA9B",
            font="verdana 15 bold").grid(row=1, column=0)
      Label(buttonFrm2,
            text=menu[1][1],
            bg="white",
            fg="#EDBA9B",
            font="verdana 15 bold").grid(row=1, column=0)
      Label(buttonFrm3,
            text=menu[2][1],
            bg="white",
            fg="#EDBA9B",
            font="verdana 15 bold").grid(row=1, column=0)
      Label(buttonFrm4,
            text=menu[3][1],
            bg="white",
            fg="#EDBA9B",
            font="verdana 15 bold").grid(row=1, column=0)

      # Price Label
      Label(buttonFrm1,
            text=str(menu[0][2]) + " บาท",
            bg="white",
            fg="#EDBA9B",
            font="verdana 20 bold").grid(row=2, column=0)
      Label(buttonFrm2,
            text=str(menu[1][2]) + " บาท",
            bg="white",
            fg="#EDBA9B",
            font="verdana 20 bold").grid(row=2, column=0)
      Label(buttonFrm3,
            text=str(menu[2][2]) + " บาท",
            bg="white",
            fg="#EDBA9B",
            font="verdana 20 bold").grid(row=2, column=0)
      Label(buttonFrm4,
            text=str(menu[3][2]) + " บาท",
            bg="white",
            fg="#EDBA9B",
            font="verdana 20 bold").grid(row=2, column=0)

      basket_button = Button(bottom,
                          bg="green",
                          fg="black",
                          borderless = 1,# type: ignore
                          highlightthickness=1,
                          font="verdana 25 bold",
                          text = "ตะกร้า",
                          command= BasketFrame
                        )                       
      basket_button.grid(row=2, column=0, columnspan=2)


def AddFoodToBasketPage(food_id: int, user_id: int, isEdit = False, index = None):
      '''
      Create Page for adding food to the basket and prepare data(s) before putting in database
      '''
      global foodToBasketFrame
      foodToBasketFrame = Frame(menuFrame, bg="#EDBA9B")
      foodToBasketFrame.rowconfigure((0,1,2), weight=1) # type: ignore
      foodToBasketFrame.columnconfigure(0, weight=1)
      foodToBasketFrame.grid(row=0, rowspan=3, column=0, sticky="news")

      top = Frame(foodToBasketFrame, bg="#EDBA9B")
      top.rowconfigure(0, weight=1)
      top.rowconfigure(1, weight=5)
      top.rowconfigure(2, weight=1)
      top.columnconfigure(0, weight=1)
      top.grid(row=0, column=0, sticky="news")

      middle = Frame(foodToBasketFrame, bg="#EDBA9B")
      middle.rowconfigure(0, weight=1)
      middle.columnconfigure((0,1), weight=1) # type: ignore
      middle.grid(row=1, column=0, sticky="news")

      bottom = Frame(foodToBasketFrame, bg="#EDBA9B")
      bottom.rowconfigure((0,1,2), weight=1) # type: ignore
      bottom.columnconfigure(0, weight=1)
      bottom.grid(row=2, column=0, sticky="news")

      # go back button
      Button(top,
            image=goBack_img,
            bg="#EDBA9B",
            borderless = 1, # type: ignore
            highlightthickness=1,
            command=foodToBasketFrame.destroy).grid(row=0, column=0, sticky='w')

      # Show food Image 
      image_label = Label(top,bg="#EDBA9B")
      image_label.grid(row=1, column=0)

      if food_id == 1:
            image_label["image"] = food1_fullsize_img
      elif food_id == 2:
            image_label["image"] = food2_fullsize_img
      elif food_id == 3:
            image_label["image"] = food3_fullsize_img
      else:
            image_label["image"] = food4_fullsize_img

      # Show food name
      foodName = getFoodName(food_id)
      Label(top,
            text=foodName,
            bg="#EDBA9B",
            fg="black",
            font="verdana 30 bold").grid(row=2, column=0, sticky='n')
      
      # Middle
      foodPrice= getFoodPrice(food_id)
      Label(middle,
            bg="#F69C5E",
            fg="black",
            width=5,
            font="verdana 20 bold",
            text=str(foodPrice) + " บ.").grid(row=0, column=0)
      
      int_list = [x for x in range(1, 10 + 1)]
      quantity_spy.set(int_list[0])
      OptionMenu(middle, quantity_spy, *int_list).grid(row=0, column=1) # type: ignore

      # Bottom
      Label(bottom,
            text="เพิ่มเติม(ไม่เอาผัก ... ฯลฯ)",
            bg="#EDBA9B",
            font="verdana 25 bold",
            fg="black").grid(row=0, column=0, sticky='n')

      textFrame = Frame(bottom, bg="#EDBA9B")
      textFrame.grid(row=1, column=0, sticky="news", padx=20)

      textBox = Text(textFrame, font="verdana")
      textBox.grid(row=0, column=0, sticky="news")

      addButton = Button(bottom,
                  text="ใส่ตะกร้า",
                  bg="#DC7633",
                  fg="black",
                  borderless=1, # type: ignore
                  highlightthickness=1,
                  command = lambda: AddFoodToBasket(food_id, quantity_spy.get(), textBox.get("1.0",'end-1c')))
      addButton.grid(row=2, column=0, sticky='e')
      
      if isEdit == True:
            quantity_spy.set(basket[index][1]) # type: ignore
            textBox.insert(INSERT, basket[index][2]) # type: ignore
            addButton["text"] = "แก้ไขสินค้า"
            addButton["command"] = lambda: editBasket(index, quantity_spy.get(), textBox.get("1.0",'end-1c')) # type: ignore

            Button(bottom,
                   text="ลบสินค้า",
                   bg="red",
                   fg="black",
                   borderless=1, # type: ignore
                   highlightthickness=0,
                   command=lambda: deleteFromBasket(index)).grid(row=2, column=0, sticky='w') # type: ignore


def BasketFrame():
      global basketFrame
      if len(basket) == 0:
            return messagebox.showerror("Admin:", "ยังไม่มีสินค้าในตะกร้า")
      
      basketFrame = Frame(menuFrame, bg="#EDBA9B")
      basketFrame.rowconfigure(0, weight=1)
      basketFrame.rowconfigure(1, weight=5)
      basketFrame.rowconfigure(2, weight=1)
      basketFrame.columnconfigure(0, weight=1)
      basketFrame.grid(row=0, rowspan=3, column=0, sticky="news")
       
      top = Frame(basketFrame, bg="#EDBA9B")
      top.rowconfigure(0, weight=1)
      top.columnconfigure((0,1,2), weight=1) # type: ignore
      top.grid(row=0, column=0, sticky="news")

      middle = Frame(basketFrame, bg="#EDBA9B")
      middle.rowconfigure(0, weight=2)
      middle.rowconfigure(1, weight=1)
      middle.columnconfigure(0, weight=1)
      middle.grid(row=1, column=0, sticky="news")

      bot = Frame(basketFrame, bg="#EDBA9B")
      bot.rowconfigure(0, weight=1)
      bot.columnconfigure(0, weight=1)
      bot.grid(row=2, column=0, sticky="news")

      bot.grid(row=2, column=0, sticky="news")

      # Go back Button
      Button(top,
            image=goBack_img,
            bg="#EDBA9B",
            borderless = 1, # type: ignore
            highlightthickness=1,
            command=basketFrame.destroy).grid(row=0, column=0, sticky='w')

      Label(top,
            text="Order",
            fg="white",
            bg="#EDBA9B",
            font="verdana 30 bold").grid(row=0, column=1, sticky='w')
      
      # Middle
      canvasRows = [i for i in range(len(basket))]
      canvasRows = tuple(canvasRows)

      orderCanvas = Canvas(middle, bg="#EDBA9B", highlightthickness=1)
      orderCanvas.grid(row=0, column=0, sticky="news")

      scrollbar = Scrollbar(middle, orient=VERTICAL, command=orderCanvas.yview,width=5)
      scrollbar.grid(row=0, column=0, sticky='nse')

      orderCanvas.configure(yscrollcommand=scrollbar.set)
      orderCanvas.bind("<Configure>", lambda e: orderCanvas.configure(scrollregion= orderCanvas.bbox("all")))

      orderFrame = Frame(orderCanvas, bg="#EDBA9B")
      orderFrame.columnconfigure(0, weight=1)
      orderCanvas.create_window((1,1), width=w, window=orderFrame, anchor="nw")

      for i in range(len(basket)):
            frame = Frame(orderFrame, bg="white")
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure((0,1,2), weight=1) # type: ignore
            frame.grid(row=i, column=0, sticky="news", pady=10, padx=10)

            left = Frame(frame, bg="white")
            left.rowconfigure(0, weight=1)
            left.columnconfigure(0, weight=1)
            left.grid(row=0, column=0, sticky="news")

            center = Frame(frame, bg="white")
            center.rowconfigure((0,1), weight=1) # type: ignore
            center.columnconfigure(0, weight=1)
            center.grid(row=0, column=1, sticky="news")

            right = Frame(frame, bg="white")
            right.rowconfigure((0,1,2), weight=1) # type: ignore
            right.columnconfigure(0, weight=1)
            right.grid(row=0, column=2, sticky="news")
            
            imageLabel = Label(left, bg="white")
            imageLabel.grid(row=0, column=0)

            if basket[i][0] == 1:
                  imageLabel["image"] = food1_img
            elif basket[i][0] == 2:
                  imageLabel["image"] = food2_img
            elif basket[i][0] == 3:
                  imageLabel["image"] = food3_img
            else:
                  imageLabel["image"] = food4_img

            Label(center, 
                  text=menu[basket[i][0] - 1][1], 
                  font="verdana 20 bold", 
                  bg="white", 
                  fg="#EDBA9B").grid(row=0, column=0)
            Label(center, 
                  text=basket[i][2], 
                  font="verdana 10", 
                  bg="white", 
                  fg="#EDBA9B").grid(row=1, column=0)
            Label(right, 
                  text=str(menu[basket[i][0] - 1][2]) + " บ.", 
                  font="verdana 20 bold", 
                  bg="white", 
                  fg="#EDBA9B").grid(row=0, column=0)
            Label(right, 
                  text=str(basket[i][1]) + " ชิ้น", 
                  font="verdana 20 bold", 
                  bg="white", 
                  fg="#EDBA9B").grid(row=1, column=0)

            # Edit Button
            Button(right,
                  text="แก้ไข",
                  bg="red",
                  fg="black",
                  font="verdana 15 bold",
                  highlightthickness=0,
                  borderless=1, # type: ignore
                  command = lambda index = i: AddFoodToBasketPage(basket[index][0], user_id, True, index)).grid(row=3, column=0) 

      detailFrame = Frame(middle, bg="#EDBA9B")
      detailFrame.rowconfigure((0,1,2), weight=1) # type: ignore
      detailFrame.columnconfigure(0, weight=1)
      detailFrame.grid(row=1, column=0, sticky="news")

      # Items total and Delivery cost
      itemAmount = getItemAmount()
      costTotal = getCostTotal()
      Label(detailFrame,
            text="Item(s) total: " + str(itemAmount),
            fg="black",
            bg="#EDBA9B",
            font="verdana 25 bold").grid(row=0, column=0, sticky='se', pady=10, padx=20)
      Label(detailFrame,
            text="Delivery: ฟรี",
            fg="black",
            bg="#EDBA9B",
            font="verdana 25 bold").grid(row=1, column=0, sticky='ne', padx=20)
      Label(detailFrame,
            text="Total: " + str(costTotal) + " บาท.",
            fg="black",
            bg="#EDBA9B",
            font="verdana 25 bold").grid(row=2, column=0, sticky='ne', pady=10, padx=20)
      
      Button(bot,
            text="ชำระเงิน",
            bg="green",
            fg="black",
            font="verdana 25 bold",
            highlightthickness=0,
            borderless=1, # type: ignore
            command= lambda: paymentClicked(user_id)).grid(row=0, column=0) 


def loginclicked():
      '''
      Function when click Login in LoginPage
      Return: user information
      '''
      if gmail_spy.get() == "":
            messagebox.showwarning("Admin:", "Please enter your Email.")
            gmail_ent.focus_force()
      else:
            if pwd_spy.get() == "":
                  messagebox.showwarning("Admin:", "Please enter your Password.")
                  pwd_ent.focus_force()
            else:
                  sql = "SELECT * FROM LoginInformation WHERE gmail = ? AND pwd = ?"
                  cursor.execute(sql, [gmail_spy.get(), pwd_spy.get()])
                  result = cursor.fetchone()
                  if result:
                        messagebox.showinfo("Admin:", "Login Successfully.")
                        global user_id
                        user_id = result[0]
                        MenuPage()
                  else:
                        messagebox.showerror("Admin:", "Email or Password is incorrect, please try again.")
                        pwd_spy.set("")
                        gmail_spy.set("")
                        gmail_ent.focus_force()


def paymentClicked(user_id: int):
      AddFromBasketToDatabase(user_id)
      PaymentFrame()


def PaymentFrame():
      global paymentFrame
      paymentFrame = Frame(basketFrame, bg="#EDBA9B")
      paymentFrame.rowconfigure((0,1,2), weight=1) # type: ignore
      paymentFrame.columnconfigure(0, weight=1)
      paymentFrame.grid(row=0, rowspan=3, sticky="news")

      top = Frame(paymentFrame, bg="#EDBA9B")
      top.rowconfigure(0, weight=1)
      top.rowconfigure(1, weight=4)
      top.columnconfigure(0, weight=1)
      top.grid(row=0, column=0, sticky="news")

      middle = Frame(paymentFrame, bg="#EDBA9B")
      middle.rowconfigure(0, weight=1)
      middle.rowconfigure(1, weight=5)
      middle.columnconfigure(0, weight=1)
      middle.grid(row=1, column=0, sticky="news")

      bot = Frame(paymentFrame, bg="#EDBA9B")
      bot.rowconfigure(0, weight=1)
      bot.columnconfigure(0, weight=1)
      bot.grid(row=2, column=0, sticky="news")
      
      Label(top,
            text="ชำระเงินสำเร็จ",
            font="verdana 25 bold",
            fg="black",
            bg="#EDBA9B").grid(row=1, column=0, sticky='n')
      
      Label(top,
            image=payment_img,
            highlightthickness=0,
            borderwidth=0).grid(row=1,column=0,)
      
      Label(middle,
            text="วิธีการจัดส่ง: Delivery",
            font="verdana 25 bold",
            fg="black",
            bg="#EDBA9B").grid(row=0, column=0)
      
      canvasRows = [i for i in range(len(basket))]
      canvasRows = tuple(canvasRows)

      orderCanvas = Canvas(middle, bg="#EDBA9B", highlightthickness=1)
      orderCanvas.grid(row=1, column=0, sticky="news")

      scrollbar = Scrollbar(middle, orient=VERTICAL, command=orderCanvas.yview,width=5)
      scrollbar.grid(row=1, column=0, sticky='nse')

      orderCanvas.configure(yscrollcommand=scrollbar.set)
      orderCanvas.bind("<Configure>", lambda e: orderCanvas.configure(scrollregion= orderCanvas.bbox("all")))

      orderFrame = Frame(orderCanvas, bg="#EDBA9B")
      orderFrame.columnconfigure(0, weight=1)
      orderCanvas.create_window((1,1), width=w, window=orderFrame, anchor="nw")

      for i in range(len(basket)):
            frame = Frame(orderFrame, bg="#EDBA9B")
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure((0,1,2), weight=1) # type: ignore
            frame.grid(row=i, column=0, sticky="news", pady=10, padx=10)

            left = Frame(frame, bg="#EDBA9B")
            left.rowconfigure(0, weight=1)
            left.columnconfigure(0, weight=1)
            left.grid(row=0, column=0, sticky="news")

            center = Frame(frame, bg="#EDBA9B")
            center.rowconfigure((0,1), weight=1) # type: ignore
            center.columnconfigure(0, weight=1)
            center.grid(row=0, column=1, sticky="news")

            right = Frame(frame, bg="#EDBA9B")
            right.rowconfigure((0,1,2), weight=1) # type: ignore
            right.columnconfigure(0, weight=1)
            right.grid(row=0, column=2, sticky="news")
            
            imageLabel = Label(left, bg="#EDBA9B")
            imageLabel.grid(row=0, column=0)

            if basket[i][0] == 1:
                  imageLabel["image"] = food1_img
            elif basket[i][0] == 2:
                  imageLabel["image"] = food2_img
            elif basket[i][0] == 3:
                  imageLabel["image"] = food3_img
            else:
                  imageLabel["image"] = food4_img

            Label(center, 
                  text=menu[basket[i][0] - 1][1], 
                  font="verdana 20 bold", 
                  bg="#EDBA9B", 
                  fg="black").grid(row=0, column=0)
            Label(center, 
                  text=basket[i][2], 
                  font="verdana 10", 
                  bg="#EDBA9B", 
                  fg="black").grid(row=1, column=0)
            Label(right, 
                  text=str(menu[basket[i][0] - 1][2]) + " บ.", 
                  font="verdana 20 bold", 
                  bg="#EDBA9B", 
                  fg="black").grid(row=0, column=0)
            Label(right, 
                  text=str(basket[i][1]) + " ชิ้น", 
                  font="verdana 20 bold", 
                  bg="#EDBA9B", 
                  fg="black").grid(row=1, column=0)
      
      Label(bot,
      text="Total: " + str(getCostTotal()) + " บาท.",
      fg="black",
      bg="#EDBA9B",
      font="verdana 25 bold").grid(row=0, column=0)
      
      Button(bot,
      text="Exit",
      bg="red",
      font="verdana 30 bold",
      fg="black",
      borderless = 1, # type: ignore
      highlightthickness=1,
      command=exit).grid(row=1, column=0)
      
      
def deleteFromBasket(index: int):
      if wantToDelete() == False:
            return
      
      basket.pop(index)
      foodToBasketFrame.destroy()
      basketFrame.destroy()
      if len(basket) > 0:
            BasketFrame()
            basket_button["text"] = "ตะกร้า (" + str(len(basket)) + ")"
      else:
            basket_button["text"] = "ตะกร้า"


def editBasket(index: int, quantity: int, extra: str):
      tmp = list(basket[index])
      tmp[1] = quantity
      tmp[2] = extra
      basket[index] = tuple(tmp)
      messagebox.showinfo("admin", "แก้ไขสินค้าเรียบร้อยแล้ว")

      foodToBasketFrame.destroy()
      basketFrame.destroy()
      BasketFrame()


def wantToDelete():
      return askyesno("confirmation", "ต้องการลบสินค้านี้หรือไม่?")


def getMenuFromDatabase():
      '''
      Function to get Menu from database
      '''
      sql = "SELECT * FROM MenuTable"
      cursor.execute(sql)
      result = cursor.fetchall()

      return result


def getItemAmount():
      amount = 0
      for i in range(len(basket)):
            amount += basket[i][1]
      
      return amount


def getCostTotal():
      total = 0
      for i in range(len(basket)):
            price = menu[basket[i][0] - 1][2]
            total += (basket[i][1]) * price
      
      return total


def getFoodName(food_id: int):
      '''
      Function to get Food Name from database
      '''
      sql = "SELECT menu_name FROM MenuTable WHERE menu_ids = ?"
      cursor.execute(sql, [food_id])
      result = cursor.fetchone()
      
      return result


def getFoodPrice(food_id: int):
      '''
      Function to get Food Price from database
      '''
      sql = "SELECT menu_price FROM MenuTable WHERE menu_ids = ?"
      cursor.execute(sql, [food_id])
      result = cursor.fetchone()
      
      return result[0]


def AddFoodToBasket(food_id: int, quantity: int, extra: str):
      '''
      Function to Add food to basket
      '''
      if extra == "":
            extra = " "
      
      basket.append((food_id, quantity, extra))
      messagebox.showinfo("admin", "เพิ่มสินค้าลงตะกร้าเรียบร้อยแล้ว")
            
      foodToBasketFrame.destroy()
      basket_button["text"] = "ตะกร้า (" + str(len(basket)) + ")"


def AddFromBasketToDatabase(user_id: int):
      if len(basket) == 0:
            return messagebox.showerror("Admin:", "ยังไม่มีสินค้าในตะกร้า")
      
      food_ids = str(basket[0][0])
      quantities = str(basket[0][1])
      extras = str(basket[0][2])
      
      for i in range(len(basket) - 1):
            food_ids += "," + str(basket[i + 1][0])
            quantities += "," + str(basket[i + 1][1])
            extras += "," + str(basket[i + 1][2])
      
      sql = '''INSERT INTO Order_id_Table (food_id, quantity, extra) VALUES (?, ?, ?)'''
      cursor.execute(sql, [food_ids, quantities, extras])
      order_id = cursor.lastrowid
      conn.commit()

      sql = "SELECT * FROM OrderTable WHERE user_id = ?"
      cursor.execute(sql, [user_id])
      result = cursor.fetchone()
      # if user_id already exists
      if result: 
            sql = "SELECT order_id FROM OrderTable WHERE user_id = ?"
            cursor.execute(sql, [user_id])
            newOrderId = cursor.fetchone()
            newOrderId = newOrderId[0]
            newOrderId += "," + str(order_id)
            
            #Update order_id
            sql = "UPDATE OrderTable SET order_id = ? WHERE user_id = ?"
            cursor.execute(sql, [newOrderId, user_id])
      else:
            sql = "INSERT INTO OrderTable (user_id, order_id) VALUES (?,?)"
            cursor.execute(sql, [user_id, order_id])
      conn.commit()


# width and hight
w = 375
h = 812

ConnectToDataBase()

root = CreateWindowsFrame()

basket = []

# Login Spies
gmail_spy = StringVar()
pwd_spy = StringVar()

# AddFoodToBasket Spies
quantity_spy = IntVar()

gmail_spy.set("purin.sing@bumail.net")
pwd_spy.set("1.3boxbox")

# Loading Images
icon_img = PhotoImage(file="Images/Icon.png").subsample(3,3)
food1_img = PhotoImage(file="Images/food1.png").subsample(4,4)
food2_img = PhotoImage(file="Images/food2.png").subsample(4,4)
food3_img = PhotoImage(file="Images/food3.png").subsample(4,4)
food4_img = PhotoImage(file="Images/food4.png").subsample(8,8)

goBack_img = PhotoImage(file="Images/goBack.png").subsample(50,50)
payment_img = PhotoImage(file="Images/payment.png").subsample(3,3)

food1_fullsize_img = PhotoImage(file="Images/food1.png").subsample(2,2)
food2_fullsize_img = PhotoImage(file="Images/food2.png").subsample(2,2)
food3_fullsize_img = PhotoImage(file="Images/food3.png").subsample(2,2)
food4_fullsize_img = PhotoImage(file="Images/food4.png").subsample(4,4)


LoginPage(root)

root.mainloop()
cursor.close()
conn.close()