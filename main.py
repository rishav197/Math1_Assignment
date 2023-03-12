from sympy import *

def checkNullVect(vector):
    return (vector.count(0)==len(vector))


def main():

    """AX=0"""

    rows = int(input("rows = "))
    cols = int(input("cols = "))

    A = []

    for i in range(rows):
        temp = []
        for j in range(cols):
            # print(i, j)
            num = int(input())
            temp.append(num)
        A.append(temp)
    print("A =",A)


    # A = [[1,-1,-1,3], [1,1,-2,1], [4,-2,4,1]] #3x4 tc-1

    # A = [[3,5,-4], [-3,-2,4], [6,1,-8]] #3x3 tc-2

    # A = [[1,-2,-1,3,0],[-2,4,5,-5,3],[3,-6,-6,8,2]] #3x5 tc-3

    # A = [[1,0,0],[0,2,0],[0,0,1],[0,1,3]] #4x3 tc-4

    # A = [[1,6,2,-5,-2,-4],[0,0,2,-8,-1,3],[0,0,0,0,1,7]] #3x6 tc-5

    # A = [[0,0,2,0,4],[0,8,0,0,1],[8,0,9,0,3],[8,0,0,5,1]] #4x5 tc-6
    
    # A = [[0,0,3],[0,5,6],[0,8,9]] #3x3 tc-7

    # A = [[0,0,3,5,6,8,-9],[0,5,6,2,1,0,3],[1,8,-9,1,5,7,0],[0,8,-9,1,5,7,0],[5,8,-9,1,5,7,0]] #5x7 tc-8

    # A = [[0,0,3,5,6,8,-9,11,4],[0,0,6,2,1,0,3,2,1],[1,8,-9,1,5,7,0,-6,-1],[0,0,-9,1,5,7,0,14,-1],[5,0,-9,1,5,7,0,3,0]] #5x9 tc-9

    rows = len(A)
    cols = len(A[0])


    print("Given:")
    print(A)
    M = Matrix(A) #converting A into sympy matrix
    rref_M = M.rref() #calculating rref of the matrix A
    # print(rref_M[1], type(rref_M[1]))
    
    rref_A = Matrix(rref_M[0]).tolist()
    pivots = list(Matrix(rref_M[1]))
    print("Pivots:")
    print(pivots)

    print("RREF:")
    print(rref_A)
    # print(2*rref_A[0][2], type(rref_A[0][2]))


    # RREF Done here

    #for  parametric solutions
    rows = len(rref_A)
    cols = len(rref_A[0])
    
    if(len(pivots)==cols):
        print("Solution:")
        print([0 for i in range(len(pivots))])
    
    else:
        freevect=[]
        fcol={}
        for i in range(cols):
            if i not in pivots:
                fcol[i]="x"+str(i+1)
                temp=[]
                for j in range(rows):
                    temp.append(rref_A[j][i])
                freevect.append(temp)
        # print("freevect = ", freevect)
        # print("fcol = ", fcol)
        t=[]
        for i in range(cols):
            t.append(0)
        print("Solution:")
        print(t,end="+")
        for i in range(len(freevect)):
            temp=[]
            k=0
            for j in range(cols):
                if j==list(fcol.keys())[i]:
                    temp.append(1)
                elif j in fcol.keys():
                    temp.append(0)
                elif j>list(fcol.keys())[i]:
                    temp.append(0)
                else:
                    temp.append(-1*freevect[i][k])
                    k+=1
            # print("temp = ", temp)
            if i == len(freevect)-1:   
                print(fcol[list(fcol.keys())[i]],"*",temp,sep="")
            else:
                print(fcol[list(fcol.keys())[i]],"*",temp,sep="",end="+")
    


if __name__ == "__main__":
    main()
    