#!/usr/bin/env python
import RingSection
import Matrix
import Particle

class EscapeException(Exception):
	pass

class Ring(object):

	def __init__(self, ring_sections, particles, xmax, ymax):
		self.particles = particles
		self.sections = ring_sections
		self.xmax = xmax
		self.ymax = ymax

	def step(self, steps):
		for particle in self.particles:
			steps_taken = 0
			try:
				for section in self.sections:
					if steps_taken >= steps:
						raise EscapeException()
					if self.is_escaped(particle):
						raise EscapeException()
					particle = section * particle
					steps_taken += 1
			except EscapeException:
				pass

	def is_escaped(self, particle):
		if abs(particle.matrix['0,0']) > self.xmax:
			particle.lost[0] = True
		if abs(particle.matrix['2,0']) > self.ymax:
			particle.lost[1] = True
		return any(particle.lost)
