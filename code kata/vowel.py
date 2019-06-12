str=input()
l1=['a','e','i','o','u']
l2=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
if(str in l1):
  print('Vowel')
elif(str in l2):
  print('Consonant')
else:
  print('invalid')
