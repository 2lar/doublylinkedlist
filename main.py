# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:08:49 2021

@author: lawre
"""
import random
import linkedlist
l = linkedlist

sep = "--------"

x = l.doublylinkedlist()
for i in range(10):
    x.lappend(i)

x1 = l.doublylinkedlist()
for i in range(10,20):
    x1.lappend(i)
    
x2 = l.doublylinkedlist()
x2.lappend(50)
x2.lappend(40)
x2.lappend(60)
x2.lappend(7)
x2.lappend(91)

x3 = l.doublylinkedlist()
x4 = l.doublylinkedlist()
x6 = l.doublylinkedlist()
x7 = l.doublylinkedlist()
x5 = l.doublylinkedlist()
x8 = l.doublylinkedlist()
x9 = l.doublylinkedlist()

def a():
    x.printlist()
    x1.printlist()
    x2.printlist()
    x.reverselist()
    x.printlist()
    print()

def b():
    x3.copylist(x)
    x.printlist()
    x4.copylist(x3)
    x4.printlist()
    print(sep)
    for i in range(3):
        x3.deleteval(i)
    x.printlist()
    x3.printlist()
    x.deletelist()
    x.printlist()
    print("testing this node print")
    x9 = l.copyfromhead(x3.head.next.next)
    l.headprint(x9)
    print()

def c():
    print("testing pops, delete, change")
    for i in range(15):
        x.lappend(i)
    x.lappend(8)
    x.pushfront(9)
    x.printlist()
    x.deleteval(7)
    x.changeval(9,69)
    x.printlist()
    print()
    
def d():
    print("test sorting")
    for i in range(15):
        ran = random.randint(0,100)
        x5.lappend(ran)
    x5.printlist()
    x5.sorting()
    x5.printlist()
    print()
    
def e():
    print("join and similarity")
    jl1 = l.doublylinkedlist()
    jl2 = l.doublylinkedlist()
    jl3 = l.doublylinkedlist()
    jl4 = l.doublylinkedlist()
    jlist = [jl1,jl2,jl3,jl4]
    
    
    jcount = 0
    for j in jlist:
        for i in range(jcount, jcount+5):
            j.lappend(i)
        jcount+=5
        j.printlist()
        
    listofj = l.doublylinkedlist()
    listofj = l.multijoinedlists(jl1,jl2,jl3,jl4)
    listofj.printlist()
    print(listofj.size)
    
    print(l.howsimilar(jl1,jl2))
    print(l.howsimilar(jl1,listofj))
    print(l.howsimilar(jl1,jl1))
    print()

def f():
    print("test string data")
    jl1 = l.doublylinkedlist()
    jl2 = l.doublylinkedlist()
    jl3 = l.doublylinkedlist()
    jl4 = l.doublylinkedlist()
    jlist = [jl1,jl2,jl3,jl4]
    jcount = 0
    for j in jlist:
        for i in range(jcount, jcount+5):
            j.lappend("hellow world")
        jcount+=5
        j.printlist()
        

if __name__ == "__main__":
    a()
    b()
    c()
    d()
    e()
    f()
        
    