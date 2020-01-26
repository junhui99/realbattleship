import sys
r  = sys.argv[0] #number of row
c = sys.argv[1] #number of column
board = [['*' for row in range (r)] for col in range (c)]
print('  ' + ' '.join(map(str, (range(r)))))
# print the column labels along with the corresponding label
for col, sign in enumerate(board): # for each column, we first print the number of the column
    print(str(col) + ' ' + ' '.join(sign)) #then we print *