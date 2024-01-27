def registeryourself(name, password):
    # Create a string of the name and password into a single line
    usrinfostring = name.strip() + " " + password.strip() + "\n"
    # Check for duplicate record in the usersdata file
    with open("usersdata.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            name_array = line.split(" ")
            if name == name_array[0]:
                return False

    with open("usersdata.txt", "a") as f:
        f.write(usrinfostring)
        return True

def logintosystem(name, password):
    with open("usersdata.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            name_array = line.split(" ")
            if name == name_array[0].strip() and password == name_array[1].strip():
                return True
    return False

def main():
    print()
    print("MENU")
    print("1. Register an account")
    print("2. Log into the system")
    print("3. Exit")
    usrput = int(input("Please make a selection: "))
    print("Thank you!")
    return usrput

def pswrdinput():
    name = input("Please enter your username: ")
    password = getpass.getpass(prompt = "Please enter your password: ")
    passwordconf = getpass.getpass(prompt = "Please enter your password again: ")
    if password == passwordconf:
        name_password.append(name)
        name_password.append(password)
        return True
    else:
        return False

if __name__ == "__main__":
    import sys, getpass
    name_password = []
    count = 0        
    while True:
        usrput = main()
        if usrput == 1:
            while True:
                print()
                print("USERNAME & PASSWORD ENTRY")
                if pswrdinput():
                    print()
                    print("REGISTRATION")
                    if registeryourself(name_password[0],name_password[1]):
                        name_password = []
                        print("Registration complete!")
                        print()
                        break;
                    else:
                        name_password = []
                        print("Kindly pick another username. Duplicate found.")
                        print()
                        break;
                else:
                    count += 1
                    if count < 3:
                        print("Passwords do not match! Please enter your username and password once more!")
                        count = 0
                        continue;
                    else:
                        sys.exit("You have exceed three tries. Goodbye!")
        elif usrput == 2:
            print("LOGIN")
            name = input("Please enter your username: ")
            password = getpass.getpass(prompt = "Please enter your password: ")
            if logintosystem(name, password):
                print("You are logged in")
            else:
                print("Incorrect username or password")
        elif usrput == 3:
            sys.exit("Bye bye birdie!")