import time
import random

class Crop:
    def __init__(self, name, growth_time, harvest_amount, selling_price):
        self.name = name
        self.growth_time = growth_time
        self.harvest_amount = harvest_amount
        self.selling_price = selling_price
        self.planted_time = 0
        self.harvested = False

class Animal:
    def __init__(self, name, growth_time, produce_item, produce_amount, selling_price):
        self.name = name
        self.growth_time = growth_time
        self.produce_item = produce_item
        self.produce_amount = produce_amount
        self.selling_price = selling_price
        self.birth_time = 0

class Facility:
    def __init__(self, name, cost, capacity):
        self.name = name
        self.cost = cost
        self.capacity = capacity

class IslandFarm:
    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.crops = []
        self.animals = []
        self.facilities = []

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# 在这里实现游戏的功能，包括种植作物、养殖动物、建设设施等

def play_game():
    island_name = "起源岛"
    farm = IslandFarm(island_name)

    crop_list = [
        Crop("小麦", 10, 5, 3),
        Crop("玉米", 15, 7, 4),
        Crop("西红柿", 20, 4, 5)
    ]

    animal_list = [
        Animal("鸡", 20, "鸡蛋", 2, 2),
        Animal("牛", 30, "牛奶", 1, 8),
        Animal("羊", 25, "羊毛", 1, 5)
    ]

    facility_list = [
        Facility("饲料厂", 200, 10),
        Facility("加工厂", 300, 8),
        Facility("市场", 500, 20)
    ]

    delay_print(f"欢迎来到{island_name}农场经营游戏！")
    delay_print("你将在这个游戏中经营自己的岛屿农场。")

    while True:
        show_status(farm)
        action = choose_action()

        if action == 1:
            show_status(farm)
        elif action == 2:
            plant_crop(farm, crop_list)
        elif action == 3:
            harvest_crops(farm)
        elif action == 4:
            raise_animal(farm, animal_list)
        elif action == 5:
            collect_products(farm)
        elif action == 6:
            build_facility(farm, facility_list)
        elif action == 7:
            delay_print(f"感谢你在{island_name}农场经营游戏中的努力，再见！")
            exit()

if __name__ == "__main__":
    play_game()
