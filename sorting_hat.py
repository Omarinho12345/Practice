Q1 = int(input("Do like Dawn or Dusk? 1= Dawn , 2= Dusk.  "))
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
if Q1 == 1:
   Gryffindor =  Gryffindor +1
   Ravenclaw = Ravenclaw +1
elif Q1 ==2: 
  Hufflepuff  = Hufflepuff +2 
  Slytherin = Slytherin +2

else:
   print("Wrong input.")

Q2 = int(input("When I’m dead, I want people to remember me as: 1) The Good, 2) The Great, 3) The Wise, 4) The Bold: "))
if Q2 == 1:
   Hufflepuff = Hufflepuff +2
elif Q2 ==2:
   Slytherin = Slytherin +2
elif Q2 ==3:
   Ravenclaw =Ravenclaw +2
elif Q2 ==4:
   Gryffindor = Gryffindor  +2
else:
   print("Wrong input")


Q3 =int(input("Which kind of instrument most pleases your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum: "))
if Q3 == 1:
   Slytherin =Slytherin  +4
elif Q3 == 2:
   Hufflepuff = Hufflepuff +4
elif Q3 ==3:
   Ravenclaw =  Ravenclaw  +4
elif Q3 ==4:
   Gryffindor =  Gryffindor +4
else:
   print("wrong input")

print("value of Gryffindor: ")
print(Gryffindor)
print("Value of Ravenclaw: ")
print(Ravenclaw)
print("value of Hufflepuff: ")
print(Hufflepuff)
print("value of Slytherin: ")
print(Slytherin)