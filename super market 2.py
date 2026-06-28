sum_of_items=1
total_amount=0
t=0
z=0

while True:
    print("enter the",sum_of_items,"item :")
    item=(input(""))

    if item=="done" or item=="finish" or item=="end" or item=="":
        print("total amount of things =",total_amount)
        break

    sum_of_items=sum_of_items+1

    amount=int(input("enter the amount :"))

    if amount==str:
        break

    price=int(input("enter the price :"))

    print("your amount of",item,"=",amount)
    print("the total price of the",item,"=",amount*price)

    kl=amount*price
    total_amount=total_amount+amount
    price=z+price
    t=t+1

    price_items=[]
    price_items.append(kl)
    sum_of_items_in_list=sum(price_items)

print("totall price of things =",sum_of_items_in_list)