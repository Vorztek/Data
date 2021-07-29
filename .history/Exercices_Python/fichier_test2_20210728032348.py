# Python code to demonstrate calling the 
# function from another function
  
def verif_premier(p):
    # computes the Square of the given number 
    # and return to the caller function
    if p < 2:
        return False
    for j in range(2, p):
        if p % j == 0:
            return False
    else:
        return True
  
def SumofSquares(Array, n):
  
    # Initialize variable Sum to 0. It stores the 
    # Total sum of squares of the array of elements
    Sum = 0
    for i in range(n):
  
        # Square of Array[i] element is stored in SquaredValue
        SquaredValue = Square(Array[i])
  
        # Cummulative sum is stored in Sum variable
        Sum += SquaredValue
    return Sum
  
# Driver Function
Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(Array)
  
# Return value from the function 
# Sum of Squares is stored in Total
Total = SumofSquares(Array, n)
print("Sum of the Square of List of Numbers:", Total)