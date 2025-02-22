import gmpy2


def prime_factorization(user_input):

    answer_list = []

    if gmpy2.is_prime(user_input):
        return f"{user_input} is a prime number."

    if user_input <= 1:
        return "0 and 1 are too small."

    # deal with 2 first
    while user_input % 2 == 0:
        answer_list.append("2")
        user_input //= 2

    divisor = 3
    while user_input != 1:
        if user_input % divisor == 0:
            answer_list.append(str(divisor))
            user_input = user_input // divisor
        else:
            divisor = gmpy2.next_prime(divisor)

    # print as a line of multiplications
    return " x ".join(answer_list)


while True:
    user_input = input("Enter an integer value : ")
    if user_input.isdigit():
        user_input = int(user_input)
        print(prime_factorization(user_input))
