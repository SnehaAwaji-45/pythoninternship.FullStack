products=input("enter a product")
def products(price,quantity):
    return price*quantity
def discount(total):
    if total>=5000:
        return total*0.10
    elif total>=10000:
        return total*0.20
    else:
        return 0   
def gst(amount):
    return amount*0.18

def delivery(total):
    if total>=1000:
        return 0
    else:
        return 100

price=int(input("enter price:"))
quantity=int(input("enter quantity:"))
delivery=int(input("enter a delivery:"))
total=products(price,quantity)
discount_amount=discount(total)
gst_amount=gst(total)
final_amount=total-discount_amount+total_amount+gst_amount+delivery

print("=======Bill========")
print("products:",total)
print("discount:",discount_amount)
print("GST:",gst_amount)
print("Delivery:",delivery)
print("Final_amount:",final_amount)


            
                
    
    
    
