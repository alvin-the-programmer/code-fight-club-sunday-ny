class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __len__(self):
    return 7
  def bark(self, person):
    return print(self.name + ' barks at ' + person)

d = Dog('Fido', 3)
d.bark('alvin')
Dog.bark(d, 'alvin')
print(len(d))

my_str = 'potato'
my_list = [1,2,3,4,6,]
my_dictionary = {
  'name': 'a/A',
  'color': 'red'
}

print(len(my_str))
print(len(my_list))
print(len(my_dictionary))