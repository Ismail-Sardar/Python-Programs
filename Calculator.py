#Addition
def add(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
    return(n1+n2+n3+n4+n5+n6+n7+n8+n9+n10)
def add1(n1,n2,n3,n4,n5,n6,n7,n8,n9):
    return(n1+n2+n3+n4+n5+n6+n7+n8+n9)
def add2(n1,n2,n3,n4,n5,n6,n7,n8):
    return(n1+n2+n3+n4+n5+n6+n7+n8)
def add3(n1,n2,n3,n4,n5,n6,n7):
    return(n1+n2+n3+n4+n5+n6+n7)
def add4(n1,n2,n3,n4,n5,n6):
    return(n1+n2+n3+n4+n5+n6)
def add5(n1,n2,n3,n4,n5):
    return(n1+n2+n3+n4+n5)
def add6(n1,n2,n3,n4):
    return(n1+n2+n3+n4)
def add7(n1,n2,n3):
    return(n1+n2+n3)
def add8(n1,n2):
    return(n1+n2)

#Subtraction
def sub(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
    return(n1-n2-n3-n4-n5-n6-n7-n8-n9-n10)
def sub1(n1,n2,n3,n4,n5,n6,n7,n8,n9):
    return(n1-n2-n3-n4-n5-n6-n7-n8-n9)
def sub2(n1,n2,n3,n4,n5,n6,n7,n8):
    return(n1-n2-n3-n4-n5-n6-n7-n8)
def sub3(n1,n2,n3,n4,n5,n6,n7):
    return(n1-n2-n3-n4-n5-n6-n7)
def sub4(n1,n2,n3,n4,n5,n6):
    return(n1-n2-n3-n4-n5-n6)
def sub5(n1,n2,n3,n4,n5):
    return(n1-n2-n3-n4-n5)
def sub6(n1,n2,n3,n4):
    return(n1-n2-n3-n4)
def sub7(n1,n2,n3):
    return(n1-n2-n3)
def sub8(n1,n2):
    return(n1-n2)

#Multiplication
def mul(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
    return(n1*n2*n3*n4*n5*n6*n7*n8*n9*n10)
def mul1(n1,n2,n3,n4,n5,n6,n7,n8,n9):
    return(n1*n2*n3*n4*n5*n6*n7*n8*n9)
def mul2(n1,n2,n3,n4,n5,n6,n7,n8):
    return(n1*n2*n3*n4*n5*n6*n7*n8)
def mul3(n1,n2,n3,n4,n5,n6,n7):
    return(n1*n2*n3*n4*n5*n6*n7)
def mul4(n1,n2,n3,n4,n5,n6):
    return(n1*n2*n3*n4*n5*n6)
def mul5(n1,n2,n3,n4,n5):
    return(n1*n2*n3*n4*n5)
def mul6(n1,n2,n3,n4):
    return(n1*n2*n3*n4)
def mul7(n1,n2,n3):
    return(n1*n2*n3)
def mul8(n1,n2):
    return(n1*n2)

#Division
def div(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
    return(n1/n2/n3/n4/n5/n6/n7/n8/n9/n10)
def div1(n1,n2,n3,n4,n5,n6,n7,n8,n9):
    return(n1/n2/n3/n4/n5/n6/n7/n8/n9)
def div2(n1,n2,n3,n4,n5,n6,n7,n8):
    return(n1/n2/n3/n4/n5/n6/n7/n8)
def div3(n1,n2,n3,n4,n5,n6,n7):
    return(n1/n2/n3/n4/n5/n6/n7)
def div4(n1,n2,n3,n4,n5,n6):
    return(n1/n2/n3/n4/n5/n6)
def div5(n1,n2,n3,n4,n5):
    return(n1/n2/n3/n4/n5)
def div6(n1,n2,n3,n4):
    return(n1/n2/n3/n4)
def div7(n1,n2,n3):
    return(n1/n2/n3)
def div8(n1,n2):
    return(n1/n2)


operator=input("enter operator,(addition,subtraction,multiplication,division):")


# code for addition
if operator=='addition':
    n=int(input("enter no of values to be added:"))

    if n==1:
      print("min two values required")
    elif n==2:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      print(add8(n1,n2))
    elif n==3:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      print(add7(n1,n2,n3))
    elif n==4:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      print(add6(n1,n2,n3,n4))
    elif n==5:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      print(add5(n1,n2,n3,n4,n5))
    elif n==6:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      print(add4(n1,n2,n3,n4,n5,n6))
    elif n==7:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      print(add3(n1,n2,n3,n4,n5,n6,n7))
    elif n==8:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      print(add2(n1,n2,n3,n4,n5,n6,n7,n8))
    elif n==9:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      n9=int(input("Enter 9th no:"))
      print(add1(n1,n2,n3,n4,n5,n6,n7,n8,n9))
    elif n==10:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      n9=int(input("Enter 9th no:"))
      n10=int(input("Enter 10th no:"))
      print(add(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10))
    else:
       print("can't operate")  


# code for subtraction
if operator=='subtraction':
    n=int(input("enter no of values to be subtracted:"))

    if n==1:
      print("min two values required")
    elif n==2:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      print(sub8(n1,n2))
    elif n==3:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      print(sub7(n1,n2,n3))
    elif n==4:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      print(sub6(n1,n2,n3,n4))
    elif n==5:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      print(sub5(n1,n2,n3,n4,n5))
    elif n==6:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      print(sub4(n1,n2,n3,n4,n5,n6))
    elif n==7:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      print(sub3(n1,n2,n3,n4,n5,n6,n7))
    elif n==8:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      print(sub2(n1,n2,n3,n4,n5,n6,n7,n8))
    elif n==9:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      n9=int(input("Enter 9th no:"))
      print(sub1(n1,n2,n3,n4,n5,n6,n7,n8,n9))
    elif n==10:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      n9=int(input("Enter 9th no:"))
      n10=int(input("Enter 10th no:"))
      print(sub(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10))
    else:
       print("can't operate")  


# code for multiplication
if operator=='multiplication':
    n=int(input("enter no of values to be multiplied:"))

    if n==1:
      print("min two values required")
    elif n==2:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      print(mul8(n1,n2))
    elif n==3:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      print(mul7(n1,n2,n3))
    elif n==4:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      print(mul6(n1,n2,n3,n4))
    elif n==5:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      print(mul5(n1,n2,n3,n4,n5))
    elif n==6:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      print(mul4(n1,n2,n3,n4,n5,n6))
    elif n==7:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      print(mul3(n1,n2,n3,n4,n5,n6,n7))
    elif n==8:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      print(mul2(n1,n2,n3,n4,n5,n6,n7,n8))
    elif n==9:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      n9=int(input("Enter 9th no:"))
      print(mul1(n1,n2,n3,n4,n5,n6,n7,n8,n9))
    elif n==10:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      n9=int(input("Enter 9th no:"))
      n10=int(input("Enter 10th no:"))
      print(mul(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10))
    else:
       print("can't operate")  


# code for division
if operator=='division':
    n=int(input("enter no of values to be divided:"))

    if n==1:
      print("min two values required")
    elif n==2:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      print(div8(n1,n2))
    elif n==3:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      print(div7(n1,n2,n3))
    elif n==4:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      print(div6(n1,n2,n3,n4))
    elif n==5:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      print(div5(n1,n2,n3,n4,n5))
    elif n==6:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      print(div4(n1,n2,n3,n4,n5,n6))
    elif n==7:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      print(div3(n1,n2,n3,n4,n5,n6,n7))
    elif n==8:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      print(div2(n1,n2,n3,n4,n5,n6,n7,n8))
    elif n==9:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      n9=int(input("Enter 9th no:"))
      print(div1(n1,n2,n3,n4,n5,n6,n7,n8,n9))
    elif n==10:
      n1=int(input("enter 1st no:"))
      n2=int(input("enter 2nd no:"))
      n3=int(input("enter 3rd no:"))
      n4=int(input("enter 4th no:"))
      n5=int(input("Enter 5th no:"))
      n6=int(input("Enter 6th no:"))
      n7=int(input("Enter 7th no:"))
      n8=int(input("Enter 8th no:"))
      n9=int(input("Enter 9th no:"))
      n10=int(input("Enter 10th no:"))
      print(div(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10))
    else:
       print("can't operate")  









    



    
    

















































    



    
    
















































    



    
    

















































    



    
    
































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































