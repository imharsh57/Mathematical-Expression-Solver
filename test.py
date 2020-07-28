# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:56:37 2019

@author: Harsh Anand
"""

n1=int(input())
even=[]
odd=[]
for i in range(n1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
n1_list=[]
for i in range(n1):
    t=int(input())
    n1_list.append(t)
n2=int(input())
n2_list=[]
for i in range(n2):
    t=int(input())
    n2_list.append(t)
even_odd = input()
temp1=[]
temp2=[]
if even_odd=="Even":
    for i in even:
        x=n1_list[i]-n2_list[i]
        temp1.append(x)
        y=n2_list[i]-n1_list[i]
        temp2.append(y)
elif even_odd=="Odd":
    for i in odd:
        x=n1_list[i]-n2_list[i]
        temp1.append(x)
        y=n2_list[i]-n1_list[i]
        temp2.append(y)
temp1=sum(temp1)
temp2=sum(temp2)
if temp1>temp2:
    print("Andrea")
elif temp2>temp1:
    print("Maria")
else:
    print("Tie")
    
    