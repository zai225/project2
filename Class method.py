class Employee:
    Company = "Apple"
    def show (self):
      print(f"The name of the employee is {self.name} and he works in {self.Company}")

    @classmethod
    def change_company(cls, new_company):
        cls.Company = new_company

a = Employee()
a.name = "Shunham"
a.show()
a.change_company("Nestle")
a.show()




