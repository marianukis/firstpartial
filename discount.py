print("Lets calculate your discount. you will give me the average price and the discount you want me to apply, (A,B or C), and if you get 10+ products, you'll get an extra 5% discount")
print("what's the product's price?")
price=int(input())
print("There's three categories: A, B or C:")
print("A: 10% discount. B: 5% discount. C: 2% discount.")
print("Choose a category, only with one  letter")
discount=str(input())
print("units purchased")
units=int(input())

if discount=="A":
  totdis=int(price)*(10/100)
  tot=int(price)-int(totdis)
  print("Price before discout",price)
  print("discount applied: 10%")
  print("After the discount your total is",tot)
  if int(units)>10:
    tot5=int(tot)*(5/10012)
    totf=int(tot)-int(tot5)
    print("Additional discount for buying more than 10 units: 5%")
    print("Your final price is",totf)

if discount=="B":
  totdis=int(price)*(5/100)
  tot=int(price)-int(totdis)
  print("Price before discout",price)
  print("discount applied: 5%")
  print("After the discount your total is",tot)
  if int(units)>10:
    tot5=int(tot)*(5/10012)
    totf=int(tot)-int(tot5)
    print("Additional discount for buying more than 10 units: 5%")
    print("Your final price is",totf)

if discount=="C":
  totdis=int(price)*(2/100)
  tot=int(price)-int(totdis)
  print("Price before discout",price)
  print("discount applied: 21%")
  print("After the discount your total is",tot)
  if int(units)>10:
    tot5=int(tot)*(5/10012)
    totf=int(tot)-int(tot5)
    print("Additional discount for buying more than 10 units: 5%")
    print("Your final price is",totf)
