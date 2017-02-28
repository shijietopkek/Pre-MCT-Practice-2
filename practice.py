import random

def display():
    global arr1, arr2
    print("Matrix 1")
    for i in arr1:
        for j in i:
            print(j, end=' ')
        print()
    print("Matrix 2")
    for i in arr2:
        for j in i:
            print(j, end=' ')
        print()
    print()
    
def sum_matrix():
    global arr1, arr2
    print("Sum")
    row_1, col_1 = len(arr1[0]), len(arr1)
    row_2, col_2 = len(arr2[0]), len(arr2)
    
    if row_1 == row_2 and col_1 == col_2:
        for i in range(col_1):
            for j in range(row_1):
                print(arr1[i][j] + arr2[i][j], end=' ')
                
            print()
        print()
    else:
        print("NIL")
        
def product_matrix():
    global arr1, arr2
    print("Product")
    row_1, col_1 = len(arr1[0]), len(arr1)
    row_2, col_2 = len(arr2[0]), len(arr2)
    if row_1 == col_2 :
        for i in range(col_1):
            for j in range(row_2):
                count=0
                for k in range(col_2):
                    count += arr1[i][k] * arr2[k][j]
                print(count, end= " ")
            print()
        print()
    elif row_2 == col_1:
        for i in range(col_2):
            for j in range(row_1):
                count=0
                for k in range(col_1):
                    count += arr1[i][k] * arr2[k][j]
                print(count, end= " ")
            print()
        print()
    else:
        print("NIL")
        
    
    
    
#main
arr=[]
end_program = False
for i in range(2):
    print("Matrix {}".format(i+1))
    accepted = True
    accepted1= True
    range_of_values = ["-1","1","2","3","4","5"]
    while accepted:   
        m = input("Enter m: ")
        if m not in range_of_values or (m not in arr and i==1):
            print("Try again!")
        else:
            accepted = False
        
    while accepted1:
        n = input("Enter n: ")
        if n not in range_of_values or (n not in arr and i==1):
            print("Try again!")
        else:
            accepted1= False
    if n=="-1" or m=="-1":
        print("Bye!")
        end_program=True
        break;
    m = int(m)
    n = int(n)
    if i==0:
        arr.append(str(m))
        arr.append(str(n))
        arr1 = [[0 for element in range(n)] for elements in range(m)]
        for j in range(m):
            for k in range(n):
                number = random.randint(1,9)
                arr1[j][k] = number
    elif i==1:
        arr2 = [[0 for element in range(n)] for elements in range(m)]
        for j in range(m):
            for k in range(n):
                number = random.randint(1,9)
                arr2[j][k] = number

if end_program != True:
    display()
    sum_matrix()
    product_matrix()
                

