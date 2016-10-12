User = {'Name': 'Zara', 'Age': 7, 'Gender': 'Male'}

#User = dict(Name = 'Zara' ,Age = 7, Gender = 'Male')
print User['Name']

User2 = {'Name': 'John', 'Age': 9, 'Gender': 'Female'}

User.update(User2)

print(User)