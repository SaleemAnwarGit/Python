# first parameter of each method is reference to current object, 
# it could be named whatever you want, as self, this, abc whatever.
# __init__ is constructor, __str__ is toString
# del obj.property will delete property, and del object will delete object.
from datetime import date


class Person:
  def __init__(this, name, birthdate):
    this.name = name
    this.birthdate = birthdate

  def __str__(selfOrthis):
    return f"{selfOrthis.name} born on {selfOrthis.birthdate} and is aged {selfOrthis.Age()}"

  def Age(self):
    return (date.today()-self.birthdate) # datetime.timedelta needed further formating


#region Test class Person
p1 = Person('First Person', date(1990,1,1))
print(p1)

#Testing Inheritance
class Dummy(Person):
  pass

dp = Dummy('Dummy Person', date.today())
print(dp.Age())
#endregion

class Student(Person):
  def __init__(this, name, birthdate, Id):
    super().__init__(name, birthdate)
    this.Id = Id
  
  def Info(thisObject):
    #return str(thisObject.Id)+ ': '+ super().__str__()
    return str(thisObject.Id)+ ': '+ thisObject.__str__()

#Test Student
s1 = Student('John', date.today(), 1)
print(s1) # calling parent class __str__
print(s1.Info())

#Things still to try
# polymorphism
# abstraction, interfaces and abstract class
# static
# multiple inheritance and diamond problem

#iterator on classes
class People:
  persons=[]
  def Add(self, thisMan):
    self.persons.append(thisMan)

  def All(self):
    for x in self.persons:
      print(x)

team1 =People()
team1.Add(Person('Person 1', date.today()))
team1.Add(Person('Person 2', date.today()))
team1.Add(Person('Person 3', date.today()))
team1.All()

#explore __iter__ on People collection class