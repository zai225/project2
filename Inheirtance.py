class student:
  def __init__(self, name, rollno):
    self.name = name
    self.rollno = rollno
  def show(self):
    print(f"The name of the student is {self.name} and roll no is {self.rollno}")

class parent(student):
  def __init__(self, name, rollno, address):
    super().__init__(name, rollno)
    self.address = address
  
  def parent_info(self):
    print(f"The name of the student is {self.name} and roll no is {self.rollno} they lives in {self.address}")

a = parent("Kavya", 22,  "Malad east")
a.parent_info()

#que
class animal:
  def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} is crealted")

class breed(animal):
  def __init__(self, name, breed):
     super().__init__(name)
     self.breed = breed
     print(f"The Dog's name is {self.name} and the breed is {self.breed}")

breed = breed("Pluto", "Beagle")



      

  




























