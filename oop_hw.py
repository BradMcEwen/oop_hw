# ============ Question 1 ===============

class Vehicle:
    def __init__(self, reg_number, type, owner):
        self.registration_number = reg_number
        self.type = type
        self.owner = owner
        
    def check_num(registration_number):
        print("12344223")

    def car_type(type):
        print("sedan")
    def update_owner(self, owner):
        print(f"{owner} now owns the car!")

Corolla = Vehicle("12344223", "sedan", "Chad")
Corolla.update_owner("Carl")
Corolla.update_owner("Brad")
Corolla.update_owner("Frank")
Corolla.update_owner("Teddy")
print(Corolla.owner)
