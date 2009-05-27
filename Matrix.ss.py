#!/usr/bin/env python

class Matrix:                            # matrix: [list(list(float))], column_number: [int], row_number: [int]
	"""This custom class is a pure Python implementation of matrices."""

	def __init__(self):                     # self: [Matrix]
		pass

	def init(self, rows, columns):          # self: [Matrix], rows: [int], columns: [int]
		self.row_number = rows                 # [int]

		self.column_number = columns           # [int]

		self.matrix = []                       # [list(list(float))]
		for r in range(self.row_number):       # [__iter(int)]
			self.matrix.append(None)              # [None]

		for row in range(self.row_number):     # [__iter(int)]
			new_column = []                       # [list(float)]
			for column in range(self.column_number): # [__iter(int)]
				new_column.append(0.0)               # [None]
			self.matrix[row] = new_column         # [list(float)]

	def __setitem__(self, position, value): # self: [Matrix], position: [str], value: [float]
		pos = position.split(',')              # [list(str)]
		row = int(pos[0])                      # [int]
		column = int(pos[1])                   # [int]
		self.matrix[row][column] = value       # [float]

	def __getitem__(self, position):        # self: [Matrix], position: [str]
		pos = position.split(',')              # [list(str)]
		row = int(pos[0])                      # [int]
		column = int(pos[1])                   # [int]
		return self.matrix[row][column]        # [float]

	def make_matrix(self, values):          # self: [Matrix], values: [list(list(float))]
		"""Generates a matrix with values given in the (row-major)
		nested list given."""
		rows = len(values)                     # [int]
		columns = len(values[0])               # [int]
		matrix = Matrix()                      # [Matrix]
		matrix.init(rows, columns)             # [None]
		for r, row in enumerate(values):       # [tuple(int, list(float))]
			for c, element in enumerate(row):     # [tuple(int, float)]
				matrix.__setitem__(str(r)+','+str(c), element) # [None]
		return matrix                          # [Matrix]

	#make_matrix = staticmethod(make_matrix)

	def get_column(self, index):            # self: [Matrix], index: [int]
		column = []                            # [list(float)]
		for row in self.matrix:                # [__iter(list(float))]
			column.append(row[index])             # [None]
		return column                          # [list(float)]

	#def get_row(self, index):
	#	return self.matrix[index]

	def __mul__ (self, other):              # self: [Matrix], other: [Matrix]
		"""Returns a Matrix of the result of multiplying this matrix
		with the given matrix."""

		# First check that multiplication is defined for these matrices
		if not self.column_number == other.row_number: # []
			raise ValueError("Matrix dimensions do not match.") # [ValueError]

		# Now make the resulting matrix
		matrix = Matrix()                      # [Matrix]
		matrix.init(self.row_number, other.column_number) # [None]

		# Now calculate each element of the new matrix
		for r, row in enumerate(matrix.matrix): # [tuple(int, list(float))]
			for c, element in enumerate(row):     # [tuple(int, float)]

				# The current element is the sum of the elements of
				# this matrix's row and the other matrix's column
				for i in range(self.row_number):     # [__iter(int)]
					matrix.__setitem__(str(r)+','+str(c), matrix.__getitem__(str(r)+','+str(c)) + self.matrix[r][i] * other.get_column(c)[i]) # [None]

		return matrix                          # [Matrix]

	def __str__(self):                      # self: [Matrix]
		return_string = "[\n"                  # [str]
		for row in self.matrix:                # [__iter(list(float))]
			return_string = return_string + ' ' + str(row) + '\n' # [str]
		return_string = return_string + ']'    # [str]
		return return_string                   # [str]

m = Matrix()                             # [Matrix]
m.init(1,1)                              # [None]

if __name__ == '__main__':               # []
	test1 = m.make_matrix([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]) # [Matrix]
	test2 = m.make_matrix([[1.0], [2.0], [3.0], [4.0]]) # [Matrix]

	print (test1.__mul__(test2)).__str__()  # [str]
	print (test1 * test2).__str__()         # [str]
