import re
numstr = raw_input('re=')
restr = ''
for i in numstr:
    restr += '%s.*' % i
#print restr
m = re.search(restr,'s2097a205a0')
if m is not None:
    print m.group()
