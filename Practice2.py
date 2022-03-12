from operator import index
from typing import Tuple
from logging import exception

#in function faghat avalin javabe zip ra barmigardanad.
def custom_zip(iterator1:iter,iterator2:iter):
    for x in range(min(len(iterator1),len(iterator2))):
        for i in iterator1:
            for j in iterator2:
                if iterator1.index(i)==iterator2.index(j):
                    return(i,j)
                

def custom_zip(iterator1:iter,iterator2:iter):
    x=map(lambda a,b:(a,b),iterator1,iterator2)
    return list(x)

tuple1 =("Mazda","BMW","Lexus","Peugeot")
tuple2 =("Red","Blue","Green")
custom_zip(tuple1,tuple2)


def transpose_matrix(matA:list[list]): 
    matB=[[0 for x in range(len(matA))]for y in range(len(matA[0]))]
    for i in range(len(matA)):
        for j in range(len(matA[0])):
            matB[j][i]=matA[i][j]
    return matB

mat1=[[3,5,9,4],[6,1,7,8]]
transpose_matrix(mat1)




def matrix_multiply(A:list[list],B:list[list]) :
    A_row = len(A)
    A_col = (lambda A=A:len(A[0]) if len(A)>0 else 0)()
    B_row = len(B)
    B_col = (lambda B=B:len(B[0]) if len(B)>0 else 0)()
    
    if A_col == B_row:
       result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    for r in result:
        print (r)

mat1=[[3,5],[6,1]]
mat2=[[2,7,6],[9,2,8]]
matrix_multiply(mat1,mat2)


def determinant_recursive(A, total=0):
    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
 
    for fc in indices: 
        As = (A).copy() 
        As = As[1:] 
        height = len(As)  
 
        for i in range(height): 
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2) 
        sub_det = determinant_recursive(As)
        total += sign * A[0][fc] * sub_det 
 
    return total

mat3 =[[2,7,6],[9,2,8],[1,7,5]]
determinant_recursive(mat3)
