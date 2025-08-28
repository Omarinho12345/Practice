height = int(input("how tall are you?"))
credits = int(input("how many credits do you have?"))
if height > 137 and credits >= 10:
  print("enjoy the ride!")
if  height < 137 and credits >=10:
  print("you are not tall enough to ride.")
if height > 137 and credits < 10:
   print ("you don't have enough credits")
if height < 137 and credits < 10:
  print ("you don't have both of the requirements")