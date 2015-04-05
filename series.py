from collections import OrderedDict
import string
import sys

LetterList = [chr(x) for x in range(65, 91)]
LetterList.insert(0, 0)
LetterNumDic={'A':1}
#print(LetterList)

def CalculateNumber():
    '''calculates number corresponding to each character based on series
    A=1
    B=A*2+2
    C=B*2+3
    ...
    and saves it in a dictionary'''
    a=1
    for x in LetterList[2:]:
      LetterNumDic[x]=LetterNumDic[LetterList[LetterList.index(x)-1]]*2+LetterList.index(x)

def LetterToNum(letter):
    '''
    returns number corresponding to a letter
    like 11 for C
    26 for D
    57 for E
    and soon.
    '''
    return LetterNumDic[letter]
    
def StringToSum(Str):
    '''
    returns sum of all letters based on given series
    like 42 for ABCD 1+4+11+26
    29132 for KLHM
    203 for DEF
    '''
    sum=0
    for l in Str:
     #print (l)
     sum=sum+LetterNumDic[l]
    return sum  

def ShortestStringOfNum(Num):
    '''returns shotest string of a number like for
    500 it returns GBA 274+247+4+1+1 GGBAA
    GBA is shortest string of GGBAA
    similarly few more test cases are as follows
    for 2000 shortest string is IHGFEB
    for 4444 its KGE
    for 2132 its JEDCA.
    '''
    ShortestStr=""
    TempLetter = LetterList[-1]
    while(1):
        if(LetterNumDic[TempLetter]<=Num):
            
            if ShortestStr.find(TempLetter)==-1:
               ShortestStr=ShortestStr+TempLetter
            Num = Num-LetterNumDic[TempLetter]
        else:
           TempLetter = ord (TempLetter)-1
           TempLetter = chr(TempLetter)
        if Num == 0:
           break
    return ShortestStr   

CalculateNumber()
while(1):
    print ("press 1 Character's corresponding number")
    print ("Press 2 Sum of the Letters")
    print ("Press 3 Shortest string of Number")
    print ("press 4 Exit" )
    try:
   	    select = input( "Please choose one of the above  ")
   	    select =int(select)
   	    if select == 1:
   	       c=input("Enter letter:")
   	       if (c.isalpha() and (len(c)==1)):
   	           print ("Correponding number is:",LetterToNum(c.upper()))
   	       else:
   	           print ("please enter a single letter")
   	    if select == 2:
   	        c=input("Please enter word:")
   	        if c.isalpha():
   	            print("Sum is:",StringToSum(c.upper()))
   	        else:
   	            print("not a alphabet string");
   	    if select == 3:
   	        c=input("Enter number:")
   	        if c.isdigit():
   	            print("Shortest string is:",ShortestStringOfNum(int(c)))
   	        else:
   	            print("not a number")
   	    if select == 4:
   	        break
    except:
           print("")
#print (LetterToNum('G'))
#print (StringToSum('AB'))
#print (ShortestStringOfNum(500))
