r  = 8 #row
c = 5 #col
board = [['*' for column in range(r)] for row in range(c)]
print(' ' + ' '.join(map(str, range(r)))) # print column labels
for row, item in enumerate(board): # for each row
    print(str(r)  + ' '.join(item))
