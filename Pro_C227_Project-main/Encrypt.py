print('Welcome')
print("Rules: Dont open it")

message=input ('Enter message you want to encrypt :')
alphabet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
key = input("Enter a encrypt key of your Choice (at lease 8 Numbers long): ")
encrypt =''

##This is incorrect since it doesn't input key for int(). <<

#for i in message:
  #position=alphabet.find(i)
  #newposition=(position+ int())%94
  #encrypt+=alphabet [newposition]
#output = (encrypt)

##This one is incorrect since it doesn't state i for alphabet.find() <<

#for i in message:
  #position=alphabet.find()
  #newposition=(position+ int(key) )%94
  #encrypt+=alphabet [newposition]
#output = (encrypt)


for i in message:
  position=alphabet.find(i)
  newposition=(position+ int(key) )%94
  encrypt+=alphabet [newposition]
output = (encrypt)

##This one is wrong since it doesn't establish encrypt at the end for output. <<

#for i in message:
  #position=alphabet.find(i)
  #newposition=(position+ int(key) )%94
  #encrypt+=alphabet [newposition]
#output = ()










print ('Encrypted Message: '+ (output) )
print ('Encryption Key: '+ (key) )
