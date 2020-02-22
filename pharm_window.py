from tkinter import*
from tkinter import ttk
import tkinter.messagebox as tkm
import main_page
import sqlite3
import datetime

class patient_bill:
      def __init__(self, main, info):
            self.tadaad = 2
            self.DICT = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
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

            self.name = Label(self.header, text='PHARMACIST', font=('',30),bg='#000000', fg='white')
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
            """
            self.linee=Frame(self.line_frame0, bg='gray', height='1', width='390')
            self.linee.pack(side=BOTTOM, pady=(0,0))
            """
            
            #1st line
            self.line_frame1 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame1.pack(fill=X)

            self.first_name = Label(self.line_frame1, text='No. of total medicines', font=('verdana', 13), bg='#FFFFFF',fg='#0049ad' )
            self.first_name.pack(side=LEFT)

            self.w = Label(self.line_frame1, text='', width=4, height=2, font=('verdana', 12),bg='#f4f4f4',fg='#000000')
            self.w.pack(side=LEFT,  padx=(15,0))

            #2nd line
            
            self.num = Entry(self.line_frame1, width=3, font=('verdana', 14),fg='#000000')
            self.num.pack(pady=self.y-3, side=RIGHT,  padx=(19,10))

            self.first_name = Label(self.line_frame1, text='Days for medicines', font=('verdana', 13), bg='#FFFFFF',fg='#0049ad' )
            self.first_name.pack(side=RIGHT, pady=self.y, padx=(0,0))

            #3rd line
            self.line_frame3 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame3.pack(fill=X, pady=(20,10))

            self.first_name = Label(self.line_frame3, text='Medicine Name', font=('verdana', 12),bg='#FFFFFF',fg='#0049ad')
            self.first_name.pack(side=LEFT, pady=self.y,)

            self.last_name = Label(self.line_frame3, text='Dose/D', font=('verdana', 12),bg='#FFFFFF',fg='#0049ad')
            self.last_name.pack(pady=self.y, side=LEFT,  padx=(105,0))

            self.last_name = Label(self.line_frame3, text='Rs/Tab', font=('verdana', 12),bg='#FFFFFF',fg='#0049ad')
            self.last_name.pack(pady=self.y, side=LEFT,  padx=(26,0))

            self.last_name = Label(self.line_frame3, text='Price of {} days'.format(self.tadaad), font=('verdana', 12),bg='#FFFFFF',fg='#0049ad')
            self.last_name.pack(pady=self.y, side=LEFT,  padx=(28,0))


            self.table(self.DICT[0][0], self.DICT[0][1])
            self.table(self.DICT[1][0], self.DICT[1][1])
            self.table(self.DICT[2][0], self.DICT[2][1])
            self.table(self.DICT[3][0], self.DICT[3][1])
            self.table(self.DICT[4][0], self.DICT[4][1])
            self.table(self.DICT[5][0], self.DICT[5][1])
            self.table(self.DICT[6][0], self.DICT[6][1])
            self.table(self.DICT[7][0], self.DICT[7][1])
            
            #4th line
            """
            self.medicine_t = open('text/medicine.txt', 'r')
            for i in self.medicine_t:
                  if sel
            for i in range(0,self.tadaad):
                  self.table()
            """
            
            #5th line
      def table(self, name=None, dose=None):
            self.name = name
            self.dose = dose
            self.line_frame4 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame4.pack()
            
            self.md = Label(self.line_frame4, font=('verdana', 15), width=16,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.md.pack(side=LEFT,pady=self.y, padx=(0,10))

            self.dose = Label(self.line_frame4, font=('verdana', 15), width=5,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.dose.pack(pady=self.y, side=LEFT, padx=(10,10) )

            self.per_t = Entry(self.line_frame4, font=('verdana', 15), width=5, fg='#383737', justify=LEFT)
            self.per_t.pack(pady=self.y, side=LEFT, padx=(10,10) )
            

            self.all_day = Label(self.line_frame4, font=('verdana', 15), width=9,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.all_day.pack(pady=self.y, side=LEFT, padx=(10,0) )

            """
            #8th line

            self.line_frame6 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame6.pack()
            
            self.md2 = Label(self.line_frame6, font=('verdana', 15), width=16,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.md2.pack(side=LEFT,pady=self.y, padx=(0,10))

            self.dose2 = Label(self.line_frame6, font=('verdana', 15), width=5,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.dose2.pack(pady=self.y, side=LEFT, padx=(10,10) )

            self.per_t2 = Entry(self.line_frame6, font=('verdana', 15), width=5, fg='#383737', justify=LEFT)
            self.per_t2.pack(pady=self.y, side=LEFT, padx=(10,10) )
            

            self.all_day2 = Label(self.line_frame6, font=('verdana', 15), width=9,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.all_day2.pack(pady=self.y, side=LEFT, padx=(10,0) )
            #------------------------------
            self.line_frame5 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame5.pack()
            
            self.md3 = Label(self.line_frame5, font=('verdana', 15), width=16,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.md3.pack(side=LEFT,pady=self.y, padx=(0,10))

            self.dose3 = Label(self.line_frame5, font=('verdana', 15), width=5,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.dose3.pack(pady=self.y, side=LEFT, padx=(10,10) )

            self.per_t3 = Entry(self.line_frame5, font=('verdana', 15), width=5, fg='#383737', justify=LEFT)
            self.per_t3.pack(pady=self.y, side=LEFT, padx=(10,10) )
            

            self.all_day3 = Label(self.line_frame5, font=('verdana', 15), width=9,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.all_day3.pack(pady=self.y, side=LEFT, padx=(10,0) )
            #------------------------------
            self.line_frame5 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame5.pack()
            
            self.md4 = Label(self.line_frame5, font=('verdana', 15), width=16,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.md4.pack(side=LEFT,pady=self.y, padx=(0,10))

            self.dose4 = Label(self.line_frame5, font=('verdana', 15), width=5,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.dose4.pack(pady=self.y, side=LEFT, padx=(10,10) )

            self.per_t4 = Entry(self.line_frame5, font=('verdana', 15), width=5, fg='#383737', justify=LEFT)
            self.per_t4.pack(pady=self.y, side=LEFT, padx=(10,10) )
            

            self.all_day4 = Label(self.line_frame5, font=('verdana', 15), width=9,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.all_day4.pack(pady=self.y, side=LEFT, padx=(10,0) )
            #------------------------------
            self.line_frame5 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame5.pack()
            
            self.md5 = Label(self.line_frame5, font=('verdana', 15), width=16,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.md5.pack(side=LEFT,pady=self.y, padx=(0,10))

            self.dose5 = Label(self.line_frame5, font=('verdana', 15), width=5,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.dose5.pack(pady=self.y, side=LEFT, padx=(10,10) )

            self.per_t5 = Entry(self.line_frame5, font=('verdana', 15), width=5, fg='#383737', justify=LEFT)
            self.per_t5.pack(pady=self.y, side=LEFT, padx=(10,10) )
            

            self.all_day5 = Label(self.line_frame5, font=('verdana', 15), width=9,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.all_day5.pack(pady=self.y, side=LEFT, padx=(10,0) )
            #------------------------------
            self.line_frame5 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame5.pack()
            
            self.md6 = Label(self.line_frame5, font=('verdana', 15), width=16,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.md6.pack(side=LEFT,pady=self.y, padx=(0,10))

            self.dose6 = Label(self.line_frame5, font=('verdana', 15), width=5,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.dose6.pack(pady=self.y, side=LEFT, padx=(10,10) )

            self.per_t6 = Entry(self.line_frame5, font=('verdana', 15), width=5, fg='#383737', justify=LEFT)
            self.per_t6.pack(pady=self.y, side=LEFT, padx=(10,10) )
            

            self.all_day6 = Label(self.line_frame5, font=('verdana', 15), width=9,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.all_day6.pack(pady=self.y, side=LEFT, padx=(10,0) )
            #------------------------------
            self.line_frame5 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame5.pack()
            
            self.md7 = Label(self.line_frame5, font=('verdana', 15), width=16,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.md7.pack(side=LEFT,pady=self.y, padx=(0,10))

            self.dose7 = Label(self.line_frame5, font=('verdana', 15), width=5,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.dose7.pack(pady=self.y, side=LEFT, padx=(10,10) )

            self.per_t7 = Entry(self.line_frame5, font=('verdana', 15), width=5, fg='#383737', justify=LEFT)
            self.per_t7.pack(pady=self.y, side=LEFT, padx=(10,10) )
            

            self.all_day7 = Label(self.line_frame5, font=('verdana', 15), width=9,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.all_day7.pack(pady=self.y, side=LEFT, padx=(10,0) )
            #------------------------------
            self.line_frame5 = Frame(self.parent_frame, bg='#FFFFFF')
            self.line_frame5.pack()
            
            self.md8 = Label(self.line_frame5, font=('verdana', 15), width=16,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.md8.pack(side=LEFT,pady=self.y, padx=(0,10))

            self.dose8 = Label(self.line_frame5, font=('verdana', 15), width=5,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.dose8.pack(pady=self.y, side=LEFT, padx=(10,10) )

            self.per_t8 = Entry(self.line_frame5, font=('verdana', 15), width=5, fg='#383737', justify=LEFT)
            self.per_t8.pack(pady=self.y, side=LEFT, padx=(10,10) )
            

            self.all_day8 = Label(self.line_frame5, font=('verdana', 15), width=9,bg='#f4f4f4',fg='#383737',text='', justify=LEFT)
            self.all_day8.pack(pady=self.y, side=LEFT, padx=(10,0) )

            #-------------------
            """
  

            


      def right_column(self):

            self.y = 7
            self.parent_frame2 = Frame(self.main, height='550px', width='100px', bg='#FFFFFF')
            self.parent_frame2.pack(padx='50',side=LEFT, fill=X)

            
            self.line_frame1 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame1.pack(fill=X)

            self.first_name = Label(self.line_frame1, text='Date & Time', font=('verdana', 12), bg='#FFFFFF',fg='#0049ad' )
            self.first_name.pack(side=LEFT, pady=(5,5))


            #2nd line
            self.line_frame2 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame2.pack(fill=X)

            self.dt = Label(self.line_frame2, text=self.date+'  |  '+self.time, width=32, bg='#f4f4f4', height='2', font=('verdana', 12),fg='#000000')
            self.dt.pack(side=LEFT,pady=20, padx=(0,0))


            self.line_frame01 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame01.pack(fill=X)

            self.re = Button(self.line_frame01, text='Click to creat the medicine bill', height=2, width=10, bg='#0048ad', fg='#FFFFFF', font=('verdana', 12), command=self.logout)
            self.re.pack(fill=X, pady=self.y+10, padx=(0,0))


           

            #1st line

            
            #1th line
            self.line_frame9 = Frame(self.parent_frame2, bg='white', relief='groove', bd=1,height='300')
            self.line_frame9.pack(fill=X,pady=self.y)

            
            #10th line
            self.line_frame10 = Frame(self.parent_frame2, bg='white')
            self.line_frame10.pack(fill=X)

            """
            for i in self.doctor_file:
                  if len(i)>0:
                        self.LIST.append(i)
            """
    

            #2th line
           
            self.line_frame13 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame13.pack(fill=X,pady=15)
            

            self.submit = Button(self.line_frame13, text='Submit', height=2, width=10, bg='#0048ad', fg='#FFFFFF', font=('verdana', 12), command=self.submit)
            self.submit.pack(fill=X, pady=self.y)

            self.line_frame0 = Frame(self.parent_frame2, bg='#FFFFFF')
            self.line_frame0.pack(fill=X)

            self.logout = Button(self.line_frame0, text='Logout', height=2, width=10, bg='#0048ad', fg='#FFFFFF', font=('verdana', 12), command=self.logout)
            self.logout.pack(fill=X, pady=self.y, padx=(0,0))


            #3th line

            #9th line
            #nextline

            #6th line

            #8th line

            #10thline

      def assign(self):
            pass

      
      def wow(self):
            pass

      
      def take_info(self):
            self.f_n=self.first_name_entry.get()
            self.l_n = self.last_name_entry.get()
            self.cnic_n = str(self.CNIC_entry.get())
            

      def generate_id(self):
            self.take_info()
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
            self.F = open('text/token.txt', 'a')            
            self.F.write(' '+str(self.token_no))
            print('done')

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
            
      def search_record(self):
            self.search_entry = self.search.get()
            
            self.medicine_text = open('text/medicine.txt', 'r')
            for i in self.medicine_text:
                  self.a=i.split('=')
                  if self.a[0]==self.search_entry:
                        self.tadaad=len(self.a)-1
                        for i in self.a[1:]:
                              b=i.split('  ')
                              print(b)
                              
                        print(self.DICT)
                  else:
                        tkm.showinfo('Error', 'Given ID is not found in our record')
                  

            """
            if self.search_entry in self.ids:
                  pass
                                 
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
                  
            else:
                  tkm.showinfo(message='Given ID not found in our record')

            self.search.delete(0,'end')
            """

            
      def new_add(self, h):
            pass
            
      def assign_appointment(self):
            pass
      
      def get_all_data(self):
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
            if len(self.username.get())!=0 and self.token_en.get():
                  self.medicine_dict[self.username.get()]=int(self.token_en.get())
                                                
            self.header.destroy()
            self.parent_frame.destroy()
            self.parent_frame2.destroy()
            self.mmain = doctor_form(self.main, 'DR-MuSa59000')
            self.mmain.left_column()
            self.mmain.right_column()
            
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
      main = patient_bill(root, 'PH-EiHa96663')
      main.left_column()
      main.right_column()
      root.mainloop()


