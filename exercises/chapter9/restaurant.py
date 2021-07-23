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
