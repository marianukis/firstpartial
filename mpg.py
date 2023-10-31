print("Enter the distance in miles:")
distance=float(input())
print("Enter the car's miles per gallon (MPG):")
MPG=float(input())
print("Enter the current price of gas per gallon:")
price=float(input())
print("Enter the number of days you plan to travel")
days=int(input())
gallons_needed=distance/MPG
cost=gallons_needed*price
total=cost*days
print("The cost of traveling",distance,"miles in",days,"days is $",total)
