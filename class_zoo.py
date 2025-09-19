class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says '{self.sound}'"

    def info(self):
        return (f"Name: {self.name}\n"
                f"Species: {self.species}\n"
                f"Age: {self.age}\n"
                f"Sound: {self.sound}")


lion = Animal(name="Simba", species="Lion", age=5, sound="Roar")


print(lion.info())
print(lion.make_sound())
