import sqlite3
import time
from send_otp import send_otp, otp_code

conn = sqlite3.connect("data/user.db") # connect to database 
c = conn.cursor() # put the cursor 
c.execute("""CREATE TABLE IF NOT EXISTS users(fname TEXT,
     lname TEXT,
     Age INTEGER,
     Email TEXT,
     ID_No TEXT,
     Password TEXT,
     Date TEXT
)""") # create users table that will hold the data 

# function for taking valid input 
def take_inp(prompt):
    """
    run an infinite while loop.If user input is correct return the value by trimming whitespaces and break the loop
    """
    while True:
            data = input(prompt)
            if not data: 
                print("Enter a valid input!")
            else:
                return data
# function for saving user into database 
def save_user(fname, lname, age, email, password): 
    with conn:
        c.execute("INSERT INTO users VALUES(:fname, :lname, :age, :email, :id_no, :password, :date)", {"fname": fname, "lname": lname, "age": age, "email": email, "id_no": f"{fname}{lname}{age}", "password": password, "date": time.asctime()})
# sign up function    
def sign_up(): 
    fname = take_inp("Enter your first name: ")
    lname = take_inp("Enter your last name: ")
    age = int(take_inp("Enter your age: "))
    email = take_inp("Enter your email address: ")
    password = take_inp("Enter a strong password: ")
    send_otp(email)
    
    while True:
        otp_verify = take_inp("Enter the otp code that's sent to your email: ")
        if otp_verify == otp_code:
            break
        else:
            print("Otp didn't match!")
    save_user(fname, lname, age, email, password)
