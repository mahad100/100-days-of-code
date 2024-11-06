import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#1
print(random.choice(friends))

#2
random_index = random.randint(0,4)
print(friends[random_index])

#3
friends[0] = 1
friends[1] = 2
friends[2] = 3
friends[3] = 4
friends[4] = 5
rand_person = random.randint(1,5)
if rand_person == 1:
    print("Alice")
elif rand_person == 2:
    print("Bob")
elif rand_person == 3:
    print("Charlie")
elif rand_person == 4:
    print("David")
elif rand_person == 5:
    print("Emanuel")
else:
    print("Null")
