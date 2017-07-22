#!/usr/bin/env python

'makeTextFile.py -- creat text file'

import os
import sys
ls = os.linesep
# get filename
fname = raw_input('Enter your file name:\n')
try:
    open(fname,'r')
except IOError, e:
    print '%s will be creat' % (fname)
else:
    print "Error: '%s' already exists" % fname
    sys.exit()

# get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)
        all[2]=entry

# write lines to file with porper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'DONE!'
