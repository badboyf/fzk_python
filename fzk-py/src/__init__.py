# -*- coding: utf-8 -*-  


n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(n[::-1])
print([1,2] + [3,4])
print([1,2] * 10)
name=list('Python')
print(name)
name[2:]=list('Dev')
print(name)
n=[1,5]
n[1:1]=[2,3,4]
print(n)
n.append(6)
n[len(n):]=[7]
print(n)
n.count(1)
#extend    a + b    slice
print(n.index(7, 0, len(n)))
n.insert(len(n), 8)
n.insert(20, 9)
print(len(n))
n.pop()   #right
n.pop(0)
n[len(n):]=[2,2,2,2]
n.remove(2)
n.reverse()
n.sort()
m=sorted(n)
print(n)

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len, reverse=False)
print(x)

f = "Hello, %s. %s enough for ya"
v = ("Word", "Hot")
print(f % v)
