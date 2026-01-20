su = 0
orger = True
b = None
a = 0

for i in range(10):
  a = int(input("Enter Number"))
  su = su + a
  if orger and b != None:
    if a <= b:
      orger = False
  b = a

if orger:
  print("You wrote numbers in order")
print("Sum is: " + str(su))
