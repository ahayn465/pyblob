#!/usr/bin/python
import sys
import os
import commands
import urllib

def main():

	def print_dir():

		print '\nThe full path to this script is:'
		print os.path.abspath(os.path.join('.','utils.py'))

		print 'A directory listing of the contents of the current directory'
		dir = os.path.abspath('.')
		cmd = 'ls -l ' + dir
		print 'Running command: ', cmd

		try:
			(status, output) = commands.getstatusoutput(cmd)
			if status:
				sys.stderr.write(output)
				sys.exit()
			print output
			#raise Exception('ERROR!')
		except 	Exception as ex:
			print type(ex)
			print ex
		
	def html_output(url):
		page = urllib.urlopen(url)
		print page.read()


	print_dir()
	html_output('http://www.hitachi-id.com')

if __name__ == '__main__':
	main()