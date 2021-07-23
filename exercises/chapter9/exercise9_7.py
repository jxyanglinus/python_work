# 9-7 管理员

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


class Admin(User):
    """管理员用户"""
    def __init__(self, first_name, last_name, hobby):
        super(Admin, self).__init__(first_name, last_name, hobby)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """展示管理员所拥有的权限"""
        print("You are the administrator, you can do these things!")
        for privilege in self.privileges:
            print("\t - " + privilege)


admin = Admin("Tom", "Young", "swim")

admin.show_privileges()
