class Parrot:
    #instance attributes
    def __init__(self , name, age):
        self.name = name
        self.age = age

        #instance methood
        def sing(self, song):
            return "{} sings {}" .format(self.name, song)
        def dance(self):
            return "{} is now dancing" .format(self.name)
        #instantitate the object

        blu = Parrot("Blu", 10)
        #call our instance methoods
        print(blu.sing("Happy"))
        print(blu.dance())
 