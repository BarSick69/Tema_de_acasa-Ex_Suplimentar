bani = int(input("introduceti suma: "))
leu1=1
leu2=5
leu3=10
leu4=20
leu5=50
leu6=100
leu7=200
leu8=500
leu9=1000

while(bani>0):
 if(bani>=leu9):
     n=bani//leu9
     if(n>1):
         print(bani//leu9," bancnote de 1000 lei")
     else:
         print(bani//leu9," bancnota de 1000 lei")
    
     bani=bani-(n*leu9)
 if(bani>=leu8):
     n=bani//leu8
     if(n>1):
         print(bani//leu8," bancnote de 500 lei")
     else:
         print(bani//leu8," bancnota de 500 lei")
     
     bani=bani-(n*leu8)
 if(bani>=leu7):
     n=bani//leu7
     if(n>1):
         print(bani//leu7," bancnote de 200 lei")
     else:
         print(bani//leu7," bancnota de 200 lei")
     
     bani=bani-(n*leu7)
 if(bani>=leu6):
     n=bani//leu6
     if(n>1):
         print(bani//leu6," bancnote de 100 lei")
     else:
         print(bani//leu6," bancnota de 100 lei")
     
     bani=bani-(n*leu6)
 if(bani>=leu5):
     n=bani//leu5
     if(n>1):
         print(bani//leu5," bancnote de 50 lei")
     else:
         print(bani//leu5," bancnota de 50 lei")
     bani=bani-(n*leu5)
 if(bani>=leu4):
     n=bani//leu4
     if(n>1):
         print(bani//leu4," bancnote de 20 lei")
     else:
         print(bani//leu4," bancnota de 20 lei")
     
     bani=bani-(n*leu4)
 if(bani>=leu3):
     n=bani//leu3
     if(n>1):
         print(bani//leu3," bancnote de 10 leu")
     else:
         print(bani//leu3," bancnota de 10 lei")
     
     bani=bani-(n*leu3)
 if(bani>=leu2):
     n=bani//leu2
     if(n>1):
        print(bani//leu2," bancnote de 5 lei")
     else:
        print(bani//leu2," bancnota de 5 lei")
    
     bani=bani-(n*leu2)
 if(bani>=leu1):
     n=bani//leu1
     if(n>1):
         print(bani//leu1," bancnote de 1 leu")
     else:
         print(bani//leu1," bancnota de 1 leu")
     
     

     
     bani=bani-(n*leu1)





    

    




    

    
        
    





