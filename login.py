import sqlite3
from sign_up import take_inp

conn = sqlite3.connect("data/user.db")
c = conn.cursor()

def check_user(id_no, password): 
    with  conn:
        c.execute("SELECT ID_No, Password FROM users WHERE ID_No = :id_no", {"id_no": id_no})
    ID_No, Password = c.fetchone()
    return ID_No == id_no and Password == password


def login(): 
    id_no = take_inp("Enter your id no: ")
    password = take_inp("Enter your password: ")
    if check_user(id_no, password): 
        print("login successful!")
    else: 
        print("Invalid email!")