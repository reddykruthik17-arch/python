'''
import keyword
print(keyword.kwlist)
a=None
print(a)
a=0
print(type(a))
print(bool(a))
print(bool(0.0))
print(bool(1.8))
print(int())

a=3j+5
print(a)
a="happy father's day"
print(a)
print(a[6])

List
my_list = [1,2,3,4,'hello',5.6,True]
print(my_list[4])
print(my_list[4][0])

my_list.append(10)
print(my_list)

print(my_list.pop())
print(my_list)

tuple
my_tuple = (1,2,3,4,'hello',5.6,True)
print(type(my_tuple))

set
my_set = {1,2,3,4,'hello',5.6,True}
print(type(my_set))
print(my_set)

dictionary
my_dict = {'a':1, 'b':[10,20,30],'c':3}
print(type(my_dict))
print(my_dict)

my_dict['d'] = 4
print(my_dict)

print(my_dict['b'][1])

slicing
a="hello world"
print(a[0:5])
print(a[6:11])
print(a[2:4])
print(a[2:3+1:3])

a="hello world"
print(a[::-1])

a="good morning"

'odM'

print(a[1:5+1:2])

'mrG'
print(a[-7::3])
a= 'Good Morning'
a=eval(input("enter:"))
print(a,type(a))


if a%2==0:
    print("even")
else:
    print("odd")

list=eval(input("enter a list:"))
if len(list)==5:
    print("yes")
else:
    print("no")   

ch=input("enter a character:")
if "A"<=ch<="Z":
    print("uppercase")
if "a"<=ch<="z":
    print("lowercase")

username="kruthik"
password="1234"
u=input("enter a username:")
p=input("enter a password:")
if u==username and p==password:
    print("login successfull")
else:
    print("invalid credintials")

i=2
while i<=50:
    print(i)
    i+=2


n=int(input("Enter a number: "))
rev=0
while(n>0):
    ld=n%10
    n=n//10
    rev=rev*10+ld
print(rev)



l={10,20,30}
for i in l:
    print(i)

ch=input("Enter:")
for ch in ch:
    if "A"<=ch<="Z":
        print(chr(ord(ch)+32))
    elif "a"<=ch<="z":
        print(chr(ord(ch)-32))
    else:
        print("Not a letter")


s=input("Enter a string: ")
rev=""
for i in s:
    rev=i+rev
print(rev)


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()'''

'''#without Args and no return
def convert_no_args_no_return():
    s=input("enter a string:")
    out=""
    for i in s:
        if "A"<=i<="Z":
            out+=chr(ord(i)+32)
        elif "a"<=i<="z":
            out+=chr(ord(i)-32)
        else:
            out+=i
            print(out)
            convert_no_args_no_return()'''
'''class college:
    cname="gopalan college of engineering and management"
    cloc="hoodi"
    cnumber=1234567
s1=college()
print(s1.cname,s1.cloc)
college.cloc="bangalore"
print(college.cloc)
print(s1.cloc)
print("changing location wrt object")
s1.cloc="davengere"
print(s1.cloc)
print(college.cloc)
print(s1.cnumber)'''

class college:
    def __init__(self,name,loc,number):
        self.cname=name
        self.cloc=loc
        self.cnumber=number
    def display(self):
        print("college name:",self.cname)
        print("college locattion:",self.cloc)
        print("college number:",self.cnumber)
s1=college("gopalan","hoodi",1234567)
print(s1.cname,s1.cloc,s1.cnumber)
s1.display()




        
     


