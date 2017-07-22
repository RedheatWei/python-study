key_string = 'Cost time'
f = file('D:\UCChatHall-900000-16572-201503100521.log')
for line in f.xreadlines():
    if key_string in line:
        line
    
