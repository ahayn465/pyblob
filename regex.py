#!/usr/bin/python
import sys
import re
def main():

	def regex():
		print 'All the user names from the file:'
		#print the usernames from the emails in the text file
		file = open('email.txt', 'rU')
		for line in file:
			match = re.search(r'([\w.-]+)@([\w.-]+)', line)
			uname = match.group(1)
			print uname
		file.close()
			
		print 'All the full email addresses from the file pre-domain change'
		file = open('email.txt', 'rU')
		emails = re.findall(r'([\w.-]+@)([\w.-]+)',file.read())
		for i in emails:
			print i
		file.close()
		
		#changes the domain of the emails and writes to a new file
		print 'Change the domain of all the emails. See newemail.txt'
		file = open('email.txt', 'r+')
		emails = re.findall(r'([\w.-]+@)([\w.-]+)',file.read())
		new = open('newemail.txt', 'w+')
		for i in emails:
			new.write(i[0]+'me.com\n')
		

	regex()		

if __name__ == '__main__':
	main()