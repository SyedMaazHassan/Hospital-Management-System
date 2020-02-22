from tkinter import*
import admin_window
import main_page
import recept_window
import doctor_window
import sqlite3
import tkinter.messagebox as tkm

class login:
    def __init__(self, main, picc):
        self.main = main
        self.header_pic = picc
        self.f = ('verdana', 15)
        self.main.geometry("1200x800")
        self.main.title('Login')
        self.main.configure(bg='#FFFFFF')

    def entities(self):
        self.header_img = PhotoImage(file='all_imgs/login_header.png')

        self.whole = Label(self.main, image=self.header_img)
        self.whole.pack(fill='both')

        self.parent_label = Label(self.whole, bg='white', height=400)
        self.parent_label.pack(pady=133)

        self.frame = Frame(self.parent_label, height=15,width=5, bg='white')
        self.frame.pack(ipadx=10, padx=4, pady=4)

        self.pic = PhotoImage(file=self.header_pic)
        self.picframe = Label(self.frame, height=164, image=self.pic, width=141, bg='#000000')
        self.picframe.pack(pady=(30,10))

        self.user = Label(self.frame, text='Username', font=self.f, bg='white', fg='#0049ad')
        self.user.pack(fill=X,pady=(10,0), padx=(0,170))
        
        self.Entry1 = Entry(self.frame, font=self.f, width=21, fg='#383737')
        self.Entry1.pack(padx=5, pady=(10,10))

        self.user = Label(self.frame, text='Password', font=self.f, bg='white', fg='#0049ad')
        self.user.pack(fill=X, padx=(0,175))
        
        self.Entry2 = Entry(self.frame, font=self.f, width=21, fg='#383737', show='•')
        self.Entry2.pack(padx=5, pady=(10,10))

        self.LogBtn = Button(self.frame, width=22, height=1, text='Login', font=('verdana',14), fg='white', bg='#0049ad', command=self.get_data)
        self.LogBtn.pack(pady=(20,10))
        self.LogBtn2 = Button(self.frame, width=22, height=1, text='Back', font=('verdana',14), fg='white', bg='#0049ad', command=self.back)
        self.LogBtn2.pack(pady=(10,20))
        

        

    def back(self):
        self.whole.destroy() 
        self.mmain = main_page.main_window(self.main)
        self.mmain.all_buttons()
        self.main.mainloop()

    def get_data(self):
        
        
        self.user_n = self.Entry1.get()
        self.passwo = self.Entry2.get()
        """
        self.txtfdile = open('login_admin.txt','r')
        self.L = self.txtfile.readline().split()

        if self.user_n==self.L[0] and self.passwo==self.L[1]:
            admin_window.form()
        else:
            print(False)
        """
        self.db = sqlite3.connect('database/employe.db')
        if self.header_pic=='all_imgs/admin.png':
            if self.user_n=='UserAdmin' and self.passwo==self.user_n[::-1]:
                self.admin_window()
            else:
                tkm.showinfo(message='Invalid username or password')
                self.Entry1.delete(0, 'end')
                self.Entry2.delete(0, 'end')

        elif self.header_pic=='all_imgs/receptt.png':
            for i in self.db.execute("SELECT ID FROM EMPLOYEES_DATA WHERE DESIGNATION='Receptionist'"):
                if self.user_n==i[0] and self.passwo==i[0][::-1]:
                    self.recept_window(self.user_n)
                else:
                    self.messages=tkm.showinfo(message='Invalid username or password')
                    self.Entry1.delete(0, 'end')
                    self.Entry2.delete(0, 'end')

        elif self.header_pic=='all_imgs/doctor.png':
            for i in self.db.execute("SELECT ID FROM EMPLOYEES_DATA WHERE DESIGNATION='Doctor'"):
                if self.user_n==i[0] and self.passwo==i[0][::-1]:
                    self.doctor_window(self.user_n)
                else:
                    tkm.showinfo(message='Invalid username or password')
                    self.Entry1.delete(0, 'end')
                    self.Entry2.delete(0, 'end')

        elif self.header_pic=='all_imgs/pharm.png':
            for i in self.db.execute("SELECT ID FROM EMPLOYEES_DATA WHERE DESIGNATION='Pharmacist'"):
                if self.user_n==i[0] and self.passwo==i[0][::-1]:
                    self.pharma_window(self.user_n)
                else:
                    tkm.showinfo(message='Invalid username or password')
                    self.Entry1.delete(0, 'end')
                    self.Entry2.delete(0, 'end')

            
    def admin_window(self):
        self.whole.destroy()
        self.mmain=admin_window.form(self.main)
        self.mmain.left_column()
        self.mmain.right_column()
        self.main.mainloop()

    def recept_window(self, id_go):
        self.whole.destroy()
        self.mmain=recept_window.patient_form(self.main, id_go)
        self.mmain.left_column()
        self.mmain.right_column()
        self.main.mainloop()

    def doctor_window(self, id_go):
        self.whole.destroy()
        self.mmain=doctor_window.doctor_form(self.main, id_go)
        self.mmain.left_column()
        self.mmain.right_column()
        self.main.mainloop()


    def pharma_window(self, id_go):
        self.whole.destroy()
        self.mmain=pharm_window.patient_bill(self.main, id_go)
        self.mmain.left_column()
        self.mmain.right_column()
        self.main.mainloop()
    
        
if __name__=='__main__':
    a=Tk()
    mmain=login(a, 'all_imgs/admin.png')
    mmain.entities()
    a.mainloop()
