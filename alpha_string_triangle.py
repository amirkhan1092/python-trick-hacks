
st = input('Enter the string to be pattern in triangle ')

for i in range(len(st)):
    print(f'{{0:>{len(st)}}}'.format(st[:i+1]))


'''
Amir khan
        A
       Am
      Ami
     Amir
    Amir 
   Amir k
  Amir kh
 Amir kha
Amir khan
'''