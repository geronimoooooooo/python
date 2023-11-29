####G#### 
##C###D##
###P####

class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')
print('')

class Animal:
    def __init__(self, name):
        self.name = name
        print("This is Grandparent animal to " +name)
 
class Cat(Animal):
    def __init__(self, name):
        
        print("This is Parent Cat Class")
        super().__init__("Cat "+name)
   
    def call(self):
        print("call pets")    
 
class Dog(Animal):
    def __init__(self, name):
        print("This is Parent Dog class")
        super().__init__("Dog "+name) 
 
class Pet(Cat, Dog):
    def __init__(self, name):
        print('This is Child Pet Class');
        super().__init__(name)
 
d = Pet("MyPet")

#################################
Dog has 4 legs.
Dog can't swim.
Dog can't fly.
Dog is a warm-blooded animal.
Dog is an animal.

Bat can't swim.
Bat is a warm-blooded animal.
Bat is an animal.

This is Child Pet Class
This is Parent Cat Class
This is Parent Dog class
This is Grandparent animal to Dog Cat MyPet
