class Chatbook:
    def __init__(self):
        self.userName = " "
        self.passWord = " "
        self.loggedIn = False
        self.menu()
    
    def menu(self):
        userInput = input("""Welcome to chatbook !
                            press 1 to signup
                            press 2 to signIn
                            press 3 to write a post
                            press 4 to message a friend
                            press any other key to exit""")
        if userInput == "1":
            pass
        elif userInput == "2":
            pass
        elif userInput == "3":
            pass
        elif userInput == "4":
            pass
        else :
            exit

obj = Chatbook()

