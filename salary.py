def gross_salary(basic,HRA,Allowance):
    return basic+HRA+allowance

def deducations(gross):
    pf=gross*0.12
    tax=gross*0.05
    return pf+tax

def net_salary(gross,deducation):
    return gross-deducation

employee("name"="Sneha","basic"=50000,"HRA"=7000,"allowance"=3000)
    gross=gross_salary(employee[basic],employee[HRA],employee[allowance])
    deducation=deducation=deducation(gross)
    net=net_salary(gross,deducation)

print("========SALARY SLIP========")
print("Name:",name)
print("Gross salary:",gross)
print("Deducation:",deducation)print("Net salary:",net)
