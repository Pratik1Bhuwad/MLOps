class MessagingApp:
    def __init__(self):
        self.username=''
        self.passwd=''
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input('''Choose no for action:
                         1. one for sign up .
                         2. Two for sign in .
                         3. Type message.
                         4. sending message to friend.
                         5. Exit.

                         ->''')
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.Msg()
        elif user_input=="4":
            self.SendMsg()
        elif user_input=="5":
            exit()
        else:
            print(" Choose valid Option.")
            self.menu()

        
    def signup(self):
        email=input("Enter your email-> ")
        password = input("Enter your password-> ")
        self.username=email
        self.passwd=password
        self.loggedin=True
        print("Signup successful!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.passwd=='':
            print("No user found. Please sign up first.")
            
        else:
            uname=input("Enter your email-> ")
            passward=input("Enter your password-> ")
            if self.username==uname and self.passwd==passward:
                print("Sign in successful!")
                self.loggedin=True
            else:
                print("Plz enter correct creadentials...")
        print("\n")
        self.menu()

    def Msg(self):
        if self.loggedin==True:
            msg=input("Enter Your Message->")
        else:
            print("You need to first signin...")
        print("\n")
        self.menu()

    def SendMsg(self):
        if self.loggedin==True:
            frnd=input("Whom to send the msg? ->")
            print(f"Your msg has been send to {frnd}")
        else:
            print("You need to signin first... ")
        print("\n")
        self.menu()

obj=MessagingApp()