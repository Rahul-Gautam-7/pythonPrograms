#simple interest prn/100

price = int(input("Enter you price : "))
rate_of_interest = int(input("Rate of interest : "))
year = int(input("Enter Number of years : "))


if rate_of_interest > 0 and rate_of_interest < 100:
    print(f"Simple Interest : {(rate_of_interest*price*year)/100}")
else:
    print("Rate of interest must be between 0 to 100")
