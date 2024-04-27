def generate_fibonacci(n):
    fibonacci_sequence = [0, 1, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

def find_in_fibonacci(number):
    fibonacci_sequence = [1, 1]
    while fibonacci_sequence[-1] < number:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    if number in fibonacci_sequence:
        return fibonacci_sequence.index(number) + 1
    else:
        return -1

def generate_lucas(n):
    lucas_sequence = [2, 1]
    for i in range(2, n):
        next_number = lucas_sequence[-1] + lucas_sequence[-2]
        lucas_sequence.append(next_number)
    return lucas_sequence

def find_in_lucas(number):
    lucas_sequence = [2, 1]
    while lucas_sequence[-1] < number:
        next_number = lucas_sequence[-1] + lucas_sequence[-2]
        lucas_sequence.append(next_number)
    if number in lucas_sequence:
        return lucas_sequence.index(number) + 1
    else:
        return -1

def generate_tribonacci(n):
    tribonacci_sequence = [0, 0, 1]
    for i in range(2, n):
        next_number = tribonacci_sequence[-1] + tribonacci_sequence[-2] + tribonacci_sequence[-3]
        tribonacci_sequence.append(next_number)
    return tribonacci_sequence

def find_in_tribonacci(number):
    tribonacci_sequence = [0, 1, 1]
    while tribonacci_sequence[-1] < number:
        next_number = tribonacci_sequence[-1] + tribonacci_sequence[-2] + tribonacci_sequence[-3]
        tribonacci_sequence.append(next_number)
    if number in tribonacci_sequence:
        return tribonacci_sequence.index(number) + 1
    else:
        return -1

def main():
    while True:
        print("1 - Fibonacci Sequence")
        print("2 - Lucas Sequence")
        print("3 - Tribonacci Sequence")
        print("4 - Exit")
        seq = input("Enter your choice: ")
        if seq == '1':
            print("1. Generate Fibonacci sequence")
            print("2. Find position of a number in Fibonacci sequence")
            choice = input("Enter your choice: ")

            if choice == "1":
                n = int(input("Enter the number of Fibonacci numbers to generate: "))
                sequence = generate_fibonacci(n)
                print("Fibonacci sequence:", sequence)
            elif choice == "2":
                number = int(input("Enter the number to find in Fibonacci sequence: "))
                position = find_in_fibonacci(number)
                if position != -1:
                    print(f"The position of {number} in Fibonacci sequence is {position}.")
                else:
                    print(f"{number} is not found in Fibonacci sequence.")
        elif seq == "2":
            print("1. Generate Lucas sequence")
            print("2. Find position of a number in Lucas sequence")
            choice = input("Enter your choice: ")

            if choice == "1":
                n = int(input("Enter the number of Lucas numbers to generate: "))
                sequence = generate_lucas(n)
                print("Lucas sequence:", sequence)
            elif choice == '2':
                number = int(input("Enter the number to find in Lucas sequence: "))
                position = find_in_lucas(number)
                if position != -1:
                    print(f"The position of {number} in Lucas sequence is {position}.")
                else:
                    print(f"{number} is not found in Lucas sequence.")
        elif seq == "3":
            print("1. Generate Tribonacci sequence")
            print("2. Find position of a number in Tribonacci sequence")
            choice = input("Enter your choice: ")

            if choice == '1':
                n = int(input("Enter the number of Tribonacci numbers to generate: "))
                sequence = generate_tribonacci(n)
                print("Tribonacci sequence:", sequence)
            elif choice == '2':
                number = int(input("Enter the number to find in Tribonacci sequence: "))
                position = find_in_tribonacci(number)
                if position != -1:
                    print(f"The position of {number} in Tribonacci sequence is {position}.")
                else:
                    print(f"{number} is not found in Tribonacci sequence.")
        elif seq == "4":
            print("Exiting...")
            break
        else:
            print("Please Enter a Valid Sequence")

if __name__ == "__main__":
    main()
