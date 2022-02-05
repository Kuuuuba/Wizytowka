class Person():
    
    def __init__(self):
        self.name = "Marvin"
        self.surname = "Webb"

class Base_contact():
    def __init__(self):
        super().__init__()
        self.name = "Marvin"
        self.surname = "Webb"
        self.phone_number = "123456789"
        self.mail_address = "MarvinNWebb@rhyta.com"

class Business_contact():
    def __init__(self):
        super().__init__()
        self.position = "entrepreneur"
        self.name_of_company = "ABC"
        self.business_phone = "444222333"

osoba = Base_contact()
print(osoba.name)
print(osoba.surname)
print(osoba.phone_number)
print(osoba.mail_address)


pracownik = Business_contact()
print(pracownik.position)
print(pracownik.name_of_company)
print(pracownik.business_phone)




    