print ('Welcome')
import random
for i in range(1):
  keygen = (random.randint(11111111111, 999999999999999))
print ("")
message=input ('Enter message you want to decrypt:')
alphabet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
key = input("Encryption Key:")
encrypt =''

##This in incorrect since we are decrypting it should be -=alphabet [newposition], however it states +=. <<

#for i in message:
  #position=alphabet.find(i)
  #newposition=(position+ +int(key) )%94
  #encrypt+=alphabet [newposition]
#output = (encrypt)

##This one is invalid because for the output at the end it's encrypt, not decrypt. <<

#for i in message:
  #position=alphabet.find(i)
  #newposition=(position+ -int(key) )%94
  #encrypt+=alphabet [newposition]
#output = (encrypt)

##This one is invalid since it doesn't state i for alphabet.find(). <<

#for i in message:
  #position=alphabet.find()
  #newposition=(position+ -int(key) )%94
  #encrypt+=alphabet [newposition]
#output = (encrypt)

for i in message:
  position=alphabet.find(i)
  newposition=(position+ -int(key) )%94
  encrypt+=alphabet [newposition]
output = (decrypt)

keyout = (keygen)


print ('Decrypted message: '+ (output) )
