#!/usr/bin/env python

class EscapeException(Exception):
	pass

class Ring(object):

	def __init__(self, ring_sections, particles):
		self.particles = particles
		self.sections = ring_sections

	def step(self, steps, is_escaped):
		for particle in self.particles:
			steps_taken = 0
			try:
				for section in self.sections:
					if steps_taken >= steps:
						raise EscapeException()
					particle = section * particle
					if is_escaped(particle):
						raise EscapeException()
					steps_taken += 1
			except EscapeException:
				pass
