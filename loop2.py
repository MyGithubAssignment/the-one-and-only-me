#program to print the multiplication of any integers
num=input("enter the integers:")
i=1
while i<=10:
     print(str(num)+ str(" * ")+  str(i)+ str(" = "), num*i)
     i=i+1


#ask the user to enter to number using only one input statement and add them to list:

lst=[]
num=int(input("How many number:"))
for n in range(num):
    numbers=int(input("enter the number:"))
    lst.append(numbers)
    print("the sum of given list:",sum(lst))


#from list ask the user to remove and print the numbers:
list=[1,2,3,7,8,9,56,78,96,63,42,75,78,41,52,63,]
list.remove(75)
print(list)

#from a list seperate the integer,str and float into three elements:
list=[1,2,3,"rose","marigold","plate",2.6,5.6,8.9,"shyam"]
int=1,2,3
str="rose","marigold","plate"
float=2.6,5.6,8.9
print(int)
print(float)
print(str)

#to perform the arithemetic operations:
a=float(input("enter the first number:"))
b=float(input("enter the second numbers:"))
ch=input("a-addition\n s-subtraction\n m-multiply\n d-divide\n q-quit")
while ch!='q':
    if ch=='a':
        print("the sum of a and b is:",a+b)
    if ch=='s':
        print("the difference of a and b is:",a-b)
    if ch=='m':
        print("the product of a and b is:",a*b)
    if ch=='d':
        print("the divide of a and b is:",a/b)

        quit(0)
        ch=input("enter the choice again \n a-addition \n s-subtraction \n m-multiply \n Q-quit")
        a=input("enter the first:")
        b=input("enter the second:")
        print(quit)

#perform to seperate even and odd from the list:
list=[]
n=int(input("enter the elements:"))
for i in range(1,n+1):
    x=input("enter the elements:")
    list.append(x)

even_lst=[]
odd_lst=[]
for j in list:
    if int(j) % 2 == 0:
        even_lst.append(j)
    else:
        odd_lst.append(j)
print("even numbers list are:",even_lst)
print("odd numbers list are:",odd_lst)