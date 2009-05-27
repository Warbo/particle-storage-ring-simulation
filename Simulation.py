import Ring
import RingSection
import Particle
import Matrix
import math
import random

def make_particles(number, xmax, ymax, xpmax, ypmax):
	particles = []
	for index in range(number):
		particles.append(Particle.p.make_particle(\
			(random.random()*2*xmax)-xmax, \
			(random.random()*2*ymax)-ymax, \
			(random.random()*2*xpmax)-xpmax, \
			(random.random()*2*ypmax)-ypmax))
	return particles

def count_x_lost(particles):
	count = 0
	for particle in particles:
		if particle.lost[0]:
			count += 1
	return count

def count_y_lost(particles):
	count = 0
	for particle in particles:
		if particle.lost[1]:
			count += 1
	return count

def count_lost(particles):
	count = 0
	for particle in particles:
		if any(particle.lost):
			count += 1
	return count

n_steps = 20
particles = 10
ring_steps = 40.
total_steps = ring_steps * 50
r0 = 2.
xmax = 0.03
ymax = 0.03
xpmax = xmax/r0
ypmax = ymax/r0

#def is_escaped(particle):
#	if abs(particle.matrix['0,0']) > xmax:
#		particle.lost[0] = True
#	if abs(particle.matrix['2,0']) > ymax:
#		particle.lost[1] = True
#	return any(particle.lost)

dz = (2 * r0 * math.pi) / ring_steps

ns = [float(x)/n_steps for x in range(1, n_steps)]

rings = []

for n in ns:
	ring_matrix = Matrix.m.make_matrix([\
		[math.cos(((1-n)**0.5)*(dz/r0)), (r0/((1-n)**0.5))*math.sin(((1-n)**0.5)*(dz/r0)),0.0,0.0],\
		[-1. * (((1-n)**0.5)/r0)*math.sin(((1-n)**0.5)*(dz/r0)), math.cos(((1-n)**0.5)*(dz/r0)),0.0,0.0],\
		[0.0,0.0,math.cos((n**0.5)*(dz/r0)), (r0/(n**0.5))*math.sin((n**0.5)*(dz/r0))],\
		[0.0,0.0,-1. * ((n**0.5)/r0)*math.sin((n**0.5)*(dz/r0)), math.cos((n**0.5)*(dz/r0))]
		])

	empty_matrix = Matrix.m.make_matrix([\
		[math.cos(dz/r0), r0*math.sin(dz/r0),0.0,0.0],\
		[(-1.0/r0)*math.sin(dz/r0), math.cos(dz/r0),0.0,0.0],\
		[0.0,0.0,1.0,dz],\
		[0.0,0.0,0.0,1.0]\
		])

	sections = []

	# NO GAPS
	for x in range(int(ring_steps)):
		sections.append(RingSection.RingSection(ring_matrix))

	# 2 GAPS OF 5%
	#for x in range((int(ring_steps)/2) - 2):
	#	sections.append(RingSection.RingSection(ring_matrix))
	#for x in range(2):
	#	sections.append(RingSection.RingSection(empty_matrix))
	#for x in range((int(ring_steps)/2) - 2):
	#	sections.append(RingSection.RingSection(ring_matrix))
	#for x in range(2):
	#	sections.append(RingSection.RingSection(empty_matrix))

	rings.append(Ring.Ring(sections, make_particles(particles, xmax, ymax, xpmax, ypmax), xmax, ymax))

for x, ring in enumerate(rings):
	ring.step(total_steps)
	print str(len(rings) - x)

out = ["n, remaining, xlost, ylost"]

for x, ring in enumerate(rings):
	out.append(str(ns[x]) + ', ' + str(particles - count_lost(ring.particles)) + ', ' + str(particles - count_x_lost(ring.particles)) + ', ' + str(particles - count_y_lost(ring.particles)))

outfile = open("OUT.csv", "w")
for line in out:
	outfile.write(line + '\n')
outfile.close()
