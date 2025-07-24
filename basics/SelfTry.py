#print('Heloo Rajarshi')
#print("Heloo Rajarshi")

for n in range(5):
    print(n)

for n in range(2,10,2):
    print(n)

a=4
while a<10:
    print('while ',a)
    a=a+2

b=90
if b>10:
    print('B ',b)
elif b==1:
    print('B ',b)
else:
    print('B ',b)


s='   helo-there-,   -this-is-rajarshi'
print(s.strip())
print(s[2:4])
print(s[3::1])


list1=['123','22','53','3454','8455','2456']
for n in list1:
    print(n)

for i in range(len(list1)):
    print(list1[i])

list11 = [xx for xx in list1 if '1' in xx]
print(list11)

def myDetails(fname):
    print('this is ',fname)

myDetails("raharshi")


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)