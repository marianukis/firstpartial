print("Calculating the amount needed for the retirement found:")
print("Enter your actual age:")
age=int(input())
print("Enter your retirement age:")
retire=int(input())
print("Enter the desired retirement amount:")
goal=int(input())
r = 0.10/12
n = (retire-age)*12
t = retire - age
PMT = (goal)*r/(((1+r)**n)-1)*((1+r)**(-t))
print("To retire at the age of",retire,"you will need to save $",PMT,"monthly, considering that the rate is 10% each year")
https://replit.com/@marianaaponceee/payment-mariana#main.py
