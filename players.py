import random

class Person:


  def __init__(self, first_name,last_name, age,position,number):
    self.first_name = first_name
    self.last_name=last_name
    self.name=f"{self.first_name} {self.last_name}"

    self.age = age
    self.position=position
    self.number=number




  def __repr__(self):
    return f"** {self.position} **  {self.first_name}({self.age}) { {random.randint(39,150)}  }"
  def __str__(self):
    return f"{self.name}({self.age})"



