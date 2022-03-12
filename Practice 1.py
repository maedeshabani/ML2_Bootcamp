#!/usr/bin/env python
# coding: utf-8

# In[17]:


def sphere_volume(r:float):
    pi=3.14
    volume =4/3*pi*r**3
    return(volume)

sphere_volume(5.3)


def odd_even(number:int):
    if number%2==0:
        print("even")
    else:
        print("odd")

odd_even(19)
odd_even(-2)

def max_numbers(a,b,c):
    if a>b and a>c:
        print("max is :{}".format(a))
    if b>a and b>c:
        print("max is :{}".format(b))
    if c>a and c>b:
        print("max is :{}".format(c))

max_numbers(28,12,40)

def min_numbers(a,b,c):
    if a<b and a<c:
        print("min is :{}".format(a))
    if b<a and b<c:
        print("min is :{}".format(b))
    if c<a and c<b:
        print("min is :{}".format(c))

min_numbers(15,39,12)


def max_and_min_numbers(a,b,c):
    list=[a,b,c]
    print("max is:{}".format(max(list)))
    print("min is:{}".format(min(list)))

max_and_min_numbers(12,15,1)


def even_100():
    result=[]
    i=1
    while i<100:
        if i%2==0:
            result.append(i)
        i=i+1
    return result

even_100()

def my_multiple(x:int,y:int):
    i=0
    while i<y:
        x+=x
        i+=1
    print(x)


def multiple_4():
    result=[]
    for i in range (22,105):
        if i%4==0 :
            result.append(i)
    return result

multiple_4()


def mul5_nor3():
    result=[]
    for i in range (200,20,-1):
        if i%3 !=0 and i%5==0:
            result.append(i)
    return result

mul5_nor3()


for i in range (1,11):
    for j in range(1,11):
        print(i*j,"",end='')
    print()


def parallelgram(a,b:int):
    for i in range(1,b+1):
        if i==1:
            print(" " * b, "*" * b);
        if i==b:
            print(" " * (b-i), "*" * b);
        else:
            print(" " *(a-i),"*" ," "(a-2),"*");


# In[143]:


parallelgram(5,4)

message ="Babak Khorramdin"
message[0]
message.find("K")
message[6]
message.split()
message.partition(" ")
message[:12:2]
for i in message:
    if i == "m":
        print("True")
        break
    


from random import randint
def guess_num(number:int):
    for i in range(5):
         while i<5 and number ==randint(1,20):
                return "You Win"
    i=i+1
    return "Game Over"
randint(1,20)
guess_num(19)