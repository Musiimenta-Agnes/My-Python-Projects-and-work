# Write a program that rints the ultiplication table (from 1 to 10) for numbers 1 to 6 using nested for loops.


print("The multipiation tables" ) 
def multiplication_table():
    for numbers in range (1,7):
        print(f'Multiplication table of {numbers}')
        for multiply in range(1,11):
            result = numbers * multiply
            print(f"{numbers} x {multiply} = {result}")

multiplication_table()
    





def adding_numbers():
    for i in range (1,20):
        if i % 2 == 0:
            print(f" {i}")
           
            for b in range(1,20):
                result = i * b
                print(f"The multiplication of these numbers is {i} x {b} = {result}")
                

adding_numbers()