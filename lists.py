#!/usr/bin/python
import sys

def main():
	pets = ['Marley', 'Minnie', 'Chinook', 'Rayne', 'Maya', 'Blue']
	cats = pets[0:2]
	dogs = pets [2:]

	print '\nLook at all my critter friends!'
	for p in pets:
		print p

	print '\nCat inventory:'
	for crit in cats:
		print crit
	print '\nDog inventory'
	for crit in dogs:
		print crit

	if 'Chinook' in dogs:
		print '\nChinook Tatuk is the best!'

	print 'Adding some new dogs and sorting the list'
	dogs.append('Jasper')
	dogs.append('Murphy')

	print '\nDog inventory'
	dogs.sort()
	for crit in dogs:
		print crit

	#printnums()

def printnums():
	print 'Obligitory number printing'
	for int in range (51):
		print int;

if __name__ == '__main__':
	main()