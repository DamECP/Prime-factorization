import gmpy2


def prime_factorization(user_input):

    def format_as_powers(factors: dict):
        print(" x ".join(f"{key}^{value}" for key, value in factors.items()))

    def format_as_multiplication(factors: dict):
        print(
            " x ".join(
                f"{key}" if value == 1 else f"{key} x {value}"
                for key, value in factors.items()
            )
        )

    result = {}

    if user_input <= 1:
        print("0 and 1 are too small.")

    elif gmpy2.is_prime(user_input):
        print(f"{user_input} is a prime number.")

    else:
        divisor = 2
        counter = 0
        while user_input > 1:
            if user_input % divisor == 0:
                user_input = user_input // divisor
                counter += 1
            else:
                if counter > 0:
                    result[int(divisor)] = counter
                    counter = 0
                divisor = gmpy2.next_prime(divisor)

        if counter > 0:
            result[int(divisor)] = counter

        format_as_multiplication(result)
        format_as_powers(result)


while True:
    user_input = input("Enter an integer value : ")
    if user_input.isdigit():
        user_input = int(user_input)
        prime_factorization(user_input)
