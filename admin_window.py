import sqlite3
from tkinter import*
import shutil, os
from tkinter import filedialog
from tkinter import ttk
import datetime
import main_page
import tkinter.messagebox as tkm

class form:
      def __init__(self, main):
            self.newnew = 0
            [self.f_n, self.l_n, self.ct_n, self.c_n, self.add, self.ema, self.cell, self.cnic_n, self.desig, self.d_o_b, self.unique_id, self.timing, self.rlgn, self.spclty, self.qual, self.ins_n, self.pwwp] = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
      
            self.currentDT = datetime.datetime.now()
                  
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

            self.name = Label(self.header, text='ADMIN', font=('',30),bg='#000000', fg='white')
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

            #1st line
            self.line_frame1 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame1.pack(fill=X)

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

            #6th line
            self.line_frame6 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame6.pack(fill=X,pady=self.y)

            self.address_c = Label(self.line_frame6, text='Complete Address (permanent)',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.address_c.pack(pady=self.y, padx=(0,280))

            self.address_c_entry = Entry(self.line_frame6, font=('verdana', 15), fg='#383737')
            self.address_c_entry.pack(fill=X, padx=(3,0),pady=self.y)

            
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

            #9th line
            self.line_frame9 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame9.pack(fill=X,pady=self.y)

            self.Desig = Label(self.line_frame9, text='Designation',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.Desig.pack(side=LEFT, pady=self.y,)

            self.email = Label(self.line_frame9, text='Date of Birth',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.email.pack(pady=self.y, side=LEFT,  padx=(175,0))

            #10th line
            self.line_frame10 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame10.pack(fill=X)

            self.designation = ttk.Combobox(self.line_frame10, values=['Select','Doctor', 'Pharmacist', 'Receptionist'], font=('verdana',12))
            self.designation.current(0)
            self.designation.pack(side=LEFT,pady=self.y, padx=(4,17))


            self.d = ttk.Combobox(self.line_frame10, values=['Day']+list(range(1,32)), font=('verdana',12), width=4)
            self.d.current(0)
            self.d.pack(side=LEFT, pady=self.y, padx=(39,10))

            
            self.m = ttk.Combobox(self.line_frame10, values=['Month']+('Jan Feb Mar Apr May Jun July Aug Sep Oct Nov Dec'.split()), font=('verdana',12), width=5)
            self.m.current(0)
            self.m.pack(side=LEFT, pady=self.y, padx=(10,10))
            
            
            self.ye = ttk.Combobox(self.line_frame10, values=['Year']+list(range(1900,2020))[::-1], font=('verdana',12), width=4)
            self.ye.current(0)
            self.ye.pack(side=LEFT, padx=(10), pady=self.y)

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
            self.parent_frame2.pack(pady='0', padx='20', side=LEFT)

            #1st line
            self.line_frame1 = Frame(self.parent_frame2, bg='#FFFFFF', height=140)
            self.line_frame1.pack(fill=X, pady=(5,0))

            self.upload = PhotoImage(file='all_imgs/uploadd.png')
            self.picframe = Button(self.line_frame1, cursor='hand2',relief='flat',height=180, image=self.upload, width=141, bg='#FFFFFF', command=self.upload_photo)
            self.picframe.pack(pady=(0,0), side=RIGHT)

            self.instructions=Label(self.line_frame1, anchor='w', bg='#FFFFFF', text='1)  Selected photo should be 2 x 3 inches.\n\n2)  Selected photo must be in GIF format.\n\n3)  Resolution must be 45 pixels/inch.\n\n4)  Background must be white or Blue in photo.', justify=LEFT, font=('verdana',12))
            self.instructions.pack(fill='both', pady=(26,0))

            #2th line
            self.line_frame9 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame9.pack(fill=X, pady=5)

            self.id = Label(self.line_frame9, text='Click to generate Username/ID',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.id.pack(pady=self.y, side=LEFT,  padx=(0,19))

            self.timing = Label(self.line_frame9, text='Timing',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.timing.pack(side=LEFT, pady=(self.y,0))


            #3th line
            self.line_frame10 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame10.pack(fill=X)

            self.username = Label(self.line_frame10, text='',bg='#f4f4f4',width=19, height='2', font=('verdana', 12),fg='#000000')
            self.username.pack(side=LEFT, pady=self.y, padx=(0,13))

            self.load = PhotoImage(file='all_imgs/load.png')
                           
            self.btn_id = Button(self.line_frame10, image=self.load, height=33, width=50, bg='#0048ad', command=self.generate_id)
            self.btn_id.pack(side=LEFT)

            self.pm = ttk.Combobox(self.line_frame10, values=['PM','AM'], font=('verdana',12), width=5)
            self.pm.current(0)
            self.pm.pack(side=RIGHT,pady=self.y, padx=(10,0))


            self.hour2 = ttk.Combobox(self.line_frame10, values=['--']+list(range(1,13)), font=('verdana',12), width=3)
            self.hour2.current(0)
            self.hour2.pack(side=RIGHT,pady=self.y, padx=(17,17))

            self.to = Label(self.line_frame10, text='to',bg='#FFFFFF', font=('verdana', 12),fg='#000000')
            self.to.pack(side=RIGHT, pady=self.y,)
            
            self.hour1 = ttk.Combobox(self.line_frame10, values=['--']+list(range(1,13)), font=('verdana',12), width=3)
            self.hour1.current(0)
            self.hour1.pack(side=RIGHT,pady=self.y, padx=(15,17))


            #4th line
            self.line_frame7 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame7.pack(fill=X,pady=self.y)
            #self.relgn
            self.religion = Label(self.line_frame7, text='Religion',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.religion.pack(side=LEFT, pady=self.y, padx=(0,0))

            self.spe = Label(self.line_frame7, text='Speciality (optional)',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.spe.pack(pady=self.y, side=LEFT,  padx=(209,0))

            #5th line
            self.line_frame8 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame8.pack()
            
            self.religioon = Entry(self.line_frame8, font=('verdana', 15), fg='#383737')
            self.religioon.pack(side=LEFT,pady=self.y, padx=(0,7))
            #spclty
            self.speciality = Entry(self.line_frame8, font=('verdana', 15), fg='#383737')
            self.speciality.pack(pady=self.y, side=LEFT, padx=(10,0))

          

            #6th line
            self.line_frame5 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame5.pack(fill=X)

            self.qua = Label(self.line_frame5, text='Qualification',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.qua.pack(pady=self.y, padx=(0,435))
            #self.qual
            self.qualification = Entry(self.line_frame5, font=('verdana', 15), fg='#383737')
            self.qualification.pack(fill=X, padx=(0,0),pady=self.y)

            #7th line
            self.line_frame6 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame6.pack(fill=X,pady=self.y)

            self.ins = Label(self.line_frame6, text='Institute (complete name)',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.ins.pack(pady=self.y, padx=(0,320))
            #inst_n
            self.institute = Entry(self.line_frame6, font=('verdana', 15), fg='#383737')
            self.institute.pack(fill=X, padx=(0,0),pady=self.y)

            
            #8th line
            self.line_frame11 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame11.pack(fill=X)

            self.work_p = Label(self.line_frame11, text='Previous Working Place (with years of experience)',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.work_p.pack(pady=self.y, side=LEFT, padx=(0,0) )

            #9thline
            self.line_frame12 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame12.pack(fill=X)
            #self.pwwp
            self.pwp =Entry(self.line_frame12, font=('verdana', 15), fg='#383737')
            self.pwp.pack(fill=X, padx=(0,0),pady=self.y)


            #10thline
            self.line_frame13 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame13.pack(fill=X,pady=self.y)

            self.submit = Button(self.line_frame13, text='Submit', height=2, width=10, bg='#0048ad', fg='#FFFFFF', font=('verdana', 12), command=self.get_info)
            self.submit.pack(side=RIGHT, pady=self.y*2)

            self.logout = Button(self.line_frame13, text='Logout', height=2, width=10, bg='#0048ad', fg='#FFFFFF', font=('verdana', 12), command=self.logout)
            self.logout.pack(side=RIGHT, pady=self.y*2, padx=(0,20))

      def upload_photo(self):
            try:
                  self.take_info()
                  self.filename = filedialog.askopenfilename()
                  shutil.copy(self.filename,'temp/img-'+self.cnic_n+'.png')
                  self.PHOTO = PhotoImage(file='temp/img-'+self.cnic_n+'.png')
                  self.picframe['image']=self.PHOTO
            except:
                  tkm.showinfo('Picture', 'You have not selected the picture')
            
      def take_info(self):
            self.f_n=self.first_name_entry.get()
            self.l_n = self.last_name_entry.get()
            self.cnic_n = str(self.CNIC_entry.get())
            self.desig = self.designation.get()

      def search_record(self):
            self.abc = 0
            self.search_entry = self.search.get()
            self.db = sqlite3.connect('database/employe.db')
            for i in self.db.execute("SELECT * FROM EMPLOYEES_DATA WHERE ID='{}'".format(self.search_entry)):
                  print(i)
                  try:
                        self.first_name_entry.insert(0,i[1])
                        self.last_name_entry.insert(0,i[2])
                        self.city_entry.insert(0,i[3])
                        self.country_entry.insert(0,i[4])
                        self.address_entry.insert(0,i[5])
                        self.address_c_entry.insert(0,i[5])
                        self.email_entry.insert(0,i[6])
                        self.phone_entry.insert(0,i[7])
                        self.CNIC_entry.insert(0,i[8])
                        
                        if self.search_entry[0:2]=='DR':
                              self.designation.current(1)
                        elif self.search_entry[0:2]=='RP':
                              self.designation.current(3)
                        elif self.search_entry[0:2]=='PH':
                              self.designation.current(2)

                        self.username['text']=self.search_entry
                        self.religioon.insert(0,i[12])
                        self.hour1.current(int(i[11][0]))
                        self.hour2.current(int(i[11][5]))
                        if i[11][7:9]=='PM':
                              self.pm.current(0)
                        else:
                              self.pm.current(1)
                        self.speciality.insert(0,i[13])
                        self.qualification.insert(0,i[14])
                        self.institute.insert(0,i[15])
                        self.pwp.insert(0,i[16])
                        self.abc+=1
                        self.piccc = PhotoImage(file='images/img-'+i[8]+'.png')
                        self.picframe['image']=self.piccc
                  except:
                        tkm.showinfo('Picture', message="We don't have the Profile picture of this person in our record")

            if self.abc==1:
                  print('yes')
            else:
                  tkm.showinfo('ID', message='Given ID is not found')

            self.search.delete(0,'end')
      
            
      def generate_id(self):
            try:
                  self.take_info()
                  if self.designation.get()=='Doctor':
                        self.code1='DR-'
                  elif self.designation.get()=='Pharmacist':
                        self.code1='PH-'
                  elif self.designation.get()=='Receptionist':
                        self.code1='RP-'
                  self.code2=self.f_n[:2]
                  self.code3=self.l_n[0:2]
                  self.code4=self.cnic_n[7:12]
                  self.unique_id = self.code1+self.code2+self.code3+self.code4
                  self.username['text']=self.unique_id
                  self.submit_in_file()
            except:
                  tkm.showinfo('ID', "ID can't be generated without required information")

      #def submit
      def submit_in_file(self):
            file = open('text/doctor_name.txt','a')
            if self.designation.get()=='Doctor':
                  file.write('='+self.f_n+' '+self.l_n)
                  print('done')
            
            
      def logout(self):
            import main_page
            self.header.destroy()
            self.parent_frame.destroy()
            self.parent_frame2.destroy()
            self.mmain = main_page.main_window(self.main)
            self.mmain.all_buttons()
            self.main.mainloop()
            
      def get_info(self):
            try:
                  if self.newnew==0:
                        if self.first_name_entry.get() and self.d.get() and self.m.get() and self.ye.get() and self.last_name_entry.get() and self.city_entry.get() and self.country_entry.get() and self.address_entry.get() and self.email_entry.get() and self.phone_entry.get() and self.CNIC_entry.get() and self.designation.get()!='Select' and self.d.get()!='Day' and self.m.get()!='Month' and self.ye.get()!='Year' and self.hour1.get()!='--' and self.hour2.get()!='--' and self.pm.get() and self.religioon.get() and self.speciality.get() and self.qualification.get() and self.institute and self.pwp:
                              if self.hour1.get()==self.hour2.get():
                                    tkm.showinfo('Time Error',message='Invalid time period of job')
                              else:
                                    self.f_n=self.first_name_entry.get()
                                    self.l_n = self.last_name_entry.get()
                                    self.ct_n = self.city_entry.get()
                                    self.c_n = self.country_entry.get()
                                    self.add = self.address_entry.get()
                                    self.ema = self.email_entry.get()
                                    self.cell = self.phone_entry.get()
                                    self.cnic_n = str(self.CNIC_entry.get())
                                    self.desig = self.designation.get() 
                                    self.timing = self.hour1.get()+' to '+self.hour2.get()+' '+self.pm.get()
                                    self.rlgn = self.religioon.get()
                                    self.spclty = self.speciality.get()
                                    self.qual = self.qualification.get()
                                    self.ins_n = self.institute.get()  
                                    self.pwwp = self.pwp.get()
                                    #self.c_t_d
                                    #self.unique_id
                                    #self.token_no
                                    self.d_o_b = str(self.d.get())+' '+self.m.get()+' '+str(self.ye.get())
                                    self.save_in_db()
                                    self.clear()
                                    self.print_details()
                                    self.newnew=0
                                    shutil.copy('temp/img-'+self.cnic_n+'.png','images/img-'+self.cnic_n+'.png')
                        else:
                              tkm.showinfo('form', message='Please! fill all the required field to submit the form')
                  else:
                        tkm.showinfo('form', message='This person is already exist in our record')
            except:
                  tkm.showinfo('picture', message=" You have not added the picture \n\n Don't worry, remaining information has been added")
                  


      def clear(self):
            self.username['text']=''
            self.first_name_entry.delete(0,'end')
            self.last_name_entry.delete(0,'end')
            self.city_entry.delete(0,'end')
            self.address_c_entry.delete(0,'end')
            self.country_entry.delete(0,'end')
            self.address_entry.delete(0,'end')
            self.email_entry.delete(0,'end')
            self.phone_entry.delete(0,'end')
            self.CNIC_entry.delete(0,'end')
            self.designation.current(0)
            self.hour1.current(0)
            self.hour2.current(0)
            self.pm.current(0)
            self.religioon.delete(0,'end')
            self.speciality.delete(0,'end')
            self.d.current(0)
            self.m.current(0)
            self.ye.current(0)
            self.qualification.delete(0,'end')
            self.institute.delete(0,'end')
            self.pwp.delete(0,'end')

      def save_in_db(self):
            self.db = sqlite3.connect('database/employe.db')
            """
            self.db.execute('''CREATE TABLE EMPLOYEES_DATA (
                  ID                        TEXT,
                  FIRST_NAME              TEXT,
                  LAST_NAME              TEXT,
                  CITY                    TEXT,
                  COUNTRY              TEXT,
                  ADDRESS               TEXT,
                  EMAIL                   TEXT,
                  CELL                     TEXT,
                  CINC                     TEXT,
                  DESIGNATION        TEXT,
                  DOB                    TEXT,
                  TIMING                TEXT,
                  RELIGION              TEXT,
                  SPECIALITY            TEXT,
                  QUALIFICATION      TEXT,
                  INSTITUTE             TEXT,
                  Previous_Working_place_exp       TEXT,
                  );''')
            """
            self.LISTT = []
            for i in seld.db.execute("SELECT ID FROM EMPLOYEES_DATA"):
                  self.LISTT.append(i[0])

            if self.unique_id in self.LISTT:
                  tkm.showinfo('form', 'This person is already exist in our record')
            else:
                  self.db.execute("INSERT INTO EMPLOYEES_DATA (ID, FIRST_NAME, LAST_NAME, CITY, COUNTRY, ADDRESS, EMAIL, CELL, CINC, DESIGNATION, DOB, TIMING, RELIGION, SPECIALITY, QUALIFICATION, INSTITUTE, Previous_Working_place_exp) \
                                    VALUES "+str(tuple([self.unique_id, self.f_n, self.l_n, self.ct_n, self.c_n, self.add, self.ema, self.cell, self.cnic_n, self.desig, self.d_o_b, self.timing, self.rlgn, self.spclty, self.qual, self.ins_n, self.pwwp])));
                  self.db.commit()
                  self.db.close()
            


            
      def print_details(self):
            for i in [self.f_n, self.l_n, self.ct_n, self.c_n, self.add, self.ema, self.cell, self.cnic_n, self.desig, self.d_o_b, self.unique_id, self.timing, self.rlgn, self.spclty, self.qual, self.ins_n, self.pwwp]:
                  print(i)
      

"""
large_font = ('Verdana',25)

def activate():
      btn = Button(a, text='wwooww', height='4', width='4')
      btn.pack()

      en = Entry(a, font=large_font, fg='gray')
      en.insert(0, 'username', )
      en.pack(ipadx=10, ipady=10)
      en.bind("<FocusIn>", lambda args: en.delete(' 0', 'end'))
"""

if __name__=='__main__':
      a = Tk()
      main = form(a)
      main.left_column()
      main.right_column()
      a.mainloop()

"""
from tkinter import *

#------------------------------------

def addBox():
    print("ADD")

    ent = Entry(root)
    ent.pack()

    all_entries.append( ent )

#------------------------------------

def showEntries():

    for number, ent in enumerate(all_entries):
        print(number, ent.get())

#------------------------------------

all_entries = []

root = Tk()

showButton = Button(root, text='Show all text', command=showEntries)
showButton.pack()

addboxButton = Button(root, text='<Add Time Input>', fg="Red", command=addBox)
addboxButton.pack()

root.mainloop()
"""
