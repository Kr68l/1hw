from abc import ABC, abstractmethod, abstractclassmethod

class Shape(ABC):
    
    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def draw(self):
        pass 

    @abstractclassmethod
    def area(self):
        pass 

    @abstractclassmethod
    def perimetr(self):
        pass 

class sustem(Shape):

    def contact(self, contacts):
        print('Contact: ')
        for contact in contacts: 
            print(f"Name: {contact['name']}, phone: {contact['phone']}") 

    def add(self, add):
        print('Add the contact: ')
        for ad in add:
            print(f"Add name contact: {ad['name']}, add contact phone: {ad['phone']}")

    def show(self):
        print('Team availability')
        print('')
        print('Show contact ')
        print('Show add ')
        print('Add contact ')
        print('Add add ')
        print('Exit')

class Whenistheendthere():
    def __init__(self, user): 
        self.contacts = []
        self.add = []
        self.user = []

    def Idite_gulat(self):
        while True:
            self.user.show()
            comandd = input('Enter command: ')
            if comandd == 'Show contact':
                self.user.show(self.contacts)
            elif comandd == 'Show add':
                self.user.show(self.contacts)
            elif comandd == 'Add contact':
                self.user.show(self.add)
            elif comandd == 'Add contac':
                name = input('Enter contact name: ')
                phone = input('Enter contact phone: ')
                self.contacts.append({'name': name , 'phone':phone})
            elif comandd == 'Add add': 
                name = input('Enter contact name: ')
                phone = input('Enter contact phone: ')
                self.add.append({ 'Add name contac': name, 'add contact phone': phone})
            elif comandd == 'exit':
                break
            else: 
                print(input('Try again'))
if __name__ == '__main__':
    qww =  sustem()
    qqw = Whenistheendthere(qww)
    Whenistheendthere.Idite_gulat()


