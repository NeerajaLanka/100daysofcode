position  = 12    #this variable position we never used.
row1 =["x1","x2","x3"]
row2 =["y1","y2","y3"]#usually matrix count by 3*3...so 1st row,2nd row,3rd row and 1st column,2nd column,3rd column.
row3 =["z1","z2","z3"]#but for counting by index it start from 0 and 1 and 2
matrix = []
matrix.append(row1)
matrix.append(row2)
matrix.append(row3)
print(matrix)
print(f"{row1}\n{row2}\n{row3}\n")
print(matrix[1][2])
matrix[1].pop(2)     #this method removes element in nested list
matrix[1].insert(2,"t") #this method inserts element in nested list
print(f"{row1}\n{row2}\n{row3}\n")





