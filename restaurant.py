class restaurant:
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name}, one of the best {self.cuisine_type} in the city.")

    def open_restaurant(self):
        print(f"{self.name} is openning!")

sixteen = restaurant('sixteen','British cuisine')
kfc = restaurant('KFC','American cuisine')
macdownloads = restaurant('MacDownloads','American cuisine')

sixteen.describe_restaurant()
kfc.describe_restaurant()
macdownloads.describe_restaurant()
