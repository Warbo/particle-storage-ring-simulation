#!/usr/bin/env python

import Matrix

class Particle(object):                  # matrix: [Matrix::Matrix], lost: [list(int)]

	def __init__(self, matrix):             # self: [Particle], matrix: [Matrix::Matrix]
		self.matrix = matrix                   # [Matrix::Matrix]
		self.lost = [False, False]             # [list(int)]

	def make_particle(self, x, y, x_divergence, y_divergence): # self: [Particle], x: [float], y: [float], x_divergence: [float], y_divergence: [float]
		return Particle(Matrix.m.make_matrix([[x],[x_divergence],[y],[y_divergence]])) # [Particle]

	#make_particle = staticmethod(make_particle)

	def __str__(self):                      # self: [Particle]
		return 'P' + str(self.matrix)          # [str]

p = Particle(Matrix.m)                   # [Particle]

if __name__ == '__main__':               # []
	test_particle = p.make_particle(1.0, 2.0, 3.0, 4.0) # [Particle]
	print test_particle.__str__()           # [str]
