#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def _get_files():
  files = [f for f in os.listdir('.') if os.path.isfile(f)]
  filtered = []

  for f in files:
    if re.findall('.+__.+__.+' ,f):
      f = os.path.abspath(os.path.join('.',f))
      filtered.append(f)

  return filtered
  

def tdir(dirs, files):
  for d in dirs:
    to_dir = d  
    if not os.path.isdir(d):
      os.mkdir(d)
    for f in files: 
      shutil.copy(f, d)


def tzip(dir, files):
  zipdir = dir[0]
  for f in files:
    cmd = 'zip -j ' + zipdir + ' ' + f
    print 'Running command: ', cmd

    try:
      (status, output) = commands.getstatusoutput(cmd)
      if status:
        sys.stderr.write(output)
        sys.exit()
      print output
      #raise Exception('ERROR!')
    except  Exception as ex:
      print type(ex)
      print ex

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # Call the appropriate function
  files = _get_files()
  #Remove the 'dir' argument from the list of args
  if args[0] == 'dir':
    del args[0]

  if len(tozip) != 0:
    tzip(args, files)

  elif len(todir) != 0:
    tdir(args, files)

  

if __name__ == "__main__":
  main()
