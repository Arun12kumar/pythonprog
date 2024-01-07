

class Person:
    def __init__(self, name ,age, address):
        self.name = name
        self.age = age
        self.address = address

    def update_info(self,new_name,new_age, new_address):
        self.name = new_name
        self.age = new_age
        self.address = new_address

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}")    

Arun = Person("Arun Kumar","24","Ithiparambil house maruvakkad" )  
print("initial Information:")
Arun.display()


Arun.update_info("Arun Kumar","25","Ithiparambil house maruvakkad kochi")
print("\nupdate Information:")
Arun.display()
