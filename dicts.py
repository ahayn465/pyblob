#!/usr/bin/python
import sys

def main():

	def dict_practice():
		animals = {}
		animals['Marley'] = 'cat'
		animals['Minnie'] = 'cat'
		animals['Chinook'] = 'dog'
		animals['Rayne']  = 'dog'
		animals['Maya']  = 'dog'
		animals['Jasper']  = 'dog'
		animals['Blue']  = 'dog'

		#print the keys and values for every item in the dict
		print animals.items()
		#sort the dict and print the key followed by the value
		
		print '\nPrint all the animals in key sorted order'
		for crit in sorted(animals.keys()):
			print crit#, animals[crit]
		
		print '\nWhat are they anyways?'
		#loop over the items() tuple list to display one key value 
		#pair on each itteration
		for k, v in animals.items(): print k, 'is a', v
		
		print '\nPoor Jasper moved away.. lets remove her'
		del animals['Jasper']
		for crit in sorted(animals.keys()):
			print crit#, animals[crit]

		return animals

	#get the dict from dict_practice to send to another funtion
	animals= dict_practice()
	
	#us the dict from dict_practice for file testing
	def file_practice(animals):
		#each line of the file will be the key and value of a dict item
		file = open('test.txt', 'w')
		for k, v in animals.items():
			file.write(k+' '+v+'\n')
		file.close()
		
		#open the file and print the contents to the screen
		print 'printing the file to the screen'
		file = open('test.txt', 'rU')
		for line in file:
			print line,	


	file_practice(animals)
if __name__ == '__main__':
	main()