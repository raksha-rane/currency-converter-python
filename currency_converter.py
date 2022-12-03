print("\n")
print("Hello! I am Raksha Rane and this is my Currency Converter project.")
print("\n")
print("In this currency converter we have 7 different currencies, namely:")
print("GBP - United Kingdom Pound")
print("CAD - Canada Dollar")
print("CNY - China Yuan Renminbi")
print("USD - United States Dollar")
print("RUB - Russia Ruble")
print("INR - Indian Rupee")
print("\n")
print("The above mentioned are the symbols of the respective currencies.")

a='GBP'
b='CAD'
c='CNY'
d='USD'
e='RUB'
f='INR'

currency =['GBP','CAD','CNY','USD','RUB','INR']

def convert(cur1,cur2,amount):
    if cur1==a and cur2==b: # for GBP to CAD
        return (amount*1.61)
    elif cur1==b and cur2==a: # for CAD to GBP
        return (amount*0.62)
    elif cur1==a and cur2==c: # for GBP to CNY
        return(amount*8.67) 
    elif cur1==c and cur2==a: # for CNY to GBP
        return(amount*0.12)
    elif cur1==a and cur2==d: # for GBP to USD
        return(amount*1.21)
    elif cur1==d and cur2==a: # for USD to GBP
        return(amount*0.83)
    elif cur1==a and cur2==e: # for GBP to RUB
        return(amount*73.15)
    elif cur1==e and cur2==a: # for RUB to GBP
        return(amount*0.014)
    elif cur1==a and cur2==f: # for GBP to INR
        return(amount*98.75)
    elif cur1==f and cur2==a: # for INR to GBP
        return(amount*0.010)
    elif cur1==b and cur2==c: # for CAD to CNY
        return(amount*5.35)
    elif cur1==c and cur2==b: # for CNY to CAD
        return(amount*0.19)
    elif cur1==b and cur2==d: # for CAD to USD
        return(amount*0.75)
    elif cur1==d and cur2==b: # for USD to CAD
        return(amount*1.34)
    elif cur1==b and cur2==e: # for CAD to RUB
        return(amount*45.14)
    elif cur1==e and cur2==b: # for RUB to CAD
        return(amount*0.022)
    elif cur1==b and cur2==f: # for CAD to INR
        return(amount*60.94)
    elif cur1==f and cur2==b: # for INR to CAD
        return(amount*0.016)
    elif cur1==c and cur2==d: # for CNY to USD
        return(amount*0.14)
    elif cur1==d and cur2==c: # for USD to CNY
        return(amount*7.17)
    elif cur1==c and cur2==e: # for CNY to RUB
        return(amount*8.50)
    elif cur1==e and cur2==c: # for RUB to CNY
        return(amount*0.12)
    elif cur1==c and cur2==f: # for CNY to INR
        return(amount*11.38)
    elif cur1==f and cur2==c: # for INR to CNY
        return(amount*0.088)
    elif cur1==d and cur2==e: # for USD to RUB
        return(amount*60.50)
    elif cur1==e and cur2==d: # for RUB to USD
        return(amount*0.017)
    elif cur1==d and cur2==f: # for USD to INR
        return(amount*81.67)
    elif cur1==f and cur2==d: # for INR to USD
        return(amount*0.012)
    elif cur1==e and cur2==f: # for RUB to INR
        return(amount*1.35)
    elif cur1==f and cur2==e: # for INR to RUB
        return(amount*0.74)
    else:
        return 0
print("\n")
start=input("To start with your conversion, press 1: ")

if start=='1':
    amount=input("Enter amount to be converted: ")
    cur1=input("Enter initial currency symbol: ").upper()
    cur2=input("Enter desired conversion currency symbol: ").upper()
    if amount.isdigit()==False and (cur1 not in currency or cur2 not in currency):
        print("Please enter valid amount and currencies!")
    elif cur1 not in currency or cur2 not in currency:
        print("Please enter valid currencies!")
    elif amount.isdigit()==False:
        print("Please enter valid amount!")
    else: 
        final=convert(cur1,cur2,float(amount))
    
        print("\n")
        print("You are converting", float(amount), cur1, "to", cur2,".")
        print("The converted amount is:", final)
        print("\n")
        print("Thank you for using my currency converter! Visit again.")
else:
    print("Please enter 1 to start. Run program to begin again.")
