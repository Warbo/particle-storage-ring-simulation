#!/usr/bin/env python
import Particle
import Matrix

class RingSection(object):

	def __init__(self, matrix):
		self.matrix = matrix

	def __mul__(self, particle):
		lost = particle.lost
		to_return = Particle.Particle(self.matrix.__mul__(particle.matrix))
		to_return.lost = lost
		return to_return

if __name__ == '__main__':
	test_section = RingSection(Matrix.m.make_matrix([ \
		[1.,0.,0.,0.], \
		[0.,1.,0.,0.], \
		[0.,0.,1.,0.], \
		[0.,0.,0.,1.] \
		]))
	test_particle = \
		test_section * Particle.p.make_particle(1.0, 2.0, 3.0, 4.0)
