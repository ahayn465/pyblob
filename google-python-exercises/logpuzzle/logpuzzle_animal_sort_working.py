#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import requests
import shutil

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  f = open(filename, 'rU')
  urls = []

  fname = filename.split('_') 
  scrape = sorted(set(re.findall(r'(?:GET\s)(.+puzzle.+)(?:\sHTTP)', f.read())))
  f.close()

  for s in scrape:
    urls.append('https://' + fname[1] + s)

  return urls
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  

  to_dl = img_urls
  proxy = {"https" : "https://10.0.0.4:80"}
  
  directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), dest_dir)
  if not os.path.isdir(directory):
      os.mkdir(directory)

  for index, url in enumerate(to_dl):  
    print 'Retrieving image ' + url  
    filename = os.path.join(directory, "img"+str(index)+'.jpg')

    response = requests.get(url, proxies=proxy, stream=True)
    
    f = open(filename, 'a')
    for chunk in response.iter_content():
      f.write(chunk)
    f.close()
    
  create_page(dest_dir)


def tryint(s):
    try:
        return int(s)
    except:
        return s

def num_sorted(pics):
  return [ tryint(c) for c in re.split('([0-9]+)', pics) ]
 

def create_page(dest_dir):

  pics = sorted([f for f in os.listdir('./'+dest_dir)], key=num_sorted)
  for pic in pics:
    print pic

  full_path = []
  for pic in pics:
    p = os.path.abspath(os.path.join('./'+dest_dir,pic))
    full_path.append(p)

  print 'Generating HTML document...'
  source = '<html><body>'
  for path in full_path: 
    tag = '<img src="%s">' % path
    source += tag
  source += '</body></html>'   
  
  html = open('index.html', 'a')
  html.write(source)  




def main():

  #download_images(read_urls('animal_code.google.com'), 'pics')
  #create_page()
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
