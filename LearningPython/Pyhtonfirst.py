import array

a = array.array( "i",[1,2,3,4,5,6]) #conttructorname.
print(a)

 #Acessing Array Elemnt.
print(a[2])
print(a[-2])

#Length of array
b=len(a)
print(b)
#addding or changing things to an array

a.append(7)  #append adds element to the end of the array
print(a)

a.extend([9, 10]) #extend muliplw element to the end of the Array
print(a)


a.insert(7,8) #insert adda elements to specific selections of the Array
print(a)
