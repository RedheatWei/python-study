#!/usr/bin/env python
print '1.Creat a new file'
print '2.Read an old file'
import os
import sys
ls = os.linesep
cho = int(raw_input('Which one did you choice:\n'))
#fname = raw_input('Enter your file name:\n')
def write():
    # get filename
    fname = raw_input('Enter filename: ')
    try:
        open(fname,'r')
    except IOError, e:
        print #'%s will be creat' % (fname)
    else:
        print "Error: '%s' already exists" % fname
        return
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

    # write lines to file with porper line-ending
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x,ls) for x in all])
    fobj.close()
    print 'DONE!'
def read():
    # get filename
    fname = raw_input('Enter filename: ')
    print

    # attempt to open file for reading
    try:
        fobj = open(fname,'r')
    except IOError, e:
        print "***file open error:", e
    else:
        # display contents to the screen
        for eachLine in fobj:
            print eachLine,
        fobj.close()
if cho == int(1):
    write()
elif cho == int(2):
    read()
else:
    print('Have a wrong choice!')
    sys.exit()