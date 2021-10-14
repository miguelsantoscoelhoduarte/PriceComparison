import json

# Class for Product
class Product:
    # Product Name
    __name = None
    # Product Price
    __price = None

    # Constructor
    def __init__(self, name, price, shop):
        self.__name = name
        self.__price = price
        self.__shop = shop

    def printProductInfo(self):
        print("-> Name:", self.__name)
        print("   Price:", self.__price)
        print(" ")

   # GET AND SET -> Name
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

   # GET AND SET -> Price
    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

   # GET AND SET -> Shop
    def setShop(self, shop):
        self.__shop = shop

    def setShop(self):
        return self.__shop
