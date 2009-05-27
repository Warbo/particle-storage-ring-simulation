#!/usr/bin/env python
import Particle
import Matrix

class RingSection(object):               # matrix: [Matrix::Matrix]

	def __init__(self, matrix):             # self: [RingSection], matrix: [Matrix::Matrix]
		self.matrix = matrix                   # [Matrix::Matrix]

	def __mul__(self, particle):            # self: [RingSection], particle: [Particle::Particle]
		lost = particle.lost                   # [list(int)]
		to_return = Particle.Particle(self.matrix.__mul__(particle.matrix)) # [Particle::Particle]
		to_return.lost = lost                  # [list(int)]
		return to_return                       # [Particle::Particle]

if __name__ == '__main__':               # []
	test_section = RingSection(Matrix.m.make_matrix([ \ # [RingSection]
		[1.,0.,0.,0.], \                       # [list(float)]
		[0.,1.,0.,0.], \                       # [list(float)]
		[0.,0.,1.,0.], \                       # [list(float)]
		[0.,0.,0.,1.] \                        # [list(float)]
		]))
	test_particle = \                       # [Particle::Particle]
		test_section * Particle.p.make_particle(1.0, 2.0, 3.0, 4.0) # [Particle::Particle]
