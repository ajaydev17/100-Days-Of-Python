def prime_checker(number):
    is_prime = True

    for i in range(2, number // 2):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number!!")
    else:
        print(f"{number} is not a prime number!!")


num = int(input("Enter your number: "))
prime_checker(number=num)

# 14645458654548465864564565456409 - breaks the above code
