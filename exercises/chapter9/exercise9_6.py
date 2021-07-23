# 9-6 冰淇淋小店

class Restaurant:
    """一家餐馆"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        """描述餐馆信息"""
        info = self.restaurant_name + ' [' + self.cuisine_type + ']'
        print(info)

    def open_restaurant(self):
        """餐馆正在营业!!!"""
        print(self.restaurant_name + " 正在营业.")


class IceCreamStand(Restaurant):
    """模拟一家冰淇淋小店"""
    def __init__(self, restaurant_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = ["香草", "草莓", "香蕉", "奥利奥", "芒果"]

    def show_flavors(self):
        """显示所提供的冰淇淋口味"""
        print("我们为您提供了如下口味的冰淇淋:")
        for ice_cream in self.flavors:
            print("\t - " + ice_cream + "冰淇淋")


ice_cream_stand = IceCreamStand("IceHouse", "甜点")

ice_cream_stand.show_flavors()
