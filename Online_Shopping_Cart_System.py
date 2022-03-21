from tkinter import *
from tkinter import messagebox
import random
import datetime
from abc import ABC,abstractmethod

#========================================== CREATE ACCOUNT Class =====================================================#

class CREATE_ACCOUNT:
    '''this class helps user to create account for Online Shopping Cart'''
    def __init__(self):
        root0 = Tk()
        self.root0 = root0
        self.root0.title("Create Account")
        self.root0.config(background="powder blue")
        self.root0.minsize(506, 550)
        self.root0.maxsize(506, 550)
        self.bg_color = "#074463"

        #============================= Frames ================================================================#

        self.AB3 = Frame(self.root0, bg=self.bg_color, bd=20, relief=RIDGE).grid()
        self.AB4 = Frame(self.AB3, bd=10, width=506, height=80, relief=RIDGE, bg=self.bg_color).grid(row=0, column=0,
                                                                                                     columnspan=4)
        self.AB5 = Frame(self.AB3, bd=14, padx=10, bg=self.bg_color, relief=RIDGE).grid(row=1, column=0)

        #============================== Variables =============================================================#

        self.user = StringVar()
        self.fname = StringVar()
        self.lname = StringVar()
        self.password = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.address = StringVar()

        self.create_account()

    def create_account(self):

        #============================== Labels & Entries ======================================================#

        n2 = Label(self.AB4, text="Create Account", font=("Arial", 15, "bold"), justify=CENTER,
                   bg=self.bg_color, fg="Cornsilk", pady=9, bd=5).grid(row=0, column=1)

        l1 = Label(self.AB5, text="Username", font=("arial", 12, "bold"), bg=self.bg_color, fg="Cornsilk").grid(row=1,
                column=0,padx=10,pady=10,sticky="w")
        self.e1 = Entry(self.AB5, width=10, font=("arial", 12, "bold"), textvariable=self.user, bd=5, relief=SUNKEN). \
            grid(row=1, column=3, padx=10, pady=10)
        l2 = Label(self.AB5, text="First Name", font=("arial", 12, "bold"), bg=self.bg_color, fg="Cornsilk") \
            .grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.e2 = Entry(self.AB5, width=10, font=("arial", 12, "bold"), textvariable=self.fname, bd=5, relief=SUNKEN). \
            grid(row=2, column=3, padx=10, pady=10)
        l3 = Label(self.AB5, text="Last Name", font=("arial", 12, "bold"), bg=self.bg_color, fg="Cornsilk") \
            .grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.e3 = Entry(self.AB5, width=10, font=("arial", 12, "bold"), textvariable=self.lname, bd=5, relief=SUNKEN). \
            grid(row=3, column=3, padx=10, pady=10)
        l4 = Label(self.AB5, text="Password", font=("arial", 12, "bold"), bg=self.bg_color, fg="Cornsilk") \
            .grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.e4 = Entry(self.AB5, width=10, font=("arial", 12, "bold"), textvariable=self.password, bd=5, relief=SUNKEN) \
            .grid(row=4, column=3, padx=10, pady=10)
        l5 = Label(self.AB5, text="Phone Number", font=("arial", 12, "bold"), bg=self.bg_color, fg="Cornsilk") \
            .grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.e5 = Entry(self.AB5, width=10, font=("arial", 12, "bold"), textvariable=self.phone, bd=5, relief=SUNKEN) \
            .grid(row=5, column=3, padx=10, pady=10)
        l6 = Label(self.AB5, text='Email Address', font=("arial", 12, "bold"), bg=self.bg_color, fg="Cornsilk") \
            .grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.e6 = Entry(self.AB5, width=10, font=("arial", 12, "bold"), textvariable=self.email, bd=5, relief=SUNKEN) \
            .grid(row=6, column=3, padx=10, pady=10)
        l7 = Label(self.AB5, text='Address', font=("arial", 12, "bold"), bg=self.bg_color, fg="Cornsilk") \
            .grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.e7 = Entry(self.AB5, width=10, font=("arial", 12, "bold"), textvariable=self.address, bd=5, relief=SUNKEN) \
            .grid(row=7, column=3, padx=10, pady=10)

        #=================================== Check Entries =======================================================#

        def check():
            u_name=self.user.get()
            f_name=self.fname.get()
            l_name=self.lname.get()
            p_password=self.password.get()
            p_phone=self.phone.get()
            a_address=self.address.get()
            e_mail=self.email.get()
            if u_name == "":
                messagebox.showerror(title="Error",message="Kindly Enter Uername")
            if f_name == "":
                messagebox.showerror(title="Error",message="Kindly Enter First Name")
            if l_name == "":
                messagebox.showerror(title="Error",message="Kindly Enter Last Name")
            if p_password == "":
                messagebox.showerror(title="Error",message="Kindly Enter Password")
            if len(p_password) < 8:
                messagebox.showerror(title="Password Error",message="Your password is not strong its should be great than or equal to 8 Charactes")
            if p_phone == "":
                messagebox.showerror(title="Error",message="Kindly Enter Phone Number")
            if a_address == "":
                messagebox.showerror(title="Error",message="Kindly Enter Address")
            if e_mail == "":
                messagebox.showerror(title="Error",message="Kindly Enter Email")

            if u_name != "" and f_name != "" and l_name != "" and p_password != "" and len(p_password) >=8 and p_phone != "" and a_address != ""\
                and e_mail != "":
                messagebox.showinfo(title='Create account info', message="Account Created")
                f = open('cs_19053.txt', "a")
                if f is None:
                    return
                f.write(str([self.user.get(), self.password.get(), self.fname.get(), self.lname.get(),
                             self.phone.get(), self.address.get(), self.email.get()])+"\n")
                f.close()
                ans1 = messagebox.askquestion(title='Buy', message="You want to login ?")
                if ans1 =='yes':
                    self.root0.destroy()
                    obj2=User()
                elif ans1 == "no":
                    self.root0.destroy()


        def bck():
            self.root0.destroy()
            Object=User()

        #============================== Buttons =============================================================#

        b1 = Button(self.AB5, text='Submit', font=("arial", 12, "bold"), relief=RAISED, bg=self.bg_color, fg="Cornsilk",
                    command=check).grid(row=8, column=1, sticky=W)
        b2 = Button(self.AB5, text='Back', font=("arial", 12, "bold"), relief=RAISED, bg=self.bg_color, fg="Cornsilk",
                    command=bck).grid(row=8, column=2, sticky=E)



class Product:
    '''This class shows the products to user and also generate Bill '''
    def __init__(self,name="none" ):
        self.name=name
        self.product_main()

    #================================= Window for Products ====================================================#

    def product_main(self):
        root1=Tk()
        self.root1=root1
        self.root1.title("PRODUCTS")
        self.root1.config(background="powder blue")
        self.root1.maxsize(630,800)
        self.bg_color="#074463"
        self.Product_interface()
        self.root1.mainloop()

    def Product_interface(self):
        #======================================= Frames ==================================================================#

        self.ABC=Frame(self.root1,bg=self.bg_color,bd=20,relief=RIDGE).grid()
        self.ABC1=Frame(self.ABC,bd=14,width=630,height=100,relief=RIDGE,bg=self.bg_color).grid(row=0,column=0,columnspan=4)
        self.ABC2=Frame(self.ABC,bd=14,padx=10,bg=self.bg_color,relief=RIDGE).grid(row=1,column=0)

        #======================================= Variables ===============================================================#


        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()


        #======================================= Product Labels & Entries ==========================================#

        title_lbl=Label(self.ABC1,text="Products",font=("Arial",20,"bold"),justify=CENTER,pady=9,bd=5,
                            bg=self.bg_color,fg="Cornsilk").grid(row=0,column=1)

        amazon_lbl_1_a=Label(self.ABC2,text="Amazon Echo",font=("arial",12,"bold"),
                                        bg=self.bg_color,fg="Cornsilk").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        amazon_lbl_1_b=Label(self.ABC2,text="Rs.2100",font=("arial",12,"bold"),bg=self.bg_color,
                                 fg="Cornsilk").grid(row=1,column=1,padx=10,pady=10,sticky="w")
        bb9 = Label(self.ABC2,bg="powder blue").grid(row=1, column=2)
        amazon_txt1=Entry(self.ABC2,width=10,textvariable=self.var1,font=("arial",12,"bold"),
                                   bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)

        amazon_lbl_2_a=Label(self.ABC2,text="Doorbell Cam",font=("arial",12,"bold"),bg=self.bg_color,
                                 fg="Cornsilk").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        amazon_lbl_2_b=Label(self.ABC2,text="Rs.2150",font=("arial",12,"bold"),bg=self.bg_color,
                                 fg="Cornsilk").grid(row=2,column=1,padx=10,pady=10,sticky="w")
        bb10 = Label(self.ABC2, bg="powder blue").grid(row=2, column=2)
        amazon_txt2=Entry(self.ABC2,width=10,font=("arial",12,"bold"),textvariable=self.var2,
                                   bd=5,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=10)

        amazon_lbl_3_a=Label(self.ABC2,text="Cinder",font=("arial",12,"bold"),bg=self.bg_color,
                                 fg="Cornsilk").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        amazon_lbl_3_b=Label(self.ABC2,text="Rs.3100",font=("arial",12,"bold"),bg=self.bg_color,
                                 fg="Cornsilk").grid(row=3,column=1,padx=10,pady=10,sticky="w")
        bb11 = Label(self.ABC2, bg="powder blue").grid(row=3, column=2)
        amazon_txt3=Entry(self.ABC2,width=10,font=("arial",12,"bold"),textvariable=self.var3,
                                   bd=5,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=10)

        amazon_lbl_4_a=Label(self.ABC2,text="House Products",font=("arial",12,"bold"),
                                 bg=self.bg_color,fg="Cornsilk").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        amazon_lbl_4_b=Label(self.ABC2,text="Rs.2000",font=("arial",12,"bold"),
                                 bg=self.bg_color,fg="Cornsilk").grid(row=4,column=1,padx=10,pady=10,sticky="w")
        bb12 = Label(self.ABC2, bg="powder blue").grid(row=4, column=2)
        amazon_txt4=Entry(self.ABC2,width=10,font=("arial",12,"bold"),textvariable=self.var4,bd=5,
                                   relief=SUNKEN).grid(row=4,column=3,padx=10,pady=10)

        amazon_lbl_5_a = Label(self.ABC2, text="Oven", font=("arial", 12, "bold"),bg=self.bg_color,
                                fg="Cornsilk").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        amazon_lbl_5_b = Label(self.ABC2, text="Rs.11000", font=("arial", 12, "bold"), bg=self.bg_color,
                                fg="Cornsilk").grid(row=5, column=1, padx=10, pady=10, sticky="w")
        bb13 = Label(self.ABC2, bg="powder blue").grid(row=5, column=2)
        amazon_txt5 = Entry(self.ABC2, width=10, font=("arial", 12, "bold"),textvariable=self.var5,
                                     bd=5, relief=SUNKEN).grid(row=5, column=3,padx=10, pady=10)

        amazon_lbl_6_a = Label(self.ABC2, text="Piper", font=("arial", 12, "bold"), bg=self.bg_color,
                                fg="Cornsilk").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        amazon_lbl_6_b = Label(self.ABC2, text="Rs.12000", font=("arial", 12, "bold"), bg=self.bg_color,
                                fg="Cornsilk").grid(row=6, column=1, padx=10, pady=10, sticky="w")
        bb14 = Label(self.ABC2, bg="powder blue").grid(row=6, column=2)
        amazon_txt6 = Entry(self.ABC2, width=10, font=("arial", 12, "bold"),textvariable=self.var6,
                                     bd=5, relief=SUNKEN).grid(row=6, column=3,padx=10, pady=10)

        amazon_lbl_7_a = Label(self.ABC2, text="Roost", font=("arial", 12, "bold"), bg=self.bg_color,
                                fg="Cornsilk").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        amazon_lbl_7_b = Label(self.ABC2, text="Rs.9000", font=("arial", 12, "bold"), bg=self.bg_color,
                                fg="Cornsilk").grid(row=7, column=1, padx=10, pady=10, sticky="w")
        bb15 = Label(self.ABC2, bg="powder blue").grid(row=7, column=2)
        amazon_txt7 = Entry(self.ABC2, width=10, font=("arial", 12, "bold"),textvariable=self.var7,
                                     bd=5, relief=SUNKEN).grid(row=7, column=3,padx=10, pady=10)

        amazon_lbl_8_a = Label(self.ABC2, text="Samsung SmartThings", font=("arial", 12, "bold"), bg=self.bg_color,
                                fg="Cornsilk").grid(row=8, column=0, padx=10, pady=10, sticky="w")
        amazon_lb_8_b = Label(self.ABC2, text="Rs.15000", font=("arial", 12, "bold"), bg=self.bg_color,
                                fg="Cornsilk").grid(row=8, column=1, padx=10, pady=10, sticky="w")
        bb16 = Label(self.ABC2, bg="powder blue").grid(row=8, column=2)
        amazon_txt8 = Entry(self.ABC2, width=10, font=("arial", 12, "bold"),textvariable=self.var8, bd=5,
                                     relief=SUNKEN).grid(row=8, column=3,padx=10, pady=10)

        amazon_lbl_9_a = Label(self.ABC2, text="ATrack trackers", font=("arial", 12, "bold"), bg=self.bg_color,
                                fg="Cornsilk").grid(row=9, column=0, padx=10, pady=10, sticky="w")
        amazon_lbl_9_b = Label(self.ABC2, text="Rs.11000", font=("arial", 12, "bold"), bg=self.bg_color,
                                fg="Cornsilk").grid(row=9, column=1, padx=10, pady=10, sticky="w")
        bb17 = Label(self.ABC2, bg="powder blue").grid(row=9, column=2)
        amazon_txt9 = Entry(self.ABC2, width=10, font=("arial", 12, "bold"),textvariable=self.var9,
                                     bd=5, relief=SUNKEN).grid(row=9, column=3,padx=10, pady=10)

        amazon_lbl_10_a = Label(self.ABC2, text="GridConnect", font=("arial", 12, "bold"), bg=self.bg_color,
                                fg="Cornsilk").grid(row=10, column=0, padx=10, pady=10, sticky="w")
        amazon_lbl_10_b = Label(self.ABC2, text="Rs.10000", font=("arial", 12, "bold"), bg=self.bg_color,
                                 fg="Cornsilk").grid(row=10, column=1, padx=10, pady=10, sticky="w")
        bb18 = Label(self.ABC2, bg="powder blue").grid(row=10, column=2)
        amazon_txt10 = Entry(self.ABC2, width=10, font=("arial", 12, "bold"),textvariable=self.var10,
                                      bd=5, relief=SUNKEN).grid(row=10, column=3,padx=10, pady=10)



        self.buttons()

    #=========================================== Functions Call behind the Buttons ==================================#

    #============================== Bill Function ==============================#


    def i_bill(self):
        self.root1.destroy()
        root3 = Tk()
        self.root3 = root3
        self.root3.title("BILL")
        self.root3.config(background="powder blue")
        self.root3.maxsize(350, 383)
        self.root3.minsize(350, 383)
        shopping_list=[]

    #================ Product Prices =====================#

        try:
            self.product1 = self.var1.get() * 2100
        except:
            self.product1 = 0 * 2100
        try:
            self.product2 = self.var2.get() * 2150
        except:
            self.product2 = 0 * 2150
        try:
            self.product3 = self.var3.get() * 3100
        except:
            self.product3  = 0 * 3100
        try:
            self.product4 = self.var4.get() * 2000
        except:
            self.product4 = 0 * 2000
        try:
            self.product5 = self.var5.get() * 11000
        except:
            self.product5 = 0 * 11000
        try:
            self.product6 = self.var6.get() * 12000
        except:
            self.product6 = 0 * 12000
        try:
            self.product7 = self.var7.get() * 9000
        except:
            self.product7 = 0 * 9000
        try:
            self.product8 = self.var8.get() * 15000
        except:
            self.product8 = 0 * 15000
        try:
            self.product9 = self.var9.get() * 11000
        except:
            self.product9 = 0 * 11000
        try:
            self.product10 = self.var10.get() * 10000
        except:
            self.product10 = 0 * 10000

        self.total_bill = int(self.product1 +
                                self.product2 +
                                self.product3 +
                                self.product4 +
                                self.product5 +
                                self.product6 +
                                self.product7 +
                                self.product8 +
                                self.product9 +
                                self.product10
                                )


        self.billno = StringVar()
        x = random.randint(10000, 99999)
        self.billno.set(str(x))
        self.now=datetime.datetime.now()

        self.F1 = Frame(self.root3, bd=10, relief=GROOVE).place(x=0, y=0, width=350, height=380)
        bill_title = Label(self.F1, text="BILL RECEPIT", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)

        #=========================== Function call behind Buttons ========================#

        def back1():
            self.root3.destroy()
            self.product_main()

        def log_out():
            self.root3.destroy()
            obj=User()

        #========================== Buttons ==============================#

        btn_3 = Button(self.F1, text='Logout', font=("arial", 12, "bold"), relief=GROOVE, command=log_out).pack(side=BOTTOM,fill=X)
        btn_4=Button(self.F1, text='Back', font=("arial", 12, "bold"), relief=GROOVE,command=back1).pack(side=BOTTOM,fill=X)

        #==========================================#

        scrol_y = Scrollbar(self.F1, orient=VERTICAL)
        self.txtarea = Text(self.F1, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview())
        self.txtarea.pack()
        self.txtarea.insert(END, "\tWelcome Webcode Retail")
        self.txtarea.insert(END, f"\n Bill Number : {self.billno.get()} ")
        self.txtarea.insert(END, f"\n Customer Username : {self.name} ")
        z=[self.name,self.now.strftime("%d-%m-%y"),self.now.strftime("%H:%M:%S")]
        shopping_list.append(z)
        self.txtarea.insert(END, f"\n =======================================")
        self.txtarea.insert(END, f"\n Products\t\t\tQTY\tPrice ")
        self.txtarea.insert(END, f"\n =======================================")

    #====================== Checks =======================#

        self.total_QTY=0
        try:
            if self.var1.get()!=0:
                self.total_QTY+=self.var1.get()
                self.txtarea.insert(END, f"\n Amazon Echo\t\t\t{self.var1.get()}\t{self.product1}")
                a=['Amazon Echo',self.var1.get(),self.product1]
                shopping_list.append(a)
        except:
            pass
        try:
            if self.var2.get()!=0:
                self.total_QTY+=self.var2.get()
                self.txtarea.insert(END, f"\n Doorbell Cam\t\t\t{self.var2.get()}\t{self.product2}")
                b = ['Doorbell Cam', self.var2.get(), self.product2]
                shopping_list.append(b)
        except:
            pass
        try:
            if self.var3.get()!=0:
                self.total_QTY+=self.var3.get()
                self.txtarea.insert(END, f"\n Cinder\t\t\t{self.var3.get()}\t{self.product3}")
                c = ['Cinder', self.var3.get(), self.product3]
                shopping_list.append(c)
        except:
            pass
        try:
            if self.var4.get()!=0:
                self.total_QTY+=self.var4.get()
                self.txtarea.insert(END, f"\n Home Products\t\t\t{self.var4.get()}\t{self.product4}")
                d = ['Home Products', self.var4.get(), self.product4]
                shopping_list.append(d)
        except:
            pass
        try:
            if self.var5.get()!=0:
                self.total_QTY+=self.var5.get()
                self.txtarea.insert(END, f"\n Oven\t\t\t{self.var5.get()}\t{self.product5}")
                e = ['Oven', self.var5.get(), self.product5]
                shopping_list.append(e)
        except:
            pass
        try:
            if self.var6.get()!=0:
                self.total_QTY+=self.var6.get()
                self.txtarea.insert(END, f"\n Piper\t\t\t{self.var6.get()}\t{self.product6}")
                f = ['Piper', self.var6.get(), self.product6]
                shopping_list.append(f)
        except:
            pass
        try:
            if self.var7.get()!=0:
                self.total_QTY+=self.var7.get()
                self.txtarea.insert(END, f"\n Roost\t\t\t{self.var7.get()}\t{self.product7}")
                g = ['Roost', self.var7.get(), self.product7]
                shopping_list.append(g)
        except:
            pass
        try:
            if self.var8.get()!=0:
                self.total_QTY+=self.var8.get()
                self.txtarea.insert(END, f"\n SmartThings\t\t\t{self.var8.get()}\t{self.product8}")
                h = ['Smarthings', self.var8.get(), self.product8]
                shopping_list.append(h)
        except:
            pass
        try:
            if self.var9.get() != 0:
                self.total_QTY+=self.var9.get()
                self.txtarea.insert(END, f"\n ATrack trackers\t\t\t{self.var9.get()}\t{self.product9}")
                i = ['ATrack trackers', self.var9.get(), self.product9]
                shopping_list.append(i)
        except:
            pass
        try:
            if self.var10.get() != 0:
                self.total_QTY+=self.var10.get()
                self.txtarea.insert(END, f"\n GridConnect\t\t\t{self.var10.get()}\t{self.product10}")
                j = ['GridConnect', self.var10.get(), self.product10]
                shopping_list.append(j)
        except:
            pass
        k=["Total",self.total_QTY,self.total_bill]
        shopping_list.append(k)

        f2 = open('history.txt', "a")
        if f2 is None:
            return
        f2.write(str(shopping_list) + ",")
        f2.close()

        self.txtarea.insert(END, f"\n =======================================")

        self.txtarea.insert(END, f"\n Total Bill\t\t\t\tRs.{self.total_bill}")
        self.txtarea.insert(END, f"\n =======================================")
        self.txtarea.insert(END, f"\n Checkout Date\t\t\tCheckout Time")
        self.txtarea.insert(END, "\n " +self.now.strftime("%d-%m-%y\t\t\t%H:%M:%S"))

    def bill_chk(self):
        try:
            if int(self.var1.get())>=0 and int(self.var2.get())>=0 and int(self.var3.get())>=0 and int(self.var4.get())>=0 and int(self.var5.get())>=0\
                and int(self.var6.get())>=0 and int(self.var7.get())>=0 and int(self.var8.get())>=0 and int(self.var9.get())>=0 and int(self.var10.get())>=0:
                obj=self.i_bill()
        except:
            messagebox.showerror(title="Error",message="Kindly enter integer values")

    #================== Exit Function ================#

    def i_exit(self):
        self.root1.destroy()
        obj=User()

    # ================== History Function ================#

    def history_btn(self):
        f2 = open('history.txt', "r")
        count = 0
        for i in f2:
            i = eval(i)
            for j in i:
                if self.name in j[0]:
                    count+=1
        f2.close()
        if count==0:
            messagebox.showinfo(title="History", message="Sorry you do not have any previous shopping history!!")
        if count>0:
            self.root1.destroy()
            ob1 = SHOPPING_HISTORY(self.name)

    #================================================= Buttons =======================================================#

    def buttons(self):

        self.ABC0=Frame(self.ABC,bd=14,width=630,height=100,relief=RIDGE,bg=self.bg_color).grid(row=12,column=0,columnspan=4)

        bill_btn=Button(self.ABC2,text="BILL",bg="powder blue",fg=self.bg_color,bd=5,pady=12,width=10,font=("arial", 12, "bold")
                        ,command=self.bill_chk).grid(row=12, column=0,padx=0, pady=10)

        exit_btn = Button(self.ABC2, text="Logout",bg="powder blue", fg=self.bg_color, bd=5, pady=12, width=10,
                           font=("arial", 12, "bold"),command=self.i_exit).grid(row=12, column=1,padx=0,pady=10)

        History_btn = Button(self.ABC2, text="HISTORY", bg="powder blue", fg=self.bg_color, bd=5, pady=12, width=10,
                          font=("arial", 12, "bold"), command=self.history_btn).grid(row=12, column=3, padx=0, pady=10)


#========================================== login Class ==============================================================#


class LOGIN(Product):
    '''If user have already an account then this class allows user to login without creating account'''

    def __init__(self):
        #=========================== Login Window ===========================#
        root2 = Tk()
        self.root2 = root2
        self.root2.title("Login")
        self.root2.config(background="powder blue")
        self.root2.minsize(350, 300)
        self.root2.maxsize(350, 300)
        self.bg_color = "#074463"



        self.username = StringVar()
        self.pswrd = StringVar()

        self.login()

    def login(self):

    #============================= Labels & Frames =====================================#

        self.AB6 = Frame(self.root2, bg=self.bg_color, bd=20, relief=RIDGE).grid()
        self.AB7 = Frame(self.AB6, bd=10, width=350, height=70, relief=RIDGE, bg=self.bg_color).grid(row=0, column=0,
                                                                                                     columnspan=4)
        self.AB8 = Frame(self.AB6, bd=14, padx=10, bg=self.bg_color, relief=RIDGE).grid(row=1, column=0)

        n3 = Label(self.AB7, text="Login", font=("Arial", 15, "bold"), justify=CENTER,
                   bg=self.bg_color, fg="Cornsilk", pady=4, bd=5).grid(row=0, column=1)

        bb7 = Label(self.AB8, bg="powder blue").grid(row=1, column=2)

        label1 = Label(self.AB8, text='Username', font=("arial", 12, "bold"), bg=self.bg_color, fg="Cornsilk") \
            .grid(row=2, column=0, padx=10, pady=10, sticky="w")

        bb8 = Label(self.AB8, bg="powder blue").grid(row=3, column=2)

        label2 = Label(self.AB8, text='Password', font=("arial", 12, "bold"), bg=self.bg_color, fg="Cornsilk") \
            .grid(row=4, column=0, padx=10, pady=10, sticky="w")

        t1 = Entry(self.AB8, width=15, font=("arial", 12, "bold"), textvariable=self.username, bd=5, relief=SUNKEN) \
            .grid(row=2, column=2, padx=10, pady=10)

        t2 = Entry(self.AB8, width=15, font=("arial", 12, "bold"), textvariable=self.pswrd, bd=5, relief=SUNKEN,
                   show="*") \
            .grid(row=4, column=2, padx=10, pady=10)

        self.buttons2()

    # ========================================== Buttons Method ==========================================================#

    def buttons2(self):
        def login():
            count=0
            name=self.username.get()
            password=self.pswrd.get()
            if name == "":
                messagebox.showinfo(title='Error', message='Kindly enter Username')
            if password == "":
                messagebox.showinfo(title='Error', message='Kindly enter Password')
            if name!= "" and password!="":
                f1 = open('cs_19053.txt', "r")
                count=0
                for item in f1:
                    item=eval(item.strip())
                    if self.username.get() in item and self.pswrd.get() in item:
                        messagebox.showinfo(title='Login status', message='You have Logged in.')
                        count+=1
                if count == 1:
                    i_login = messagebox.askquestion("Products", "You want to buy?")
                    if i_login == "yes":
                        self.root2.destroy()
                        Ob = Product(name)
                else:
                    messagebox.showinfo(title='Login Error', message='Invalid Username or Password!!')
                    q=messagebox.askquestion(title='Account', message='You want to creat account?')
                    if q == "yes":
                        self.root2.destroy()
                        Obj=User()
                f1.close()
        def ii_exit():
            self.root2.destroy()

        #====================================== Buttons =========================================#

        bb8 = Label(self.AB8, bg="powder blue").grid(row=5, column=2)

        b1 = Button(self.AB8, text='Login', width=7, font=("arial", 12, "bold"), relief=RAISED, bg=self.bg_color,
                        fg="Cornsilk", command=login).grid(row=6, column=0, sticky=E)

        b2 = Button(self.AB8, text='Cancel', width=7, font=("arial", 12, "bold"), relief=RAISED, bg=self.bg_color
                        , fg="Cornsilk", command=ii_exit).grid(row=6, column=2, sticky=W)


#========================================== Abstract Class ==========================================================#

class Abstract(ABC):
    '''This is an Abstract class for user'''
    def __init__(self):
        root = Tk()
        self.root = root
        self.root.title("Online Shopping Cart")
        self.root.config(background="powder blue")
        self.root.minsize(350, 350)
        self.root.maxsize(350, 350)
        self.bg_color = "#074463"
        self.user_main()
        root.mainloop()

    #=================== Abstract Method ==================#

    @abstractmethod
    def user_main(self):
        pass


#========================================== User Class ==========================================================#

class User(LOGIN,Abstract):
    '''This class allows user to create window or login also exit from Online Shopping Cart'''
    def __init__(self):
        Abstract.__init__(self)

    #===================== Implementation for Abstract method for Abstract Class ==========================#

    def user_main(self):
        self.Fa = Frame(self.root, bg=self.bg_color, bd=20, relief=RIDGE).grid()
        self.Fa1 = Frame(self.Fa, bd=14, width=350, height=80, relief=RIDGE, bg=self.bg_color).grid(row=0, column=0,
                                                                                                           columnspan=4)
        self.Fa2 = Frame(self.Fa, bd=14, padx=10, bg=self.bg_color, relief=RIDGE).grid(row=1, column=0)

        n1 = Label(self.Fa1, text="Online Shopping Cart",font=("Arial",15,"bold"),justify=CENTER,pady=9,bd=5,
                       bg=self.bg_color,fg="Cornsilk").grid(row=0,column=2)

        #=============================== Function calls behind Buttons ============================#

        def i_create():
            self.root.destroy()
            obj1=CREATE_ACCOUNT()
        def i_log():
            self.root.destroy()
            obj2=LOGIN()
        def ii_exit():
            self.root.destroy()

        #=============================== Labels & Buttons ===================================#

        bb1 = Label(self.Fa2,bg="powder blue").grid(row=1, column=2)
        bb2 = Label(self.Fa2, bg="powder blue").grid(row=2, column=2)
        bb3 = Button(self.Fa2, text='Create Account',font=("Arial",15,"bold"),bg=self.bg_color,fg="Cornsilk",relief=RAISED
                             , command=i_create).grid(row=3, column=2)
        bb4 = Label(self.Fa2, bg="powder blue").grid(row=4, column=2)
        bb5 = Label(self.Fa2, bg="powder blue").grid(row=5, column=2)
        bb6 = Button(self.Fa2, text='Login',font=("Arial",15,"bold"),bg=self.bg_color,fg="Cornsilk",relief=RAISED
                             , command=i_log).grid(row=6, column=2)
        bb7 = Label(self.Fa2, bg="powder blue").grid(row=7, column=2)
        bb8 = Label(self.Fa2, bg="powder blue").grid(row=8, column=2)
        bb9 = Button(self.Fa2, text='Exit', font=("Arial", 15, "bold"), bg=self.bg_color, fg="Cornsilk", relief=RAISED
                     , command=ii_exit).grid(row=9, column=2)

#=======================================Shopping History Class========================================================#

class SHOPPING_HISTORY(User):
    '''This class shows the shopping history if the user has any previous shopping history'''

    def __init__(self,name):

        #================= Shopping History Window ================#
        self.name=name
        root4 = Tk()
        self.root4 = root4
        self.root4.title("Shopping History")
        self.root4.config(background="powder blue")
        self.root4.maxsize(350, 383)
        self.root4.minsize(350, 383)
        self.frame()

    def frame(self):

        #============================= Frames ===============================#

        self.F2 = Frame(self.root4, bd=10, relief=GROOVE).place(x=0, y=0, width=350, height=380)
        bill_title1 = Label(self.F2, text="SHOPPING HISTORY", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)

        #===================== Function calls behind Buttons ============================#

        def back():
            self.root4.destroy()
            ob1 = Product()

        def logout():
            self.root4.destroy()
            ob1=User()

        #============================= Buttons ==========================#

        btn_2 = Button(self.F2, text='Logout', font=("arial", 12, "bold"), relief=GROOVE, command=logout).pack(side=BOTTOM,
                                                                                                           fill=X)
        btn_1 = Button(self.F2, text='Back', font=("arial", 12, "bold"), relief=GROOVE, command=back).pack(side=BOTTOM,
                                                                                                           fill=X)
        scrol_y1 = Scrollbar(self.F2, orient=VERTICAL)
        self.txtarea = Text(self.F2, yscrollcommand=scrol_y1.set)
        scrol_y1.pack(side=RIGHT, fill=Y)
        scrol_y1.config(command=self.txtarea.yview())
        self.txtarea.pack()

        #============================== Read Data from File =================================#

        f3 = open('history.txt', "r")
        for i in f3:
            i = eval(i)
            count=0
            for j in i:
                if self.name in j[0]:
                    z=len(j)
                    self.txtarea.insert(END, f"\n Username\t\tDate\t\tTime ")
                    self.txtarea.insert(END, f"\n {j[0][0]}\t\t{j[0][1]}\t\t{j[0][2]} ")
                    self.txtarea.insert(END, f"\n =======================================")
                    self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice ")
                    self.txtarea.insert(END, f"\n =======================================")
                    for i in range(1,z-1):
                        self.txtarea.insert(END, f"\n {j[i][0]}\t\t{j[i][1]}\t\t{j[i][2]} ")

                    self.txtarea.insert(END, f"\n =======================================")
                    self.txtarea.insert(END, f"\n {j[z-1][0]}\t\t{j[z-1][1]}\t\tRs.{j[z-1][2]} ")
                    self.txtarea.insert(END, f"\n =======================================")
                    self.txtarea.insert(END, f"\n")
        f3.close()

#======================================= Main Call ===========================================================#

o1=User()