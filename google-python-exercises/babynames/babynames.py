#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename, 'rU')
  
  #Searches the file to find the year the name ranking relates to 
  def get_year(filename):
    with open (filename, "r") as myfile:
      data=myfile.read()
      str = re.search('(Popularity in )(\d\d\d\d)',data)
      year = str.group(2) #get just the year
      myfile.close()
      return year
  
  #Searches the file for each name and its ranking   
  def get_data(filename): 
    year = get_year(filename)
    
    found = re.findall('<td>(\d+)</td><td>(.+)</td><td>(.+)</td>', f.read())
    ranks = [year]
    for i in found:
      ranks.append((i[1]+' '+ i[0]))
      ranks.append((i[2]+' '+ i[0]))

    f.close()
    return sorted(ranks)

  result = get_data(filename)
  return result

#Calls extract_name which returns a list begining with the year including each name and its ranking as a tuple
def main():
  runon = [] # list of files to scrape
  results = []
  files = [f for f in os.listdir('.') if os.path.isfile(f)]
  for f in files:
    if f != 'babynames.py':
      runon.append(f)

  for r in runon:
    results.append(extract_names(r))
  
    
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    for i in results:
      for x in i:
        print x  
    sys.exit(1)
  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
  if summary:
    writer = open('../'+args[0],'a')
    for i in results:
      for x in i:
        writer.write(x+' ')

  
if __name__ == '__main__':
  main()
