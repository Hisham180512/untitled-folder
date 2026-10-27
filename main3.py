class Parrot:

    #Class attribute
    species = "Bird"

    #Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #Instantinate the parrot class
        blu = Parrot("Blu", 10)
        woo = Parrot("Woo", 15)

        #acess the class attributes
    print("Blu is a {}" .format(blu.species))
    print ("Woo is also a {}" .format(woo.species))

    #Acess the instance attributes
print("{} is {} years old" .format(blu.name, blu.age))
print("{} is {} years old" .format(woo.name, woo.age))
        