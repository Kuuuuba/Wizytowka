from classes import BaseContact
from classes import BusinessContact
from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, adress, number, email):
       self.name = name
       self.adress = adress
       self.number = number
       self.email = email
       self.label_length = 0 # Variables
    def contact(self):
        return f'"Wybieram numer" {self.number} "i dzwonię do" {self.name}'
    @property
    def label_length(self):
        return self._label_length
    @label_length.setter
    def label_length(self, value):
        x = self.name
        self._label_length = value + len(x.replace(" ", ""))
    def __str__(self):
        return f'{self.name} {self.adress} {self.number} {self.email}'
class BusinessContact(BaseContact):
    def __init__(self, firma, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.firma = firma
#by_name = sorted(vcs, key=lambda vis: vis.name)
person1 = BaseContact(name=fake.name(), adress= fake.address(), number=fake.phone_number(), email=fake.ascii_email())
person2 = BaseContact(name=fake.name(), adress= fake.address(), number=fake.phone_number(), email=fake.ascii_email())
persons = [person1, person2]
Person1 = BusinessContact(name=fake.name(), adress= fake.address(), number=fake.phone_number(), email=fake.ascii_email(), firma=fake.job())


def generation(n):
    for _ in range(n):
        person = BaseContact(name=fake.name(), adress= fake.address(), number=fake.phone_number(), email=fake.ascii_email())
        persons.append(person)
n = 30 #input("Wpisz numer wizytówek.")
generation(n)
#print(person1.contact())
#print(Person1)
print(person1.label_length())# NIE PRACUJE
#print(*persons)

def create_contacts(card_type, quantity):
    list() 
    if card_type == "BaseContact":
            for number in range(quantity):
                list.append(BaseContact(name=fake.name(), last_name=fake.last_name(), phone=fake.phone_number(), email=fake.email()))
    elif card_type == "BusinessContact":
            for number in range(quantity):
                list.append(BusinessContact(name=fake.name(), last_name=fake.last_name(), phone=fake.phone_number(),
                                               email=fake.email(), posiiton=fake.job(), company=fake.company(), business_phone=fake.phone_number()))
    else :
        print('Invalid contact type')
    return list()


list() == create_contacts("BusinessContact", 2)
single_card = list()
print(single_card.contact())
    


