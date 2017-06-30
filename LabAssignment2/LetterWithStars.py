result_str="";  #creating an empty string
#defining 7 rows, 7 columns and writing a nested loop for each row and column
for row in range(0,7):
    for column in range(0,7):
        if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or (column == 1 and (row == 1 or row == 2 or row == 6)) or (column == 5 and (row == 0 or row == 4 or row == 5))):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str);