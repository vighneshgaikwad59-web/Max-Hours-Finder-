mera=[("Sonu",300),("abhi",500)]
def My_list(mera):
    hours=0
    montly=""
    for name,worker in mera:
       if worker>hours:
        hours=worker
        montly=name
    return(hours,montly)
print(My_list(mera))
hours,name=(My_list(mera))
print(hours)
print(name)