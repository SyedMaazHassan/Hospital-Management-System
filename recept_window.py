from tkinter import*
from tkinter import ttk
import tkinter.messagebox as tkm
import main_page
import sqlite3
import datetime

class patient_form:
      def __init__(self, main, info):
            self.upload_photo_wali_place = 'img-'
            [self.f_n, self.l_n, self.ct_n, self.c_n, self.add, self.ema, self.cell, self.cnic_n, self.c_t_d, self.token_no, self.unique_id, self.appointment_doc, self.d_o_b] = [None,None,None,None,None,None,None,None,None,None,None,None,None]
            self.currentDT = datetime.datetime.now()
            self.info = info
            self.db = sqlite3.connect('database/employe.db')
            for i in self.db.execute("SELECT * FROM EMPLOYEES_DATA WHERE ID='{}'".format(self.info)):
                  self.upload_photo_wali_place+=i[8]+'.png'
            print(self.info)
            self.date = self.currentDT.strftime("%a, %b %d, %Y")
            self.time = self.currentDT.strftime("%I:%M:%S %p")
            self.c_t_d = self.date+'  -  '+self.time
            self.main = main
            self.main.configure(background="#FFFFFF")
            self.main.geometry("1200x800")
            self.main.title("Hospital Management System")
            #self.btn = Button(self.main, text='wssow', height='4', width='4', command=activate)
            #self.btn.pack(ipadx=10)
            self.header=Frame(self.main, height=70, width=700, bg='#000000')
            self.header.pack(fill=X, ipady=(8))

            self.logo=PhotoImage(file='all_imgs/logo.png')
            self.logo_label=Label(self.header, bg='#000000',image=self.logo)
            self.logo_label.pack(side=LEFT, padx=(30,10))

            self.name = Label(self.header, text='RECEPTIONIST', font=('',30),bg='#000000', fg='white')
            self.name.pack(side=LEFT)

            self.photo = PhotoImage(file='all_imgs/search.png')                           
            self.search_btn = Button(self.header, image=self.photo, height=33, width=60, bg='#0048ad', command=self.search_record)
            self.search_btn.pack(side=RIGHT, padx=(10,38))

            self.search = Entry(self.header,font=('verdana', 16), fg='#383737', width=17)
            self.search.pack(side=RIGHT, ipady=4)
            self.search.insert(0, ' Search by ID')
            self.search.bind("<FocusIn>", lambda args: self.search.delete(' 0', 'end'))

      def left_column(self):
            self.y = 7
            self.parent_frame = Frame(self.main, height='550px', width='425px', bg='white')
            self.parent_frame.pack(pady='0', padx=(30,20), side=LEFT)
      
            #0th line
            self.line_frame0 = Frame(self.parent_frame, bg='#FFFFFF', height=140)
            self.line_frame0.pack(fill=X, pady=self.y)
            try:
                  self.upload = PhotoImage(file='images/'+self.upload_photo_wali_place)
                  self.picframe = Label(self.line_frame0,relief='flat',height=190, image=self.upload, width=141, bg='#FFFFFF')
                  self.picframe.pack(pady=(0,0), side=LEFT)
            except:
                  self.upload = PhotoImage(file='all_imgs/uploadd.png')
                  self.picframe = Label(self.line_frame0,relief='flat',height=164, image=self.upload, width=141, bg='#FFFFFF')
                  self.picframe.pack(pady=(0,0), side=LEFT)
                  
            for i in self.db.execute("SELECT * FROM EMPLOYEES_DATA WHERE ID='{}'".format(self.info)):
                  self.instructions=Label(self.line_frame0, anchor='w', bg='#FFFFFF', text='   '+i[1]+' '+i[2]+'\t(Age : 19)'+'\n\n   '+i[6]+'\n\n   '+i[3]+' '+i[4]+'\n\n   '+i[7]+' : (Timing : '+i[11]+')', justify=LEFT, font=('verdana',12))
                  self.instructions.pack(side=LEFT)
                  print(self.upload_photo_wali_place)
            """
            self.linee=Frame(self.line_frame0, bg='gray', height='1', width='390')
            self.linee.pack(side=BOTTOM, pady=(0,0))
            """
            
            #1st line
            self.line_frame1 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame1.pack(fill=X, pady=(self.y*2,0))

            self.first_name = Label(self.line_frame1, text='First Name', font=('verdana', 12), bg='#FFFFFF',fg='#0049ad' )
            self.first_name.pack(side=LEFT, pady=self.y,)

            self.last_name = Label(self.line_frame1, text='Last Name', font=('verdana', 12),bg='#FFFFFF',fg='#0049ad')
            self.last_name.pack(pady=self.y, side=LEFT,  padx=(188,0))

            #2nd line
            self.line_frame2 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame2.pack()
            
            self.first_name_entry = Entry(self.line_frame2, font=('verdana', 15), fg='#383737')
            self.first_name_entry.pack(side=LEFT, padx=(3,7), pady=self.y)

            self.last_name_entry = Entry(self.line_frame2, font=('verdana', 15), fg='#383737')
            self.last_name_entry.pack(pady=self.y, side=LEFT, padx=(10,0))

            #3rd line
            self.line_frame3 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame3.pack(fill=X)

            self.first_name = Label(self.line_frame3, text='City (current)', font=('verdana', 12),bg='#FFFFFF',fg='#0049ad')
            self.first_name.pack(side=LEFT, pady=self.y,)

            self.last_name = Label(self.line_frame3, text='Country', font=('verdana', 12),bg='#FFFFFF',fg='#0049ad')
            self.last_name.pack(pady=self.y, side=LEFT,  padx=(168,0))


            #4th line
            self.line_frame4 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame4.pack()
            
            self.city_entry = Entry(self.line_frame4, font=('verdana', 15), fg='#383737')
            self.city_entry.pack(side=LEFT, padx=(3,7),pady=self.y)

            self.country_entry = Entry(self.line_frame4, font=('verdana', 15), fg='#383737')
            self.country_entry.pack(pady=self.y, side=LEFT, padx=(10,0))

            #5th line
            self.line_frame5 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame5.pack(fill=X)

            self.address = Label(self.line_frame5, text='Complete Address (current)',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.address.pack(pady=self.y, padx=(0,315))

            self.address_entry = Entry(self.line_frame5, font=('verdana', 15), fg='#383737')
            self.address_entry.pack(fill=X, padx=(3,0),pady=self.y)
            
            #11th line
            self.line_frame11 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame11.pack(fill=X)

            self.cnic = Label(self.line_frame11, text='Email Address',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.cnic.pack(pady=self.y, side=LEFT, )

            #12thline
            self.line_frame12 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame12.pack(fill=X)
            
            self.email_entry = Entry(self.line_frame12, font=('verdana', 15), fg='#383737')
            self.email_entry.pack(fill=X, padx=(3,0),pady=self.y)


            #7th line
            self.line_frame7 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame7.pack(fill=X,pady=self.y)

            self.phone = Label(self.line_frame7, text='Cell Number',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.phone.pack(side=LEFT, pady=self.y,)

            self.email = Label(self.line_frame7, text='CNIC Number',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.email.pack(pady=self.y, side=LEFT,  padx=(175,0))

            #8th line
            self.line_frame8 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame8.pack()
            
            self.phone_entry = Entry(self.line_frame8, font=('verdana', 15), fg='#383737')
            self.phone_entry.pack(side=LEFT,pady=self.y, padx=(3,7))

            self.CNIC_entry = Entry(self.line_frame8, font=('verdana', 15), fg='#383737')
            self.CNIC_entry.pack(pady=self.y, side=LEFT, padx=(10,0))

  
            #13thline
            self.line_frame13 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame13.pack(fill=X,pady=self.y)
            self.check = Checkbutton(self.line_frame13, font=('verdana',10), bg='#FFFFFF')
            self.check.pack(side=LEFT)
            self.address_c = Label(self.line_frame13, text='I am ensure that this information is completely authentic.',bg='#FFFFFF', font=('verdana', 12),fg='#000000')
            self.address_c.pack(pady=self.y+4, padx=(0,0))

      def right_column(self):

            self.y = 7
            self.parent_frame2 = Frame(self.main, height='550px', width='425px', bg='#FFFFFF')
            self.parent_frame2.pack(padx='30', side=LEFT)

            #1st line
            self.line_frame1 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame1.pack(fill=X)

            self.first_name = Label(self.line_frame1, text='Date & Time', font=('verdana', 12), bg='#FFFFFF',fg='#0049ad' )
            self.first_name.pack(side=LEFT, pady=(30,10))


            #2nd line
            self.line_frame2 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame2.pack(fill=X)

            self.dt = Label(self.line_frame2, text=self.date+'  |  '+self.time, width=32, bg='#f4f4f4', height='2', font=('verdana', 12),fg='#000000')
            self.dt.pack(side=LEFT,pady=self.y, padx=(0,0))


            #1th line
            self.line_frame9 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame9.pack(fill=X,pady=self.y)

            self.Desig = Label(self.line_frame9, text='Appointment',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.Desig.pack(side=LEFT, pady=self.y,)

            self.email = Label(self.line_frame9, text='Date of Birth',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.email.pack(pady=self.y, side=LEFT,  padx=(168,0))

            #10th line
            self.line_frame10 = Frame(self.parent_frame2, bg='white')
            self.line_frame10.pack(fill=X)

            self.doctor_file = open('text/doctor_name.txt', 'r')
            self.LIST = self.doctor_file.readline().split('=')
            """
            for i in self.doctor_file:
                  if len(i)>0:
                        self.LIST.append(i)
            """
            self.appo = ttk.Combobox(self.line_frame10, values=self.LIST, font=('verdana',12))
            self.appo.current(0)
            self.appo.pack(side=LEFT,pady=self.y, padx=(4,17))


            self.d = ttk.Combobox(self.line_frame10, values=['Day']+list(range(1,32)), font=('verdana',12), width=5)
            self.d.current(0)
            self.d.pack(side=LEFT, pady=self.y, padx=(40,10))

            
            self.m = ttk.Combobox(self.line_frame10, values=['Month']+('Jan Feb Mar Apr May Jun July Aug Sep Oct Nov Dec'.split()), font=('verdana',12), width=5)
            self.m.current(0)
            self.m.pack(side=LEFT, pady=self.y, padx=(10,10))
            
            
            self.ye = ttk.Combobox(self.line_frame10, values=['Year']+list(range(1900,2020))[::-1], font=('verdana',12), width=7)
            self.ye.current(0)
            self.ye.pack(side=LEFT, pady=self.y, padx=(10,3))


            #2th line
            self.line_frame9 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame9.pack(fill=X, pady=5)

            self.id = Label(self.line_frame9, text='Click to generate patient ID',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.id.pack(pady=self.y, side=LEFT,  padx=(0,43))

            self.timing = Label(self.line_frame9, text='Click to generate token no.',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.timing.pack(side=LEFT, pady=self.y,)


            #3th line
            self.line_frame10 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame10.pack(fill=X)

            self.username = Label(self.line_frame10, text='',bg='#f4f4f4',width=19, height='2', font=('verdana', 12),fg='#000000')
            self.username.pack(side=LEFT, pady=self.y, padx=(0,13))

            self.load = PhotoImage(file='all_imgs/load.png')
                           
            self.btn_id = Button(self.line_frame10, image=self.load, height=33, width=50, bg='#0048ad', command=self.generate_id)
            self.btn_id.pack(side=LEFT)


            self.token_en = Label(self.line_frame10, text='',bg='#f4f4f4',width=18, height='2', font=('verdana', 12),fg='#000000')
            self.token_en.pack(side=LEFT, pady=self.y, padx=(18,13))

            self.btn_token = Button(self.line_frame10, image=self.load, height=33, width=50, bg='#0048ad', command=self.generate_token)
            self.btn_token.pack(side=LEFT)
          #9th line

            #nextline
            self.line_frame12 = Frame(self.parent_frame2, bg='#FFFFFF', height=200)
            self.line_frame12.pack(fill=X, pady=self.y)

            self.line_line1 = Frame(self.line_frame12, bg='white')
            self.line_line1.pack(side=TOP, padx=(0,0), pady=6, fill=X)

            self.recept = Label(self.line_line1, text="Click for token's receipt",bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.recept.pack(pady=0, padx=(0,0), side=LEFT)


            self.btn_rcpt = Button(self.line_line1, image=self.load, height=33, width=50, bg='#0048ad', command=self.generate_receipt)
            self.btn_rcpt.pack(padx=10, side=LEFT)


            self.line_line2 = Frame(self.line_frame12, bg='#FFFFFF')
            self.line_line2.pack(side=BOTTOM)
            self.rcpt = Label(self.line_line2, bg='white', font=('verdana',11),height=13, justify=LEFT,width=78, relief='groove', text='')

            self.rcpt.pack(fill='both', pady=(7,7))



            #6th line

            #8th line

            #10thline
            self.line_frame13 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame13.pack(fill=X,pady=0)

            self.submit = Button(self.line_frame13, text='Submit', height=2, width=10, bg='#0048ad', fg='#FFFFFF', font=('verdana', 12), command=self.submit)
            self.submit.pack(side=RIGHT, pady=self.y)

            self.logout = Button(self.line_frame13, text='Logout', height=2, width=10, bg='#0048ad', fg='#FFFFFF', font=('verdana', 12), command=self.logout)
            self.logout.pack(side=RIGHT, pady=self.y, padx=(0,20))

      
      def take_info(self):
            self.f_n=self.first_name_entry.get()
            self.l_n = self.last_name_entry.get()
            self.cnic_n = str(self.CNIC_entry.get())
            
      def search_record(self):
            self.abc = 0
            self.search_entry = self.search.get()
            self.db = sqlite3.connect('database/patient.db')
            for i in self.db.execute("SELECT * FROM PATIENT_DATA WHERE ID='{}'".format(self.search_entry)):
                  print(i)
                  try:
                        self.first_name_entry.insert(0, i[1])
                        self.last_name_entry.insert(0, i[2])
                        self.city_entry.insert(0, i[3])
                        self.country_entry.insert(0, i[4])
                        self.address_entry.insert(0, i[5])
                        self.email_entry.insert(0, i[6])
                        self.phone_entry.insert(0, i[7])
                        self.CNIC_entry.insert(0, i[8])
                        self.abc+=1
                        
                  except:
                        tkm.showinfo('Picture', message="We don't have the Profile picture of this person in our record")

            if self.abc==1:
                  print('yes')
            else:
                  tkm.showinfo('ID', message='Given ID is not found')

            self.search.delete(0,'end')
      
      def generate_id(self):
            self.take_info()
            
            if len(self.f_n)==0 or len(self.l_n)==0 or len(self.cnic_n)==0:
                  tkm.showinfo('ID', "ID can't be generated without filling the required fileds")
            else:
                  self.code1='P-'
                  self.code2=self.f_n[:2]
                  self.code3=self.l_n[0:2]
                  self.code4=self.cnic_n[7:12]
                  self.unique_id = self.code1+self.code2+self.code3+self.code4
                  self.username['text']=self.unique_id
                  print(self.unique_id)


      def generate_token(self):
            self.F = open('text/token.txt', 'r')
            """
            for i in self.F:
                  self.token_no = int(i)+1
            """
            self.token_list=self.F.readline().split(' ')
            self.token_no=int(self.token_list[-1])+1
            self.token_en['text']=self.token_no
            self.add_no_in_file()
            
      def add_no_in_file(self):
            self.F = open('all_imgs/token.txt', 'a')            
            self.F.write(' '+str(self.token_no))
            print('done')

      def generate_receipt(self):
            if self.first_name_entry.get() and self.appo.get()!='Select DR' and self.d.get()!='Day'  and self.m.get()!='Month' and self.ye.get()!='Year' and self.last_name_entry.get() and self.city_entry.get() and self.country_entry.get() and self.address_entry.get() and self.email_entry.get() and self.phone_entry.get() and self.CNIC_entry.get(): 
                  self.f_n=self.first_name_entry.get()
                  self.l_n = self.last_name_entry.get()
                  self.ct_n = self.city_entry.get()
                  self.c_n = self.country_entry.get()
                  self.add = self.address_entry.get()
                  self.ema = self.email_entry.get()
                  self.cell = self.phone_entry.get()
                  self.cnic_n = str(self.CNIC_entry.get())
                  #self.c_t_d
                  #self.unique_id
                  #self.token_no
                  self.appointment_doc = self.appo.get()
                  self.d_o_b = str(self.d.get())+' '+self.m.get()+' '+str(self.ye.get())
         
                  #self.token_rcpt_open = open('token_receipt.txt', 'w')
                  self.age = str(datetime.date.today().year-int(self.ye.get()))
                  self.n=0
                  if len(self.f_n+self.l_n)<16:
                        self.n=16-(len(self.f_n+self.l_n))
                        self.rcpt['text']=self.c_t_d+'\t\t'+'\n\n'+'Token No:  '+str(self.token_no)+'\t\t\t'+'Patient id: '+self.unique_id+'\n\n'+'Name:  '+self.f_n+' '+self.l_n+' '*self.n+'\t\t'+'Age : '+self.age+'\n\n'+'Email:  '+self.ema+'\t'+'Cell: '+self.cell+'\n\n'+'Appointment: Dr.'+self.appointment_doc+'\n\n'+'Receipt generated by:  '+'Muhammad Khalid (RP-muha478995)'
                        print(self.token_no, type(self.token_no))
                  else:
                        tkinter.message.showinfo('Name is too long')
                  self.add_no_in_file()
            else:
                  tkm.showinfo('form', 'Please fill all required field to go forward')
            #tkinter.messagebox.showinfo('Form Sequence', 'Its necessary to fill all the entries in the sequence')
            
      def new_add(self, h):
            pass
            
      def assign_appointment(self):
            pass
      def get_all_data(self):
            pass
      def submit_data(self):
            pass
      def logout(self):
            self.header.destroy()
            self.parent_frame.destroy()
            self.parent_frame2.destroy()
            self.mmain = main_page.main_window(self.main)
            self.mmain.all_buttons()
            self.main.mainloop()
            

      def add_p_id(self, a):
            self.Q = open('text/p_id.txt', 'w')
            self.Q.write(a)
            
      def submit(self):
            self.save_in_db()

      def print_details(self):
            for i in [ self.unique_id, self.f_n, self.l_n, self.ct_n, self.c_n, self.add, self.ema, self.cell, self.cnic_n, self.c_t_d, self.token_no, self.appointment_doc, self.d_o_b]:
                  print(i)
            
      def save_in_db(self):
            try:
                  self.db = sqlite3.connect('database/patient.db')
                  """
                  self.db.execute('''CREATE TABLE PATIENT_DATA (
                        ID                        TEXT,
                        FIRST_NAME              TEXT,
                        LAST_NAME              TEXT,
                        CITY                    TEXT,
                        COUNTRY              TEXT,
                        ADDRESS               TEXT,
                        EMAIL                   TEXT,
                        CELL                     TEXT,
                        CINC                     TEXT,
                        DateTime                TEXT,
                        TOKEN                  TEXT,
                        APPOINTMENT        TEXT,
                        DOB                    TEXT,
                        AGE                     TEXT
                        );''')
                  """
                        
                  self.db.execute("INSERT INTO PATIENT_DATA (ID, FIRST_NAME, LAST_NAME, CITY, COUNTRY, ADDRESS, EMAIL, CELL, CINC, DateTime, TOKEN, APPOINTMENT, DOB, AGE) \
                                                VALUES "+str(tuple([ self.unique_id, self.f_n, self.l_n, self.ct_n, self.c_n, self.add, self.ema, self.cell, self.cnic_n, self.c_t_d, self.token_no, self.appointment_doc, self.d_o_b, self.age])));
                  
                  self.db.commit()
                  self.db.close()
            except:
                  tkm.showinfo('form', "Please! fill all required fields in order to submit the form")
            
            self.first_name_entry.delete(0, 'end')
            self.last_name_entry.delete(0, 'end')
            self.city_entry.delete(0, 'end')
            self.country_entry.delete(0, 'end')
            self.address_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.phone_entry.delete(0, 'end')
            self.CNIC_entry.delete(0, 'end')
            #self.c_t_d
            #self.unique_id
            #self.token_no
            self.appo.current(0)
            self.d.current(0)
            self.m.current(0)
            self.ye.current(0)
            self.rcpt['text']=''
            self.username['text']=''
            self.token_en['text']=''

      
      def abc(self):
            pass
        

          
if __name__=='__main__':
      root=Tk()
      main = patient_form(root, 'RP-AmKh47888')
      main.left_column()
      main.right_column()
      root.mainloop()

