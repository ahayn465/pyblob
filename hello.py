#!/usr/bin/python
import sys

def main():
	print "Hello World"

	a = "Hello "
	num = 12
	b = "World"
	c= "Why are you so cruel?"

	def string(a, b , num, c):
		print "\nShall we print some strings?\n"
		print a + b
		print a * num
		print c.upper()
		story1 = ('One %s, there was a %s %s...' % 
			('night', 'wild and crazy', 'party'))
		story2 = ('%d %s were there.' %
			(12, 'bears'))

		print story1 + story2
		
		def optimistic(c, check, num):
			if num == check:
				print c.replace('cruel','awesome')			
			elif num > check:
				print c.replace('cruel', 'big')
			else:
				print c.replace('cruel','dark')

		optimistic(c,12,num)
		optimistic(c, 15, num)
		optimistic(c,5,num)

	string(a, b, num, c)


	def splits():
		print "\nNow moving on to some slices... \n"
		print c.split()
		print c[4]+c[15]+c[18]
		print b[1:4]		
		print a[1:]
		print c[15]+c[4]+b[2]


	splits()

	



if __name__ == '__main__':
	main()