from tkinter import*
from tkinter import ttk
import tkinter.messagebox as tkm
import main_page
import sqlite3
import datetime

class doctor_form:
      def __init__(self, main, info):
            self.info=info
            self.upload_photo_wali_place = 'img-'
            self.db = sqlite3.connect('database/employe.db')
            for i in self.db.execute("SELECT * FROM EMPLOYEES_DATA WHERE ID='{}'".format(self.info)):
                  self.upload_photo_wali_place+=i[8]+'.png'
            self.counter=0
            [self.f_n, self.l_n, self.ct_n, self.c_n, self.add, self.ema, self.cell, self.cnic_n, self.c_t_d, self.token_no, self.unique_id, self.appointment_doc, self.d_o_b] = [None,None,None,None,None,None,None,None,None,None,None,None,None]
            self.currentDT = datetime.datetime.now()
            self.medicine_dict = {}
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

            self.name = Label(self.header, text='DOCTOR', font=('',30),bg='#000000', fg='white')
            self.name.pack(side=LEFT)

            self.photo = PhotoImage(file='all_imgs/search.png')                           
            self.search_btn = Button(self.header, image=self.photo, height=33, width=60, bg='#0048ad',command=self.search_record)
            self.search_btn.pack(side=RIGHT, padx=(10,38))

            self.search = Entry(self.header,font=('verdana', 16), fg='#383737', width=17)
            self.search.pack(side=RIGHT, ipady=4)
            self.search.insert(0, ' Search by ID')
            self.search.bind("<FocusIn>", lambda args: self.search.delete(' 0', 'end'))

      def left_column(self):
            self.y = 7
            self.parent_frame = Frame(self.main, height='550px', width='425px', bg='white')
            self.parent_frame.pack(pady='0', padx=(50,20), side=LEFT)

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
            
            #1st line
            self.line_frame1 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame1.pack(fill=X, pady=(self.y*2,0))

            self.first_name = Label(self.line_frame1, text='First Name', font=('verdana', 12), bg='#FFFFFF',fg='#0049ad' )
            self.first_name.pack(side=LEFT, pady=self.y)

            self.last_name = Label(self.line_frame1, text='Last Name', font=('verdana', 12),bg='#FFFFFF',fg='#0049ad')
            self.last_name.pack(pady=self.y, side=LEFT,  padx=(188,0))

            #2nd line
            self.line_frame2 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame2.pack()
            
            self.first_name_entry = Label(self.line_frame2, font=('verdana', 15), width=17,bg='#f4f4f4',fg='#383737', text='',justify=LEFT)
            self.first_name_entry.pack(side=LEFT, padx=(0,5), pady=self.y)

            self.last_name_entry = Label(self.line_frame2, font=('verdana', 15), bg='#f4f4f4', width=17, fg='#383737', text='',justify=LEFT)
            self.last_name_entry.pack(pady=self.y, side=LEFT, padx=(50,30) )

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
            
            self.city_entry = Label(self.line_frame4, font=('verdana', 15), width=17,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.city_entry.pack(side=LEFT,pady=self.y, padx=(0,5))

            self.country_entry = Label(self.line_frame4, font=('verdana', 15), width=17,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.country_entry.pack(pady=self.y, side=LEFT, padx=(50,30) )

            #5th line
            self.line_frame5 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame5.pack(fill=X)

            self.address = Label(self.line_frame5, text='Complete Address (current)',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.address.pack(pady=self.y, padx=(0,315))

            self.address_entry = Label(self.line_frame5, font=('verdana', 15), width=39,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.address_entry.pack(side=LEFT, padx=(3,0),pady=self.y)
            
            #11th line
            self.line_frame11 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame11.pack(fill=X)

            self.cnic = Label(self.line_frame11, text='Email Address',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.cnic.pack(pady=self.y, side=LEFT, )

            #12thline
            self.line_frame12 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame12.pack(fill=X)
            
            self.email_entry = Label(self.line_frame12, font=('verdana', 15), width=39,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.email_entry.pack(side=LEFT, padx=(3,0),pady=self.y)


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
            
            self.phone_entry = Label(self.line_frame8, font=('verdana', 15), width=18,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.phone_entry.pack(side=LEFT,pady=self.y, padx=(3,7))

            self.CNIC_entry = Label(self.line_frame8, font=('verdana', 15), width=19,bg='#f4f4f4',fg='#383737', text='', justify=LEFT)
            self.CNIC_entry.pack(pady=self.y, side=LEFT, padx=(30,20))

  
            #13thline
            self.line_frame13 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame13.pack(fill=X,pady=self.y)

      def right_column(self):

            self.y = 7
            self.parent_frame2 = Frame(self.main, height='550px', width='425px', bg='#FFFFFF')
            self.parent_frame2.pack(padx='50', side=LEFT)

            #1st line
            
            self.line_frame0 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame0.pack(fill=X)

            self.logout = Button(self.line_frame0, text='Logout', height=1, width=10, bg='#0048ad', fg='#FFFFFF', font=('verdana', 12), command=self.logout)
            self.logout.pack(fill=X, pady=self.y, padx=(0,0))

            self.line_frame1 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame1.pack(fill=X)

            self.first_name = Label(self.line_frame1, text='Date & Time', font=('verdana', 12), bg='#FFFFFF',fg='#0049ad' )
            self.first_name.pack(side=LEFT, pady=(5,5))


            #2nd line
            self.line_frame2 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame2.pack(fill=X)

            self.dt = Label(self.line_frame2, text=self.date+'  |  '+self.time, width=32, bg='#f4f4f4', height='2', font=('verdana', 12),fg='#000000')
            self.dt.pack(side=LEFT,pady=20, padx=(0,0))


            #1th line
            self.line_frame9 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame9.pack(fill=X,pady=self.y)

            self.Desig = Label(self.line_frame9, text='Enter the Recommended Medicines',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.Desig.pack(side=LEFT, pady=10)

            self.number = Entry(self.line_frame9,width=4, font=('verdana', 16),fg='#000000')
            self.number.pack(side=LEFT, pady=self.y, padx=(29,30))

            self.btn = Button(self.line_frame9, text='OK', height=1, font=('verdana', 12), fg='white',width=4, bg='#0048ad', command=self.add_medicine)
            self.btn.pack(side=LEFT)

            #10th line
            self.line_frame10 = Frame(self.parent_frame2, bg='white')
            self.line_frame10.pack(fill=X)

            """
            for i in self.doctor_file:
                  if len(i)>0:
                        self.LIST.append(i)
            """
    

            #2th line
            self.line_frame9 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame9.pack(fill=X, pady=5)

            self.id = Label(self.line_frame9, text='Enter Medicines',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.id.pack(pady=20, side=LEFT,  padx=(0,90))

            self.timing = Label(self.line_frame9, text='Dose/Day',bg='#FFFFFF', font=('verdana', 12),fg='#0049ad')
            self.timing.pack(side=LEFT, pady=15, padx=(90,0))

      def generate_receipt(self):
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
            
            #tkinter.messagebox.showinfo('Form Sequence', 'Its necessary to fill all the entries in the sequence')

      def search_record(self):
            self.abc = 0
            self.search_entry = self.search.get()
            self.db = sqlite3.connect('database/patient.db')
            for i in self.db.execute("SELECT * FROM PATIENT_DATA WHERE ID='{}'".format(self.search_entry)):
                  print(i)
                  self.first_name_entry['text']=i[1]
                  self.last_name_entry['text']=i[2]
                  self.city_entry['text']=i[3]
                  self.country_entry['text']=i[4]
                  self.address_entry['text']=i[5]
                  self.email_entry['text']=i[6]
                  self.phone_entry['text']=i[7]
                  self.CNIC_entry['text']=i[8]
                  self.abc=1
                  print(4)

            if self.abc==1:
                  print('yes')
            else:
                  tkm.showinfo(message='Given ID not found in our record')

            self.search.delete(0,'end')
            

            
      def submit(self):
            """
            self.first_name_entry['text']=''
            self.last_name_entry['text']=''
            self.city_entry['text']=''
            self.country_entry['text']=''
            self.address_entry['text']=''
            self.email_entry['text']=''
            self.phone_entry['text']=''
            self.CNIC_entry['text']=''
            self.number.delete(0, 'end')
            """
            self.extra = self.search_entry
            for i in self.medicine_dict:
                  self.extra+='='+(i+'  '+str(self.medicine_dict[i]))
            
            self.medicine_text = open('text/medicine.txt','a')
            self.medicine_text.write('\n{}'.format(self.extra))
            self.medicine_text.close()
                                                
            self.header.destroy()
            self.parent_frame.destroy()
            self.parent_frame2.destroy()
            self.mmain = doctor_form(self.main, 'DR-MuSa59000')
            self.mmain.left_column()
            self.mmain.right_column()

      def logout(self):
            self.parent_frame.destroy()
            self.parent_frame2.destroy()
            self.mmain = main_page.main_window(self.main)
            self.mmain.all_buttons()
            self.main.mainloop()


      
      def add_medicine(self):
            self.btn['command']=''
            try:
                  if self.number.get():
                        if int(self.number.get())==0:
                              #self.btn['command']=''
                              tkm.showinfo(message=' Please write the number of medicines \n\n If no need of medicines then not necessary to fill it')
                              self.wow()
                                    
                        elif int(self.number.get())<9 and int(self.number.get())!=9:
                              if self.counter<int(self.number.get()):
                                    if self.counter>0:
                                          self.btn_token['command']=''
                                          try:
                                                if len(self.username.get())!=0 and self.token_en.get():
                                                      self.medicine_dict[self.username.get()]=int(self.token_en.get())
                                                      print(self.medicine_dict)                               
                                                      self.line_frame10 = Frame(self.parent_frame2, bg='#FFFFFF')
                                                      self.line_frame10.pack(fill=X)

                                                      self.username = Entry(self.line_frame10,width=22, font=('verdana', 16),fg='#000000')
                                                      self.username.pack(side=LEFT, pady=self.y, padx=(0,13))


                                                      self.token_en = Entry(self.line_frame10,width=4, font=('verdana', 16),fg='#000000')
                                                      self.token_en.pack(side=LEFT, pady=self.y, padx=(18,30))

                                                      self.btn_token = Button(self.line_frame10, text='+', height=1, font=('verdana', 12), fg='white',width=4, bg='#0048ad', command=self.add_medicine)
                                                      self.btn_token.pack(side=LEFT)
                                                      self.counter+=1
                                                else:
                                                      tkm.showinfo('Error', 'Please! write Medicine name and Dose')
                                                      self.btn_token['command']=self.add_medicine
                                          except:
                                                tkm.showinfo('Error', 'Please! write Medicine name and Dose')
                                                self.btn_token['command']=self.add_medicine
                                    else:      
                                          self.line_frame10 = Frame(self.parent_frame2, bg='#FFFFFF')
                                          self.line_frame10.pack(fill=X)
                                                
                                          self.username = Entry(self.line_frame10,width=22, font=('verdana', 16),fg='#000000')
                                          self.username.pack(side=LEFT, pady=self.y, padx=(0,13))


                                          self.token_en = Entry(self.line_frame10,width=4, font=('verdana', 16),fg='#000000')
                                          self.token_en.pack(side=LEFT, pady=self.y, padx=(18,30))
                                                
                                          self.btn_token = Button(self.line_frame10, text='+', height=1, font=('verdana', 12), fg='white',width=4, bg='#0048ad', command=self.add_medicine)
                                          self.btn_token.pack(side=LEFT)
                                          print(self.medicine_dict)
                                          self.counter+=1
                              else:
                                    if len(self.username.get())!=0 and self.token_en.get():
                                          self.medicine_dict[self.username.get()]=int(self.token_en.get())         
                                          self.wow()
                                          print(self.medicine_dict)
                                          self.btn_token['command']=''
                                    else:
                                          tkm.showinfo('Error', 'Please! write Medicine name and Dose')
                                          
                        elif int(self.number.get())>9:
                              tkm.showinfo(message='Larger recommendation is not allowed\nUse a paper for that.')
                  else:
                        tkm.showinfo('Medicines',message=' Please write the number of medicines \n\n If no need of medicines then not necessary to fill it')
                        self.wow()
                        self.btn['command']=''
            except:
                  tkm.showinfo('Error', 'Invalid Entry for Medicines number')
                  self.btn['command']=self.add_medicine
            
      def print_details(self):
            for i in [ self.unique_id, self.f_n, self.l_n, self.ct_n, self.c_n, self.add, self.ema, self.cell, self.cnic_n, self.c_t_d, self.token_no, self.appointment_doc, self.d_o_b]:
                  print(i)
            
      def save_in_db(self):
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
      
      
            self.db.execute("INSERT INTO PATIENT_DATA (ID, FIRST_NAME, LAST_NAME, CITY, COUNTRY, ADDRESS, EMAIL, CELL, CINC, DateTime, TOKEN, APPOINTMENT, DOB, AGE) \
                              VALUES "+str(tuple([ self.unique_id, self.f_n, self.l_n, self.ct_n, self.c_n, self.add, self.ema, self.cell, self.cnic_n, self.c_t_d, self.token_no, self.appointment_doc, self.d_o_b, self.age])));
            self.db.commit()
            self.db.close()

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
            """
            pass
          
if __name__=='__main__':
      root=Tk()
      main = doctor_form(root, 'DR-MuSa59000')
      main.left_column()
      main.right_column()
      root.mainloop()


