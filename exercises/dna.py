dna =['A','C','C','A','T','T','G','A','C','A']

print(dna.count('A'))
print(dna.index('T'))

dna2 = dna
dna2.remove('G')
dna2.insert(3,'A')
dna2.reverse()
print(dna2)
