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


def MenuPage(user_id: int):
      global menuFrame, pay_button
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

      pay_button = Button(bottom,
                          bg="green",
                          fg="black",
                          borderless = 1,# type: ignore
                          highlightthickness=1,
                          font="verdana 25 bold",
                          text = "ชำระเงิน",
                          command=lambda: AddFromBasketToDatabase(user_id)
                        )                       
      pay_button.grid(row=2, column=0, columnspan=2)


def AddFoodToBasketPage(food_id: int, user_id: int):
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

      Button(bottom,
             text="ใส่ตะกร้า",
             bg="#DC7633",
             fg="black",
             borderless=1, # type: ignore
             highlightthickness=1,
             command = lambda: AddFoodToBasket(food_id, quantity_spy.get(), textBox.get("1.0",'end-1c'))).grid(row=2, column=0, sticky='e')
      
      for i in range(len(basket)):
            if basket[i][0] == food_id:
                  wantToChange = ifWantToChange()
                  if (wantToChange == False):
                        foodToBasketFrame.destroy()
                  else:
                        quantity_spy.set(basket[i][1])
                        textBox.insert(INSERT, basket[i][2])
                        break

     
def BasketFrame():
      basketFrame = Frame(menuFrame, bg="red")
      basketFrame.grid(row=0, rowspan=3, column=0, sticky="news")
      


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
                        user_id = result[0]
                        MenuPage(user_id)
                  else:
                        messagebox.showerror(
                              "Admin:", "Email or Password incorrect, please try again.")
                        pwd_spy.set("")
                        gmail_spy.set("")
                        gmail_ent.focus_force()



def ifWantToChange():
      return askyesno("confirmation", "เมนูนี้มีอยู่ในตะกร้าแล้ว ต้องการแก้ไขหรือไม่?")


def getMenuFromDatabase():
      '''
      Function to get Menu from database
      '''
      sql = "SELECT * FROM MenuTable"
      cursor.execute(sql)
      result = cursor.fetchall()

      return result


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
      
      found = False
      for i in range(len(basket)):
            if basket[i][0] == food_id:
                  found = True
                  tmp = list(basket[i])
                  tmp[1] = quantity
                  tmp[2] = extra
                  basket[i] = tuple(tmp)
                  messagebox.showinfo("admin", "แก้ไขสินค้าเรียบร้อยแล้ว")
                  break
      
      if found == False:
            basket.append((food_id, quantity, extra))
            messagebox.showinfo("admin", "เพิ่มสินค้าลงตะกร้าเรียบร้อยแล้ว")
            
      foodToBasketFrame.destroy()
      pay_button["text"] = "ชำระเงิน (" + str(len(basket)) + ")"
      print(basket)


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

      sql = "INSERT INTO OrderTable (user_id, order_id) VALUES (?, ?)"
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

food1_fullsize_img = PhotoImage(file="Images/food1.png").subsample(2,2)
food2_fullsize_img = PhotoImage(file="Images/food2.png").subsample(2,2)
food3_fullsize_img = PhotoImage(file="Images/food3.png").subsample(2,2)
food4_fullsize_img = PhotoImage(file="Images/food4.png").subsample(4,4)


LoginPage(root)

root.mainloop()
cursor.close()
conn.close()