def song(name,age):
  
    print(f"happy birthday to you {name} bla bla")
    print(f"u are {age}")
    print("cake goes to though")
song("Brother" , "21")
song("steve " , "23")
song("joe" , "34")

def display(username,amount, date):
    print(f"hello {username}")
    print(f" the total of your bills is {amount}")
    print(f"you have time to pay untill {date}")
display("marco" , " 44 dollars" , "01/02")
display("John", "100 dollars" , "01/01") 

def add(x,y):
   z = x+y
   return z
def subtract(x ,y):
  z = x-y
  return z
def multiple(x,y):
 z = x * y
 return z
def divide(x , y):
  z = x/y
  return z
print(add( 2 , 1))
print(subtract(2 ,1))
print(multiple( 1 ,2 ))
print(divide(2 ,1))

def fullname(first, second):
  first = first.capitalize()
  second = second.capitalize()
  return first +" " + second
create_name = fullname ("omar" ,"223")
print(create_name)

