#!/usr/bin/env python

class EscapeException(Exception):
	pass

class Ring(object):

	def __init__(self, ring_sections, particles):
		self.particles = particles
		self.sections = ring_sections

	def step(self, steps, is_escaped):
		for i from 0 <= i < len(self.particles)-1:
			particle = self.particles[i]
			steps_taken = 0
			try:
				for j from 0 <= j < len(self.sections)-1:
					section = self.sections[j]
					if steps_taken >= steps:
						raise EscapeException()
					self.particles[i] = section * particle
					if is_escaped(particle):
						raise EscapeException()
					steps_taken += 1
			except EscapeException:
				pass

