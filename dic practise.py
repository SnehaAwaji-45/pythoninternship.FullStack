
#std_details
student={"name":"sam","Age":25,"Course":"BCA","Marks":88}
print(student)

if student["Marks"]>=40:
    print("result:passed")
else:
    print("result:failed")


#contact book
contact={"sam":8974563209,"Anu":7843562190}
print(contact)

contact.update({"divya":9087695431})
print(contact)

print(contact['sam'])

contact['sam']=87653890652
print("After update:",contact)

del contact['Anu']
print(" After delete:",contact)



