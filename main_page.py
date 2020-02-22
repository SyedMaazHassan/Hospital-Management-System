from tkinter import*
import login_admin

class main_window:
    def __init__(self, main):
        self.var = ''
        self.main = main
        self.main.configure(background="#FFFFFF")
        self.main.geometry("1200x800")
        self.main.title("Hospital Management System")

    def all_buttons(self):
        self.img1 = PhotoImage(file="all_imgs/newimg1.png")

        self.label1 = Label(self.main, image=self.img1, bd="0")
        self.label1.pack()

        self.frame1 = Frame(self.main, bg="#FFFFFF", height="300", width="1200")
        self.frame1.pack(pady=60)

        self.onepic = PhotoImage(file="all_imgs/line.png")
        self.label2 = Label(self.frame1, image=self.onepic)
        self.label2.pack(side=LEFT)

        #1st button
        self.btn01 = PhotoImage(file='all_imgs/btn03.png')

        self.btn1 = Button(self.frame1, cursor='hand2', image=self.btn01, relief='flat', height="220", width="188", command=lambda: self.all_pic_run('a'))
        self.btn1.pack(side=LEFT, padx=30)
    
        #2nd button
        self.btn02 = PhotoImage(file="all_imgs/btn002.png")
           
        self.btn2 = Button(self.frame1, cursor='hand2', image=self.btn02, relief='flat', height="220", width="188", command=lambda: self.all_pic_run('r'))
        self.btn2.pack(side=LEFT, padx=30)

        #3rd button
        self.btn03 = PhotoImage(file="all_imgs/btn01.png")        
                           
        self.btn3 = Button(self.frame1, cursor='hand2', image=self.btn03, relief='flat', height="220", width="188", command=lambda: self.all_pic_run('d'))
        self.btn3.pack(side=LEFT, padx=30)

        #4th button
        self.btn04 = PhotoImage(file="all_imgs/btn04.png")        
        self.btn4 = Button(self.frame1, cursor='hand2', image=self.btn04, relief='flat', height="220", width="188", command=lambda: self.all_pic_run('p'))
        self.btn4.pack(side=LEFT, padx=30)
    
    def doc(self):
        var = 'Doctor'

    def Phar(self):
        var = 'Pharmacist'

    def rep(self):
        var = 'Receptionist'

        """
        elif self.var=='Doctor':
            pass
        elif self.var=='Receptionist':
            pass
        elif self.var=='Pharmacist':
            pass
        """

    def all_pic_run(self, P):
        if P=='r':
            self.var = 'Receptionist'
        elif P=='d':
            self.var = 'Doctor'
        elif P=='p':
            self.var = 'Pharmacist'
        else:
            self.var = 'Admin'
        
        print(self.var)
        self.login(P, self.main)


    def login(self,b, main):
        self.frame1.destroy()
        self.label1.destroy()
        print('done')
        self.RUN(b)
        self.mmain.entities()
        self.main.mainloop()

     #aggregation           
    def RUN(self, k):
            if k=='a':
                self.mmain = login_admin.login(self.main,'all_imgs/admin.png')
            elif k=='p':
                self.mmain = login_admin.login(self.main, 'all_imgs/pharm.png')
            elif k=='d':
                self.mmain = login_admin.login(self.main, 'all_imgs/doctor.png')
            elif k=='r':
                self.mmain = login_admin.login(self.main, 'all_imgs/receptt.png')
        
        
if __name__=='__main__':        
    wd = Tk()
    #login_window.new(wd) 
    main = main_window(wd)
    main.all_buttons()
    wd.mainloop()





"""
def login(self, ID, passwo):
        #checking
        #if self.var=='Admin':
    main=main_window(wd)
    main.frame1.destroy()
    main.label1.destroy()
    if main.var=='Admin':
        import admin_window
        main = admin_window.form(wd)
        main.active()
        main.active2()
        wd.mainloop()
"""
