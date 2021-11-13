import random

generate_10_integers = range(-100,100,20)
print(list(generate_10_integers))


random_positive_integer_no_smaller_than_50 = []
for i in range(0,10):
    random_positive_integer_no_smaller_than_50.append(random.randint(0,50))
        
print(random_positive_integer_no_smaller_than_50)