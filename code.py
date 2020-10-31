x=input('Do you want to proceed with replacing trick1.txt with trick2.txt? Note, you cannot undo this action. y/n')

def myFunc():
    g=open('trick1.txt', 'r')
    l=g.read()
    g.close()
    trick2=open('trick2.txt', 'r')
    trickt=trick2.read()
    trick2.close()
    trickster=open('trick2.txt', 'w')
    trickster.write(l)
    trickster.close()
    finisher=open('trick1.txt','w')
    finisher.write(trickt)
    finisher.close
    print('done')
if(x=='n'):
    print('cancelled action')
elif(x=='y'):
    myFunc()