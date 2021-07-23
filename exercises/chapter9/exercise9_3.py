# 9-3 用户

class User:
    def __init__(self, first_name, last_name, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name.title() + ' ' + self.last_name.title()
        self.hobby = hobby

    def describe_user(self):
        info = "Name: " + self.full_name + "\tHobby: " + self.hobby
        print(info)

    def greet_user(self):
        msg = "Hey, " + self.full_name + "! Do you want to " + self.hobby + "?"
        print(msg)


Sam = User("Sam", "Green", "play soccer")
Jack = User("Jack", "Walker", "play basketball")
Tom = User("Tom", "Young", "program")

Sam.describe_user()
Sam.greet_user()

Jack.describe_user()
Jack.greet_user()

Tom.describe_user()
Tom.greet_user()
