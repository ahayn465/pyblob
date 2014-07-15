#!/usr/bin/python
import sys


def main():

	#fucntion to demonstrate list sorting with keys
	def key_sort():
		dogs = ['Chinook', 'Rayne', 'Maya', 'Blue', 'Jasper', 'Murphy']
		
		print '\nSorting by length of word'
		s1 = sorted(dogs, key=len)
		for dog in s1:
			print dog
		print '\n'	

		print 'Sorting by length of word in reverse order'
		s2 = sorted(dogs, key=len, reverse=True)
		for hound in s2:
			print hound
		print '\n'
		

	# fucntion to show practice with tuples	
	def tuple_practice():
		print 'Gorgeous colours:'
		colours = ('Blue', 'Green', 'Purple', 'Yellow', 'Pink')

		for hue in colours:
			print hue

	def list_comprehension():
					
		def is_prime(num):
			prime = True
			for i in range(2, num):
				if num % i == 0:
					prime = False
			if prime:
				print num
				return num

		comprehended = [i for i in range (300, 350) if is_prime(i)]

		print '\nUsing list comprehension to find prime numbers between 300 and 350'
		for prime in comprehended:
			print prime


	#function calls	
	key_sort()
	tuple_practice()
	list_comprehension()



if __name__ == '__main__':
	main()