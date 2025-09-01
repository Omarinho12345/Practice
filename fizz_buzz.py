#1) range 2) 3 and 5 fizz buzz  3) 3 e fizz 4) 5 e buzz basta 6) else num :
for num in range(1,101):
    if num % 3==0 and num %5==0:
        print("fizz buzz") 
    elif num % 3==0:
        print("fizz")
    elif num % 5==0:
        print("buzz")
    else:
        print(num)
