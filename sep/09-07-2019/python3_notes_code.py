class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __len__(self):
    return 7
  def bark(self, person):
    return print(self.name + ' barks at ' + person)

d = Dog('Fido', 3)
print("printing d = Dog('Fido', 3)")
d.bark('alvin')
print('-----')
print("printing Dog.bark(d, 'alvin')")
Dog.bark(d, 'alvin')
print('-----')
print('len(d)', len(d))

my_str = 'potato'
my_list = [1,2,3,4,6,]
my_dictionary = {
  'name': 'a/A',
  'color': 'red'
}

print('len(my_str) prints', len(my_str))
print('len(my_list) prints', len(my_list))
print('len(my_dictionary) prints', len(my_dictionary))

a = [3, 4]
b = [3, 4]
print('a == b prints', a == b) # true

c = [4, 3]
print('a == c prints', a == c) # false
print('a is b prints', a is b)
a[0] = '!'
b[1] = '!'
print('a prints', a)
print('b prints', b)

a = [3, 4]
b = a

print('a is b prints', a is b)
