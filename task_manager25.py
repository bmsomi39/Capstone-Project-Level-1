from datetime import date

def mainmenu(a):
 a=1
 while a>0:  
  print(username)   
  if username == "admin":
        print("Please select one of the following options:")
        print("r - register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("gr - generate reports")
        print("s - Display Statistics")      
        print("e-exit")
        option=input("")
  
  else:
        print("Please select one of the following options:")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")      
        print("e-exit") 
        option=input("")
        
  
  if option==   "r": 
      reg_user()
  if option==   "a":
      add_task()   
  if option==   "va":
      view_all()
  if option== "gr":
      generate_reports(user_current)
  if option==   "vm":
      view_mine()
  if option == "ds":
        users_reg = []
        with open('user25.txt','r+') as file:
           c=0
           
           for line in file:
                c+=1
    
                users_reg.append(str(line))

                tasks=[]
                d=0
                b=False
                
                with open('tasks25.txt','r+') as file:
                        for line in file:  
                              d+=1
                              tasks.append(str(line))
                             
   


        print("Total number of tasks:")
        print(d)
        print("Total number of users:")
        print(c)
  if option == "e":
   print("Exit")
   a-=1      
   exit()






















   
  #----------------------------------------------------------------------------------------------------------
def generate_reports(user_current):
    
        Total_incomplete_overdue=0
        with open('tasks25.txt', 'r+') as f:
         total_tasks=0
         contents=""
         completed_tasks=0
         uncompleted_tasks=0
         for index,line in enumerate(f):
           
           total_tasks+=1
           contents+=line
           line = line.split (',')
           chars=0
           
           b=False  
           name =line[chars]
           if user_current == name:
               b=True

           chars+=5
           comp=line[chars]
           chars-=5
           comp.strip()
           comp=comp[1:]
           if comp[-1]=="\n":
            comp=comp[:-1]
           l=0
           l=len(comp)
           bcomplete=False
           
           if comp =="Yes":
               completed_tasks+=1
               bcomplete=True              
           if comp =="No":
               uncompleted_tasks+=1
           chars+=4
           Due_due=""
           Month=""
           Due_date=line[chars]
           import datetime
           Due_date= Due_date.split(" ")
           if Due_date[-1]=="\n":
               Due_date[:-1]
           Month=Due_date[2]
           Date=Due_date[1]
           Year=Due_date[3]
           
           Month_num=0
           if Month=="Jan":
               Month_num=1
           elif Month=="Feb":
               Month_num=2
           elif Month=="Mar":
               Month_num=3
           elif Month=="Apr":
               Month_num=4
           elif Month=="May":
               Month_num=5
           elif Month=="Jun":
               Month_num=6
           elif Month=="Jul":
               Month_num=7
           elif Month=="Aug":
               Month_num=8
           elif Month=="Sep":
               Month_num=9
           elif Month=="Oct":
               Month_num=10
           elif Month=="Nov":
               Month_num=11
           elif Month=="Dec":
               Month_num=12
           CurrentDate = datetime.datetime.now()

           overdue=0
           ExpectedDate = str(Date)+"/"+str(Month_num)+"/"+str(Year)
           ExpectedDate = datetime.datetime.strptime(ExpectedDate, "%d/%m/%Y")
           
           boverdue=False
           if CurrentDate > ExpectedDate:
                boverdue=True
                overdue+=1
               
           if (boverdue) and (bcomplete==False):
               Total_incomplete_overdue+=1
               
               

               










        
        
        Perc_incomplete = str(round(uncompleted_tasks*100/total_tasks)) +"%"
        Perc_overdue= str(round(Total_incomplete_overdue*100/total_tasks)) +"%"
        print("Total tasks generated using task_manager.py :",total_tasks)  
        print("Number of completed tasks: ", completed_tasks)
        print("Number of uncompleted tasks: ", uncompleted_tasks)
        print("Total incomplete & overdue tasks:",Total_incomplete_overdue)   
        print("Percentage of tasks that are overdue: ", Perc_overdue)
        print("Percentage of tasks that are incomplete: ", Perc_incomplete)
                         #then post to task_overview.txt
        #---------------------------------------------------------------------------------
        
        with open('user25.txt', 'r+') as f:
         print()
         total_users=0
         list_users=[]
         for index,line in enumerate(f):
             total_users+=1
             list_users.append(line) 
         print("Total number of users registered: ",total_users)
         print("Total number of tasks generated:",total_tasks)
         user_complete=0
         user_incomplete=0
         if b :
           chars+=5
           comp=line[chars]
           comp.strip()
           comp=comp[1:]
           if comp[-1]=="\n":
            comp=comp[:-1]
           l=0
           l=len(comp)
           

           if comp =="Yes":
               user_complete+=1
               
           if comp =="No":
               user_incomplete=1
                        
         for  idex,val in enumerate(list_users) :
                 val = val.split(",")
                 curr_name=val[0]
                 bcomplete=False
                 print(str(idex+1),":",curr_name)
                 with open('tasks25.txt', 'r+') as f:
                     contents=""                                                                            #we need
                     Total_num_tasks=0           #assigned to user
                     completed_tasks=0
                     incomplete_tasks=0
                     Total_incomplete_overdue=0                     
                     for index,line in enumerate(f):
                        chars=0
                        contents=line
                        line=line.split(",")
                        name_=line[chars]
                        
                        if curr_name==name_:
                         Total_num_tasks+=1
                         chars=0
           
                         b=False           
                             
                              
                                    
                         name =line[chars]
                         b=True
                         chars+=5
                         comp=line[chars]
                         chars-=5
                         comp.strip()
                         comp=comp[1:]
                         if comp[-1]=="\n":
                                comp=comp[:-1]
                                l=0
                                l=len(comp)
                                bcomplete=False
                         
                         if comp=="Yes":
                          completed_tasks+=1
                          bcomplete=True
                         else:
                             incomplete_tasks+=1
                         chars+=4
                         Due_due=""
                         Month=""
                         Due_date=line[chars]
                         #print(Due_date)
                         import datetime
                         Due_date= Due_date.split(" ")
                         if Due_date[-1]=="\n":
                               Due_date[:-1]
                         Month=Due_date[2]
                         Date=Due_date[1]
                         Year=Due_date[3]
                         #print("Date",Date)
                         #print("Month",Month)
                         #print("Year",Year)
                         Month_num=0
                         if Month=="Jan":
                                   Month_num=1
                         elif Month=="Feb":
                                   Month_num=2
                         elif Month=="Mar":
                                   Month_num=3
                         elif Month=="Apr":
                                   Month_num=4
                         elif Month=="May":
                                 Month_num=5
                         elif Month=="Jun":
                                   Month_num=6
                         elif Month=="Jul":
                                   Month_num=7
                         elif Month=="Aug":
                                   Month_num=8
                         elif Month=="Sep":
                                   Month_num=9
                         elif Month=="Oct":
                                   Month_num=10
                         elif Month=="Nov":
                                   Month_num=11
                         elif Month=="Dec":
                                   Month_num=12
                         Curr_Date = datetime.datetime.now()
                         #print("month"+str(Month_num))
                                                            
                         overdue=0
                         DUEDate = str(Date)+"/"+str(Month_num)+"/"+str(Year)
                         DUEDate = datetime.datetime.strptime(DUEDate, "%d/%m/%Y")
                         #print("Curr date",Curr_Date)
                         #print("DUEDate",DUEDate)
                               
           
                        boverdue=False
                        if Curr_Date > DUEDate :
                                    boverdue=True
                                    overdue+=1
                        #print("CURR",curr_name)
                        #print("NAME",name_)
                        if (boverdue) and (bcomplete==False) and curr_name==name_:
                                   Total_incomplete_overdue+=1
                                   #print("Total_incomplete_overdue",Total_incomplete_overdue)

                             
                     Perc_user_incomplete_overdue= str(round(Total_incomplete_overdue*100/Total_num_tasks)) +"%"
                     Perc_user_tasks = str(round(Total_num_tasks*100/total_tasks)) +"%"
                     Perc_user_tasks_completed = str(round(completed_tasks*100/Total_num_tasks)) +"%"
                     Perc_user_tasks_incomplete = str(round(incomplete_tasks*100/Total_num_tasks)) +"%"
                     
                     
                     print("Total number of tasks assigned to "+curr_name+" : ",Total_num_tasks)
                     print("Percentage of number of tasks assigned to "+curr_name+" : ", Perc_user_tasks)
                     print("Percentage of tasks that "+curr_name+" has completed: ",Perc_user_tasks_completed )
                     print("Percentage of tasks that "+curr_name+" has not completed: ",Perc_user_tasks_incomplete)
                     print("Percentage of tasks that "+curr_name+" has not completed and are overdue: ",Perc_user_incomplete_overdue)

         users_reg = []
         with open('user25.txt','r+') as file:
                           c=0
                           
                           for line in file:
                                c+=1
    
                                users_reg.append(str(line))

                                tasks=[]
                                d=0
                                b=False
                
                                with open('tasks25.txt','r+') as file:
                                        for line in file:  
                                              d+=1
                                              tasks.append(str(line))
                             
   
         print("Total number of tasks:")
         print(d)
         print("Total number of users:")
         print(c)
                 
                                            
                 
                 
                 
                 
                    
                
                 
        print()
        #post to user_overview
  #----------------------------------------------------------------------------------------------------------








































  
def search_string_in_file(string_to_search):
     line_number=0
     list_of_results=[]
     with open('tasks25.txt','r+') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
               list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
     return list_of_results


  #----------------------------------------------------------------------------------------------------------

def reg_user():
   bconfirm = False
   users_reg = []
   usernamE = str(input("Enter new username: "))
   password = str(input("Enter new password: "))
   confirm_pass=str(input("Confirm password: "))
   if password==confirm_pass:
     bconfirm=True
      
   while bconfirm !=True:
         usernamE = str(input("Enter new username: "))
         password = str(input("Enter new password: "))
         confirm_pass=str(input("Confirm password: ")) 
         if password == confirm_pass:
            bconfirm=True
   full_user_pass= usernamE + ", " + password
   
   users_reg_txt_format=[]
   bconfirm=False
   
  
   with open('user25.txt','r+') as file:
      c=0
      for line in file:
        c+=1
        users_reg_txt_format.append(str(line))
        users_reg.append(str(line))#
      c+=1
      
            
      while full_user_pass in users_reg:
           print("The user you are trying to register already exists. Try again")
           bconfirm=False
              
           while bconfirm !=True:
             usernamE = str(input("Enter new username: "))
             password = str(input("Enter new password: "))
             confirm_pass=str(input("Confirm password: ")) 
             if password == confirm_pass:
                bconfirm=True
           full_user_pass= usernamE + ", " + password
           
        


            
      users_reg.append(str(full_user_pass))
      users_reg_txt_format.append("\n"+str(full_user_pass))
      print("Users:")  
      for i in users_reg:
          with open('user25.txt','w') as file:
              for i in range(0,c):
                  file.write(str(users_reg_txt_format[i]))
      

  #----------------------------------------------------------------------------------------------------------


def add_task():      
       tasks = []
       due_date=" "
       Username = str(input("Enter new username: "))
       task_title = str(input("Enter task title: "))
       task_description=str(input("task d "))
       due_date+=str(input("Enter due date: "))


   
       today = date.today()
       current_date= today.strftime("%d/%b/%Y")
   
   
       completed_or_not= "No"
       full_user_task= Username + ", " + task_title + ", " +task_description +", "+current_date +","+due_date +", "+ completed_or_not 
       
       print(full_user_task)
       with open('tasks25.txt','r+') as file:
            c=0
            for line in file:
             c+=1
             tasks.append(str(line))
            c+=1
            tasks.append("\n" + str(full_user_task))
            with open('tasks25.txt','w') as file:
                   for i in range(0,c):
                      file.write(str(tasks[i]))

  #----------------------------------------------------------------------------------------------------------
def view_mine():                  
   contents=""
   mytasks =[]
   
           
   toprint="" 
   print(user_current+ "'s tasks")  
   with open('tasks25.txt', 'r+') as f:
       
        
    Corres_num=0
    for index,line in enumerate(f):
       
      contents = contents + line
      line = line.split (',')
      count = 0
      #for chars in line:
      chars=0
      global task_count
      task_count=0
      name =line[chars]
      
            
      if user_current == name:
           Corres_num+=1
            
           task_count+1
           mytasks.append(line)     
           name=""
           task=""
           taskdesc=""
           currdate=""
           duedate=""
           completed=""
           bcurrdate=True
           bduedate=True
           bcompleted=True
           bname=True
           btask=True
           btaskdesc  =True

           print("Task no: "+ str(Corres_num))
      
           chars=0        
           while (bname!=False)and(btask!=False) and(btaskdesc!=False)and chars <6 and (bcurrdate!=False)and (bduedate !=False) and(bcompleted!=False):
      
              name =line[chars]   
          
              chars+=1
              bname=False
          
              task=line[chars]
              chars+=1
              btask=False
              print("Task: "+task)

              taskdesc=line[chars]
              chars+=1
              btaskdesc=False
              print("Task description: " +taskdesc)
       
              currdate=line[chars]
              chars+=1
              bcurrdate=False
              print("Date issued: " + currdate)

          

              duedate=line[chars]
              chars+=1
              bduedate=False
              print("Due date: " +duedate)

          

              completed=line[chars]
              chars+=1
              bcompleted=False
              print("Complete: "+completed)
          

              chars+=1

################################
   
##########################################################
   strnum=""
   CHECK=""
      
   with open('tasks25.txt', 'r+') as f:
    print("**")
    for idx,val in enumerate(range(1,Corres_num+1)):
      strnum+=str(idx+1) + ","
    matched_lines = search_string_in_file( user_current)
    #print('Total Matched lines : ', len(matched_lines))
    for elem in matched_lines: 
     print('Line Number = ', elem[0], ' :: Line = ', elem[1])
     print()
    nuum= int(input("Choose a task number to edit:"))
        
    if nuum!=-1:
     nuum-=1


     INDEX_IN_TXT_TO_EDIT=0  
    
     #print("##########")
     nuum_index_in_txt=0
     matched_lines = search_string_in_file( user_current)
     #print('Total Matched lines : ', len(matched_lines))
     for idx,elem in enumerate(matched_lines):
        #print("idx:",idx)
       # print("chosen:",nuum)
        while idx==nuum:
        #nuum_index_in_txt=int(elem[0])
         INDEX_IN_TXT_TO_EDIT=int(elem[0]) -1 
         #print('Line Number = ', elem[0], ' :: Line = ', elem[1])
        # print("#########################")
         idx-=1
    
    else:
        mainmenu()
        
    #############################################################################
       
    with open('tasks25.txt', 'r+') as f:
     contents=""   
     for index,line in enumerate(f):
      
      if index==INDEX_IN_TXT_TO_EDIT:
          # print("index",index)
           #print("INDEX EDIT",INDEX_IN_TXT_TO_EDIT)
           
           contents+=line
           line = line.split (',')
           chars=0
           chars+=5
           comp=line[chars]
           comp.strip()
           print("Comp: ",comp)
           chars-=5

    
    
    ############################################################################
    
    if comp.strip() =="No":
        print("Select the option you would like to edit from the following:")
        print("1 - To change user assigned to task")
        print("2 - To change due date")
        print("3 - To change both both user assigned to task and due date")
        num_option=int(input("Option choice number: "))
        b1=False
        b2=False
        b3=False
        new_username=""
        new_due_date=""
        if num_option == 1:
                b1=True
                new_username=input("Enter the new user name assign to this task:")   
        if num_option == 2:
                b2=True
                new_due_date=input("Enter the new due date for this task:")
        if num_option == 3:
                b3=True
                new_username=input("Enter the new user name assign to this task:")
                new_due_date=input("Enter the new due date for this task:")
        
               #to check no and change username assign and due date
        
        with open('tasks25.txt', 'r+') as f:
         contents=""   
         for index,line in enumerate(f):
         
          if index==INDEX_IN_TXT_TO_EDIT:
          # print("index",index)
           #print("INDEX EDIT",INDEX_IN_TXT_TO_EDIT)
           
           contents+=line
           line = line.split (',')
           count = 0
  
           chars=0
      
           task_count=0

           chars+=5
           comp=line[chars]
           comp.strip()
           print("Comp: ",comp)
           chars-=5
           
           name =line[chars]
            
           task_count+1
           mytasks.append(line)     
           name=""
           task=""
           taskdesc=""
           currdate=""
           duedate=""
           completed=""
           bcurrdate=True
           bduedate=True
           bcompleted=True
           bname=True
           btask=True
           btaskdesc  =True
           new_full_task=""

           
           chars=0        
           while (bname!=False)and(btask!=False) and(btaskdesc!=False)and chars <6 and (bcurrdate!=False)and (bduedate !=False) and(bcompleted!=False):
              
              if  ( ((b1 == True) or (b3 == True )) and ( index == INDEX_IN_TXT_TO_EDIT) ):
                  name=new_username
                  chars+=1
                  bname=False
              
              else:
                  bother1 =true
                  name =line[chars]   
                  chars+=1
                  bname=False
              print("Name: "+name)    
              new_full_task+=name +","
              
             # print("Full change: ",new_full_task)
              
              
              task=line[chars]
              chars+=1
              btask=False
             # print("Task: "+task)
              new_full_task+=task +","
              #print("Full change: ",new_full_task)

              taskdesc=line[chars]
              chars+=1
              btaskdesc=False
              print("Task description: " +taskdesc)
              new_full_task+=taskdesc +","
            #  print("Full change: ",new_full_task)
       
              currdate=line[chars]
              chars+=1
              bcurrdate=False
              print("Date issued: " + currdate)
              new_full_task+=currdate+","
             # print("Full change: ",new_full_task)

          
              if  (b2 == True or b3 == True ) and ( index == INDEX_IN_TXT_TO_EDIT):
                  duedate=new_due_date
                  chars+=1
                  bname=False
              else:
                  duedate=line[chars]
                  chars+=1
                  bduedate=False
              print("Due date: " +duedate)
              new_full_task+=duedate
              new_full_task+=","
            #  print("Full change: ",new_full_task)
              
              
              
              completed=line[chars]
              chars+=1
              bcompleted=False
              #print("Complete: "+completed)
              new_full_task+=completed

              #print("Full change: ",new_full_task)
          

              chars+=1

              if completed.strip() == "No":
                  a_file = open("tasks25.txt", "r")
                  list_of_lines = a_file.readlines()
                  list_of_lines[INDEX_IN_TXT_TO_EDIT] = new_full_task
                
                  a_file = open("tasks25.txt", "w")
                  a_file.writelines(list_of_lines)
                  a_file.close()
                
              
                  
                  
    else:
        print("This task has already been completed. Therefore it cannot be changed.")
             





      ################################################################################change
      


    
    




















    
 

######################################################################################

def view_all():      
   contents=""
   mytasks =[]
   Total_number_of_tasks=0 
      
       
   with open('tasks25.txt', 'r+') as f: 
    for line in f:
       
      contents = contents + line
      line = line.split (',')
      count = 0
      mytasks.append(line)                        
      name=""
      task=""
      taskdesc=""
      currdate=""
      duedate=""
      completed=""
      bcurrdate=True
      bduedate=True
      bcompleted=True
      bname=True
      btask=True
      btaskdesc  =True
      chars=0 
      while (bname!=False)and(btask!=False) and(btaskdesc!=False)and chars <6 and (bcurrdate!=False)and (bduedate !=False) and(bcompleted!=False):
          Total_number_of_tasks+=1
          name =line[chars]   
          print(name + "'s tasks")
          chars+=1
          bname=False
          
          task=line[chars]
          chars+=1
          btask=False
          print("Task: "+task)

          taskdesc=line[chars]
          chars+=1
          btaskdesc=False
          print("Task description: " +taskdesc)
       
          currdate=line[chars]
          chars+=1
          bcurrdate=False
          print("Date issued: " + currdate)

          

          duedate=line[chars]
          chars+=1
          bduedate=False
          print("Due date: " +duedate)

          

          completed=line[chars]
          chars+=1
          bcompleted=False
          print("Completed: "+completed)
          
          

          chars+=1

#######################################################################################                  

                  

username=""
password=""
user=""
passw=""
buser=False
bpass=False
numu=1
l=0
bu=False
bp=False
a=""
users_registered= 0
user_current="" 
global Total_number_of_users
global Total_number_of_tasks
Total_number_of_users=0
Total_number_of_tasks=0




################################################################ LOGIN



################################################################ Login function begin
def checkvaliduser(username,password):
      
  users_reg=[]
  contents=""
  myusers=[]
  with open('user25.txt','rt') as file:
      
                                                                                    
    for line in file:
                                    
      contents = contents + line
      line = line.split (',')
      count = 0
      #
      users_reg.append(str(line))
      
      
      myusers.append(line)
       
                              
      name=""
      passw=""
      
    
  
      bname=True
      bpass=True
      checkcount=0
      bu=False
      bp=False
      bboth=0
      #for chars in line:
      chars=0
            
      while (bname!=False)and(bpass!=False) :
          
          name =line[chars]   
          
          chars+=1
          bname=False
          #print("user "+name)
          if username==name:
            bu=True
          #print("bu"+str(bu))
              
          passw=line[chars]
          passw.strip()
          passw=passw[1:]
          chars+=1
          #print("pass: "+passw)
          
          
          a=passw
          if passw[-1] == '\n':
             a=passw[0:-1]
             l=len(a)
             lastchar=a[-1]
            
             
          
          
          bpass=True
          if password==a:
            bp=True
          #print("bp"+str(bp))
          if bp and bu:
            bboth=+1
             
          #print("bboth" + str(bboth))           
          if bboth>0:
             return True
    if bboth==0:
        return False
          
########################################################### Login function end
blogin=False                
while blogin !=True:
  username=str(input("Enter username"))
  user_current=username
  password=str(input("Enter password"))
  b=checkvaliduser(username,password)
  if b==True:
   print("Login Successful!")   
   blogin=True
  else:
    print("User does not exist, try again.")
          
############################################################LOGIN   END

############################################################ MAIN MENU BEGIN  
option=""
a=1
while a>0:
 print("")
 numu=0

 if blogin :
  mainmenu(a)
  

  













     
      

      
