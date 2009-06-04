#!/usr/bin/env python
import Particle

class RingSection(object):

	def __init__(self, matrix):
		self.matrix = matrix

	def __mul__(self, particle):
		lost = particle.lost
		to_return = Particle.Particle(self.matrix * particle.matrix)
		to_return.lost = lost
		return to_return
