import random

print(random.randint(5, 20))  # line 1
# Line 1 gives a minimum of 5 and a maximum of 20
print(random.randrange(3, 10, 2))  # line 2
# The smallest number was a 3 and the largest was 7. Getting a 4 is impossible as it only delivers odd numbers.
print(random.uniform(2.5, 5.5))  # line 3
# Smallest number would be 3.8245523577896883 and the largest number was 4.533884762272804

print(random.randrange(1, 100))