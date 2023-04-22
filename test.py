print("{}, {}, {}".format("a", "b", "c"))

print("{2}, {1}, {0}".format("a", "b", "c"))

print("Coordinates: {latitude}, {longtitude}".format(latitude = "122.334N", longtitude = "24.32W"))

#fstring
name = "Comel"
print(f"Look, it's {name}!")

def to_lowercase(name):
    return name.lower()

print(f"That model looks like {to_lowercase(name)}.")

#dictionary
tel ={'jack': 1234, 'bad': 5678}
tel['friend']= 1230

print(tel)

del tel['bad']

tel['good']=5678
print(tel)

#list
print(list(tel))
print(sorted(tel))

print('good' not in tel)
print('bad'  in tel)

#tupple
tup =(123, 456, "Bold")
print(tup)
print(tup[0])
print(tup[-1])

x, y, z =tup
print(x, y, z)

a = "gorilla"
b = "turtle"
a, b = b, a
print(a)
print(b)

#set
basket ={'apple', 'orange', 'apple', 'banana', 'pearl', 'banana'}
print(basket)

print('pearl'not in basket)

a = set('charmender')
b = set('charmelon')

print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

#pickle
import pickle
my_list = [1, 2, 3, "bucket", "for", "spamming"]
save_file = open("pickle_list", "wb")
pickle.dump(my_list, save_file)
save_file.close()
open_file = open("pickle_list", "rb")
pickled_rick = pickle.load(open_file)   
print(pickled_rick)

#class with methods

class Test:

    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.shop_markup = 1.5
        self.sales_profit = 0
        self.store_profit = 0
        self.sales_comission = None
        self.sell_price = 0

    def initial_inventory(self, car, quantity):
        self.inventory[car] = quantity
        self.sell_price = self.sales_comission * self.shop_markup
    
    def show_inventory(self):
        avail_inventory = []
        for car in self.inventory:
            if self.inventory[car] > 0:
                avail_inventory.append(car)
        return avail_inventory

    def indiv_sales_profit(self, car_cost):
        self.sales_comission = car_cost
        self.sales_profit += (self.sales_comission * self.shop_markup) - self.sales_comission

    def total_profit(self):
        self.store_profit += self.sales_profit
        return self.store_profit

    def sell_car(self, car_name):
        self.inventory[car_name] -= 1    

