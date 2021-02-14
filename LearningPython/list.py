
#QUESTION1

list1= [1,2,3,4,5]
list2 = [6,7,3,4,1,8,9]

#Create new list with no duplicate
# Example [1,2,3,4,5,6,7,8,9]

list3 = list1 + list2
print(list3)
list4=[]

for x in list3:
    if x not in list4:
        list4.append(x)
    else:
        continue

print(list4)


#QUESTION2 - Transpose the rows into colomn to create
#transpose_matrix = [
#           [1, 4, 7],
#           [2, 5, 8],
#           [3, 6, 9]
#                ]


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# [ [1,2,3], [4,5,6], [7,8,9] ]

print(matrix[0])

transpose = []
cols = len(matrix[0])
print(cols)
for i in range (cols):
    t_row =[]
    for row in matrix:
        t_row.append(row[i])
    transpose.append(t_row)

print(transpose)

print([[row[i] for row in matrix] for i in range(cols)])
