import sys
r  = 10#number of row
c = 7 #number of column
#we set the board array
board = [['*' for row in range (r)] for col in range (c)]
print('  ' + ' '.join(str(r) for r in range (r)))
# print the column labels along with the corresponding label
for col, dot in enumerate(board):
# for each column, we first print the number of the column, then we print "*"
    print(str(col) + ' ' + ' '.join(dot))
