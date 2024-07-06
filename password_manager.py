from cryptography.fernet import Fernet

'''
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb")as key_file:
        key_file.write(key)'''

def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")
key=load_key() + master_pwd.bytes


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, "| password:", passw)

def create():
    name = input("account name: ")
    pwd = input("password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to view an existing password or create new one (create/view) or press q to quit: ").lower()
    
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "create":
        create()
    else:
        print("invalid mode!")
