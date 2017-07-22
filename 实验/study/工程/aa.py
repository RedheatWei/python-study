import subprocess
res = subprocess.Popen('tracert '+'119.167.244.134',shell=True,stdout=subprocess.PIPE)
res.wait()
res_list = res.stdout.read().split('\n')
for line in res_list:
    print line
    print type(line)
    for each_str in line.split():
        if '(' in each_str:
            print each_str
            area_ip = each_str.split('(')[-1].split(')')[0]
            print area_ip