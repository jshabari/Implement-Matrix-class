import math
from math import sqrt
import numbers

def zeroes(height, width):    
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):    
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
    
class Matrix(object):
    
    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):        
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            det_A = self.g[0][0]
            return Matrix(det_A)
        
        elif self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            det_A = (a * d) - (b * c)
            return Matrix(det_A)            

    def trace(self):        
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        diagonal_sum = 0
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
 
        # TODO - your code here
        # Nested for loop to calculate the sum of diagonal matrix
        for i in range(len(self.g)):
            for j in range(len(self.g[0])):
                if (i == j):
                    diagonal_sum += self.g[i][j]
        return diagonal_sum

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverse = []
        inverse_row = [] 
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        if self.h == 1:
            inverse_row . append(1/float(self.g[0][0]))
            inverse . append (inverse_row)
            return Matrix(inverse)
            
        # TODO - your code here
        if self.h == 2:
            # Intializing variable to calculate determination
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            det_A = (a * d) - (b * c)
            
            # Intializing variable to implement[[d, -b], [-c, a]]
            self.g[0][0] = d
            self.g[0][1] = - b
            self.g[1][0] = - c
            self.g[1][1] = a
            
            # For loop to calculate the inverse 
            for i in range(len(self.g)):
                inverse_row = []
                for j in range(len(self.g[0])):
                    inverse_row . append ((1 / float(det_A)) * self.g[i][j])
                inverse . append(inverse_row)            
            return Matrix(inverse)  

    def T(self):        
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = []
        transpose_row = []
        
        # For loop to calculate the transpose of the matrix
        for i in range(len(self.g[0])):
            transpose_row = []
            for j in range(len(self.g)):
                transpose_row . append (self.g[j][i])
            transpose . append (transpose_row)
        return Matrix(transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):        
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        addition = []
        for i in range(len(self.g)):            
            addition_row = []
            for j in range(len(self.g[0])):
                addition_row.append(self.g[i][j] + other.g[i][j])
            addition.append(addition_row)
        return Matrix(addition)

    def __neg__(self):        
        """
        Defines the behavior of - operator (NOT subtraction) 

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        neg = []
        for i in range(len(self.g)):
            neg_row = []
            for j in range(len(self.g[0])):
                neg_row.append(-self.g[i][j])
            neg.append(neg_row)
        return Matrix(neg)

    def __sub__(self, other):        
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        subtraction = []
        for i in range(len(self.g)):            
            subtraction_row = []
            for j in range(len(self.g[0])):
                subtraction_row.append(self.g[i][j] - other.g[i][j])
            subtraction.append(subtraction_row)
        return Matrix(subtraction)

    def __mul__(self, other):        
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        # Function call for transpose of other matrix
        transpose_mul=Matrix.T(other)
        
        # Code for multiplication of two rows or list
        def dot_product(vector1, vector2):
            mul_sum = 0
            for i in range(len(vector1)):
                mul_sum += vector1[i] * vector2[i]
            return mul_sum
        
        # Variables for matrix    
        multiplication = []
        multiplication_row = []
        
        # For Loop for calculation of multiplication of two matrix
        for i in range(len(self.g)):
            multiplication_row = []
            for j in range(len(transpose_mul.g)):
                multiplication_row . append(dot_product(self.g[i], transpose_mul.g[j]))
            multiplication . append(multiplication_row)  
        return Matrix(multiplication)

    def __rmul__(self, other):        
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            rmulmatrix = []
            for i in range(len(self.g)):
                rmul_row = []
                for j in range(len(self.g[0])):
                    rmul_row.append(other * self.g[i][j])
                rmulmatrix.append(rmul_row)            
            return Matrix(rmulmatrix)
    
