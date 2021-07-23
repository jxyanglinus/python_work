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
