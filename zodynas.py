import datetime as dt
 
zodynas = {"Jonas": dt.date(2008,1,19), "Azuolas": dt.date(2009,5,25), "Mantas": dt.date(2007,4,23)}
 

eldest_name = None
eldest_dob = None

for name, dob in zodynas.items(): # name, dob = ("Jonas": dt.date(2008,1,19))
    
    if eldest_dob is None or dob < eldest_dob:  # earlier DOB means older
        eldest_name = name
        eldest_dob = dob

print(eldest_name, eldest_dob)