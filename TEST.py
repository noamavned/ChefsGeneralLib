import ChefsGeneralLib as cgl

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def GetName(self) -> str:
        """Returns the name of the fruit

        Returns:
            str: Name of the fruit
        """
        return self.name
    def GetPrice(self):
        return self.price

obj1 = Fruit("Banana", 2.45)
obj2 = Fruit("Apple", 5)
# cgl.print_obj(obj1)

print(cgl.getWebsiteStatusCode("https://www.youtube.com/"))
print(cgl.generatePassword(5000))