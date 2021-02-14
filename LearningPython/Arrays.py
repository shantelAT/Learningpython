import array #use to import array modules, to be able to use array

a = array.array( "i",[1,2,3,4,5,6]) # i represents INTEGERS the array type which is .
print(a)

 #ACCESSING ELEMENTS IN Array.
print(a[2])
print(a[-2])

#Length of array
b = len(a)
print(b)

#ADDING or changing things to an array

a.append(7)  #append adds element to the end of the array
print(a)

a.extend([9, 10]) #extend muliplw element to the end of the Array
print(a)


a.insert(7,8) #insert adda elements to specific selections of the Array
print(a)


#REMOVING ELEMENTS

a.pop((3))
print(a)

a.remove(7)
print(a)


#CONCAENATION

b = array.array("d", [2,4,6,8,10]) #d represents float numbers eg 2.2
c = array.array("d", [1,3,5,7,9])
d = array.array("d")
d = b+c
print(d)

#SLICING
f= d[::-1]
print(f)
print(d[2:6])

#LOOPS

for x in d:     #FOR LOOPS
    print(x)
i =1
while i < len(a):
  print(d[i])
  i += 1
