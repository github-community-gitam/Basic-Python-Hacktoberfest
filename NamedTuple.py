from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'DOB'])
S = Student('CHANDU', '20', '2541997')
print("The Student age using index is : ", end="")
print(S[1])
print("The Student name using keyname is : ", end="")
print(S.name)
