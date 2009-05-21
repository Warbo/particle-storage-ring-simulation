#!/usr/bin/env python
import os
import sys

if sys.argv[1] == 'p':
	os.popen('pyrexc '+sys.argv[2]+'.pyx')
elif sys.argv[1] == 'b':
	os.popen('gcc -c -fPIC -I/usr/include/python2.5/ ' + sys.argv[2]+'.c')
elif sys.argv[1] == 'l':
	os.popen('gcc -shared '+sys.argv[2]+'.o -o '+sys.argv[2]+'.so')

print "Done"
