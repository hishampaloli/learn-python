# 1. get duplicates from an array
array = [1, 2, 3, 3, 3, 4, 5, 3, 3, 6, 3, 5]
dup = []
for i, el in enumerate(array):
    if array.count(el) > 1:
        if el not in dup:
            dup.append(el)

print(34)


# 2. simple oop

class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1 Add nother Cat


class Hisham(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
simon = Simon('simon', 34)
sally = Sally('sally', 35)
hisham = Hisham('hisham', 42)
my_cats = [simon, sally, hisham]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)
# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()