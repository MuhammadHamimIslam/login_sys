import login
from sign_up import sign_up
from login import login, conn

def main():
    while True: 
        choice = input("Do you have any account?(y/n): ").strip().lower()
        if choice == "y":
            login()
        elif choice == "n":
            sign_up()
        elif choice == "q":
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()
    conn.close()