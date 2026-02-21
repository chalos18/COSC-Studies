def fizz_buzz(number : int):
    if number % 3 == 0 and number % 5 == 0 :
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
        
# print(fizz_buzz(15))

for i in range(1, 101):
    num = ""
    if i % 3 == 0 and i % 5 == 0 :
        num += "FizzBuzz " + str(i)
    elif i % 3 == 0:
        num += "Fizz " + str(i)
    elif i % 5 == 0:
        num += "Buzz " + str(i)
    else:
        num += str(i)
    
    print(num)
        
    

