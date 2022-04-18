from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, adress, number, email, last_name):
       self.name = name
       self.adress = adress
       self.number = number
       self.email = email
       self.label_length = 0 # Variables
       self.last_name = last_name
    def contact(self):
        return f'"Wybieram numer" {self.number} "i dzwonię do" {self.name}'
    @property
    def label_length(self):
        return self._label_length
    @label_length.setter
    def label_length(self, value):
        x = self.name
        self._label_length = value + len(x.replace(" ", ""))
    def __repr__(self):
        return f'{self.name} {self.adress} {self.number} {self.email}'
      
class BusinessContact(BaseContact):
    def __init__(self, firma, *args, position="",company="",business_phone="", **kwargs):
        super().__init__(*args, **kwargs)
        self.positon=position
        self.company=company,
        self.business_phone = business_phone  
        self.firma = firma
    
    def __str__(self):
      return f"{self.firma}, {super()}, {self.position}, {self.company} {self.business_phone}"
#by_name = sorted(vcs, key=lambda vis: vis.name)
person1 = BaseContact(name=fake.name(), adress= fake.address(), number=fake.phone_number(), email=fake.ascii_email(), last_name=fake.last_name())
person2 = BaseContact(name=fake.name(), adress= fake.address(), number=fake.phone_number(), email=fake.ascii_email(), last_name=fake.last_name())
persons = [person1, person2]
Person1 = BusinessContact(name=fake.name(), adress= fake.address(), number=fake.phone_number(), email=fake.ascii_email(), firma=fake.job(), last_name=fake.last_name())


def generation(n):
    for _ in range(n):
        person = BaseContact(name=fake.name(), adress= fake.address(), number=fake.phone_number(), email=fake.ascii_email(), last_name=fake.last_name())
        persons.append(person)
n = 30 #input("Wpisz numer wizytówek.")
generation(n)
#print(person1.contact())
#print(Person1)
print(person1.label_length)# NIE PRACUJE
#print(*persons)

def create_contacts(card_type, quantity):
    empty_list = list() 
    if card_type == "BaseContact":
            for number in range(quantity):
                list.append(BaseContact(name=fake.name(), last_name=fake.last_name(), phone=fake.phone_number(), email=fake.email()))
    elif card_type == "BusinessContact":
            for number in range(quantity):
                empty_list.append(BusinessContact("TESTOWA_FIRMA",name=fake.name(), last_name=fake.last_name(), number=fake.phone_number(),
                                               email=fake.email(), position=fake.job(), company=fake.company(), business_phone=fake.phone_number(),adress=fake.address()))
    else :
        print('Invalid contact type')
    return empty_list


contacts = create_contacts("BusinessContact", 2)
print(contacts)