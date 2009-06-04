#!/usr/bin/env python

import Matrix

class Particle(object):

	def __init__(self, matrix):
		self.matrix = matrix
		self.lost = [False, False]

	def make_particle(self, x, y, x_divergence, y_divergence):
		return Particle(Matrix.m.make_matrix([[x],[x_divergence],[y],[y_divergence]]))

	def __str__(self):
		return 'P' + str(self.matrix)

p = Particle(Matrix.m)
