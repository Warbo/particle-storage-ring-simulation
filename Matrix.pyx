#!/usr/bin/env python

class Matrix(object):
	"""This custom class is a pure Python implementation of matrices."""

	def __init__(self, rows, columns):
		cdef int self.row_number
		cdef int self.column_number

		self.row_number = rows

		self.column_number = columns

		cdef double self.matrix[self.row_number][self.column_number]
		self.matrix = []
		for r in range(self.row_number):
			self.matrix.append(None)

		for row in range(self.row_number):
			cdef double new_column[self.column_number]

			new_column = []
			for column in range(self.column_number):
				new_column.append(0.0)
			self.matrix[row] = new_column

	def __setitem__(self, position, value):
		pos = position.split(',')
		row = int(pos[0])
		column = int(pos[1])
		self.matrix[row][column] = value

	def __getitem__(self, position):
		pos = position.split(',')
		row = int(pos[0])
		column = int(pos[1])
		return self.matrix[row][column]

	def make_matrix(self, values):
		"""Generates a matrix with values given in the (row-major)
		nested list given."""
		rows = len(values)
		columns = len(values[0])
		matrix = Matrix(rows, columns)
		for r, row in enumerate(values):
			for c, element in enumerate(row):
				matrix[str(r)+','+str(c)] = element
		return matrix

	#make_matrix = staticmethod(make_matrix)

	def get_column(self, index):
		column = []
		for row in self.matrix:
			column.append(row[index])
		return column

	#def get_row(self, index):
	#	return self.matrix[index]

	def __mul__ (self, other):
		"""Returns a Matrix of the result of multiplying this matrix
		with the given matrix."""

		# First check that multiplication is defined for these matrices
		if not self.column_number == other.row_number:
			raise ValueError("Matrix dimensions do not match.")

		# Now make the resulting matrix
		matrix = Matrix(self.row_number, other.column_number)

		# Now calculate each element of the new matrix
		for r, row in enumerate(matrix.matrix):
			for c, element in enumerate(row):

				# The current element is the sum of the elements of
				# this matrix's row and the other matrix's column
				for i in range(self.row_number):
					matrix[str(r)+','+str(c)] += \
						self.matrix[r][i] * other.get_column(c)[i]

		return matrix

	def __str__(self):
		return_string = "[\n"
		for row in self.matrix:
			return_string = return_string + ' ' + str(row) + '\n'
		return_string = return_string + ']'
		return return_string

cdef class CMatrix:

	cdef double values[4][4]

	def __init__(self, int rows, int columns):
		self.row_number = rows

		self.column_number = columns

		self.matrix = []
		#for r from 0 <= i < self.row_number-1:
		#	self.values[r] = 0.0

		for r from 0 <= i < self.row_number-1:
			#for row in range(self.row_number):
			#double new_column[self.row_number]
			for c from 0 <= i < self.column_number-1:
				#for column in range(self.column_number):
				values[r][c] = 0
			#self.matrix[row] = new_column

	def __mul__ (self, other):
		"""Returns a Matrix of the result of multiplying this matrix
		with the given matrix."""

		# First check that multiplication is defined for these matrices
		if not self.column_number == other.row_number:
			raise ValueError("Matrix dimensions do not match.")

		# Now make the resulting matrix
		matrix = Matrix(self.row_number, other.column_number)

		# Now calculate each element of the new matrix
		for r from 0 <= i < self.row_number-1:
			for c from 0 <= i < self.column_number-1:
				#for r, row in enumerate(matrix.matrix):
				#for c, element in enumerate(row):

				# The current element is the sum of the elements of
				# this matrix's row and the other matrix's column
				for i from 0 <= i < self.row_number-1:
					matrix[str(r)+','+str(c)] += \
						self.values[r][i] * other.get_column(c)[i]
		return matrix

m = Matrix(1,1)

if __name__ == '__main__':
	test1 = m.make_matrix([ \
		[1.0, 0.0, 0.0, 0.0], \
		[0.0, 1.0, 0.0, 0.0], \
		[0.0, 0.0, 1.0, 0.0], \
		[0.0, 0.0, 0.0, 1.0] \
		])
	test2 = m.make_matrix([ \
		[1.0], \
		[2.0], \
		[3.0], \
		[4.0] \
		])

	print str(test1*test2)
