#Question:-1=> Write a program that accepts a sentence and calculate the number of latters and digits.
def sentence(s):
    a=b=1
    for i in s:
        if i.isdigit():
            a+=1;

        elif i.isalpha():
            b+=1
    print("Digits={}".format(a-1))
    print("Letters={}".format(b-1))
sentence(input("Enter the Sentence:"))

#Question:2 => Write a program, which we find all such numbers between 1000 to 3000 such the each digit of the number is an even number.
def num():
    for i in range(1000,3000+2):
        if i%2==0:
            print("Even Number:{}".format(i))

num()

#Question:3 => Write a given integer number n, write a program to generate a dictionary that contain(i,i*i) such as an integeral number between
#1 to n and then should program should print the dictionary.

def num(n):
    d={}
    for i in range(1,n+1):
        d[i]=i*i
    print(d)
num(int(input("Enter the range:")))

#Question:4 => Write a program to find the factorial of a number given by use.
def fact(n):
    s=1
    for i in range(1, n + 1):
        s=s*i
    print(s)
fact(int(input("Enter the number u want the factorial:")))


#Question:5 => Write a program to print multipication table of a givennumber.
def num(n,r):
    for i in range(1,r+1):
        a=n*i
        print(" {} X {} = {}".format(n,i,a))
n=int(input("Enter the number:"))
r=int(input("Enter the range:"))
num(n,r)

#Question:6 => Write a program to print all prime number from 0 to 100.
#Python program to display all the prime numbers within an interval

def prime():
    for num in range(0, 100 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
prime()

#Question:7 => Use a loop to display element from a given list present at odd index position.
l=[12,34,56,78,90,98,76,54,32,10]
for i in range(len(l)):
    if i % 2 != 0:
        print("{} on position of {}".format(l[i],i))

#Question:8 =>  Find sum of all elements in the given list l=[18,82[57,59,73],33,29,58]
l = [18, 82,[57, 59, 73], 33, 29, 58]
a = 0
for i in range(len(l)):
    if type(l[i]) == type(l):
        for j in l[i]:
            a += j

    else:

        a += l[i]
print(a)

#Question:9 => Write a program to print all the string starting from "N" in a list.
r=int(input("Enter the range:"))
l=[]
for i in range(0,r):
    v=input("Enter your sentence:")
    l.append(v)
for i in l:
    for j in i:
        if j[0]=="N" or j[0]=="n":
            print(i)

#Question:10 => Write a program to print a square of second half of elements of a list.
r=int(input("Enter the range:"))
l=[]
for i in range(r):
    v=int(input("Enter:"))
    l.append(v)
for i in range(len(l)):
    if l[i]%2==0:
        a=l[i]**2
        print("The square of number {} on position {} is {}".format(l[i],i,a))
    else:
        print()