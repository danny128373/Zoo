zoo = ('alligator', 'bee', 'camel', 'duck',
       'eagle', 'fox', 'horse', 'iguana', 'jaguar', 'kangaroo')
print(zoo.index('bee'))

animal_to_find = 'horse'
found_animal = False

for animal in zoo:
    if animal == animal_to_find:
        found_animal = True
print(found_animal)

(firstAnimal, secondAnimal, thirdAnimal, fourthAnimal, fifthAnimal,
 sixthAnimal, seventhAnimal, eighthAnimal, ninethAnimal, tenthAnimal) = zoo
print(firstAnimal)
print(secondAnimal)

zoo = list(zoo)
print(zoo)
