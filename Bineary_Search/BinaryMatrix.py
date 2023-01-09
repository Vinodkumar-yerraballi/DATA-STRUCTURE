#Let's define the function for bineary serching the 2D matrix
def Matrix_searching(matrix,target):
    #find the rows of the matrix
    m=len(matrix)
    # define a condition when the row will be zero it's return to false
    if m==0:
        return False
    #let's find the number of columns 
    n=len(matrix[0])
    #find the starting and ending index of the matrix
    #we take the left index=0
    # And we find the last index will be multiply the rows and columns substract with -1
    left,right=0,m*n-1
    #find the middle number
    while left<=right:
        mid=left+(right-left)//2
        #how to find the middle number in the matix
        #find the row_number in the matrix row_number=mid//n it means midle number divided by columns
        # find the column in the matrix column=mid%n if means mid number divided by column it return the remainder
        mid_element=matrix[mid//n][mid%n]
        if target==mid_element:
            return True
        elif  target < mid_element:
            right=mid-1
        else:
            left=mid+1
    return False


# create a 2D matrix
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#define the target variable
target=5
#calling the function
result=Matrix_searching(matrix,target)
print(result)