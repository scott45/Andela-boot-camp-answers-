# a function to generate prime numbers


prime_numbers = 0  # intitializing

def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True


for i in range(int(input("Input range: "))):
    if is_prime_number(i):
        prime_numbers += 1
        print(i)

print("there are " + str(prime_numbers) + " prime numbers.")  # similar to what you may call word count
