




# ENTER USER

## It helps the user to log into the system.
## The user may enter incorrectly 3 times in the login,or user may log again after 1 hour.
## With the forgot password option, mail will log in again with the outgoing confirmation code.

import time

## Data stored in the system
user_name="CLARA"
user_password="cl2554"
mail_adress="drona@gmail.com"
attempt=0     
max_attempts=0
wait_time=3600 # 1 hour=3600 second

while True:
    miss=input("If you have forgotten your password, enter the value v: ")

    if (miss!="v"):
    
        user_nm_enter=str(input("Please nter the user name: "))
        user_psw_enter=input("Please enter the user password: ")
    
        if ((user_nm_enter=="")and(user_psw_enter=="")):
            print("Enter your information")
        elif ((user_nm_enter=="")and(user_psw_enter!="")):
            print("Enter the user name")
        elif ((user_nm_enter!="")and(user_psw_enter=="")):
            print("Enter the user password")
        else:
            
            if ((user_name==user_nm_enter) and (user_password==user_psw_enter)):
                print("Logging in to the system...")
                print("Welcome {}".format(user_name))
                attempt=0
                break     
            elif ((user_name!=user_nm_enter)and (user_password==user_psw_enter)):
                print("The user name is incorrect please try again...")
            elif ((user_name==user_nm_enter)and (user_password!=user_psw_enter)):
                print("Your password is incorrect please try again...")
            else:
                print("Your user name and user password are incorrect")
                print("Try again...")          
                attempt=attempt+1
                if (attempt>max_attempts):
                    print("Too many false attempts...")
                    print("Try again after 1 hour.")
                    time.sleep(wait_time)
                    attempt=0   
    else:
        adress=input("Enter the email address: ")
        if (adress==mail_adress):        
            print("Sending an email...")
            print("A new password was sent by mail. Please check")
            break
        else:
            print("Enter the email address registered in the system.")
            
            
 
    