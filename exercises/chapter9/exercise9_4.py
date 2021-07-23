# 9-4 就餐人数

class Restaurant:
    """一家餐馆"""
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐馆信息"""
        info = self.restaurant_name + ' [' + self.cuisine_type + ']'
        print(info)

    def open_restaurant(self):
        """餐馆正在营业!!!"""
        print(self.restaurant_name + " 正在营业.")

    def set_number_served(self, num: int):
        """设置就餐人数"""
        if num <= 0:
            pass
        else:
            print("本次有 " + str(num) + " 人就餐")
            self.increment_number_served(num)

    def increment_number_served(self, num: int):
        """增加就餐过的人数"""
        temp = self.number_served + num
        if temp <= self.number_served:
            pass
        else:
            self.number_served = temp
            print("增加 " + str(num) + " 个人， 共 " + str(self.number_served) + " 人")


restaurant = Restaurant("蜜雪冰城", "奶茶")

restaurant.describe_restaurant()
restaurant.open_restaurant()
print("-" * 30)

restaurant.set_number_served(5)
