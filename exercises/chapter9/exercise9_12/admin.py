from user import User


class Admin(User):
    """管理员用户"""
    def __init__(self, first_name, last_name, hobby):
        super().__init__(first_name, last_name, hobby)
        self.privileges = Privileges()


class Privileges:
    """管理员用户的权限"""
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """展示管理员所拥有的权限"""
        print("You are the administrator, you can do these things!")
        for privilege in self.privileges:
            print("\t - " + privilege)
