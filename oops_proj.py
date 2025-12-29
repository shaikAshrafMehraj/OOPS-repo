class Chatbook:
    def __init__(self):
        self.userName = " "
        self.passWord = " "
        self.loggedIn = False
        self.menu()
    
    def menu(self):
        userInput = input("""Welcome to chatbook !
                            1. press 1 to signup
                            2. press 2 to signIn
                            3. press 3 to write a post
                            4. press 4 to message a friend
                            5. press any other key to exit""")
        if userInput == "1":
            self.signUp()
        elif userInput == "2":
            self.signIn()
        elif userInput == "3":
            pass
        elif userInput == "4":
            pass
        else :
            exit()

    def signUp(self):
        email = input("Enter the email here :")
        pwd = input("Enter the pwd here :")
        self.userName = email
        self.passWord = pwd
        print("You have signed successfully ..")
        print("\n")
        self.menu()

    def signIn(self):
        if self.userName == " " and self.passWord == " ":
            print("Please signUP first then signIn later ")
        else :
            uname = input("Enter the email/ username here :")
            pwd = input("Enter the email/ username here :")
            if self.userName == uname and self.passWord == pwd:
                print("you are signed In sucessfully !!")
                self.loggedIn = True
            else :
                print("Please input correct credentials..")
        print("\n")
        self.menu()

        
obj = Chatbook()

