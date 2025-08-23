class MessagingApp:
    def __init__(self):
        self.userid=''
        self.passwd=''
        self.signin=False
        self.menu()

    def menu(self):
        user_input=input('''Choose no for action:
                         1. one for sign up .
                         2. Two for sign in .
                         3. Type message.
                         4. sending message to friend.
                         5. Exit.

                         ->''')
        if user_input==1:
            pass
        elif user_input==2:
            pass
        elif user_input==3:
            pass
        elif user_input==4:
            pass
        elif user_input==5:
            pass
        else:
            print(" Choose valid Option.")

obj=MessagingApp()