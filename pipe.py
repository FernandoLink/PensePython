import os
cmd = 'dir d:\\workspace'
fp = os.popen(cmd)
res = fp.read()
print(res)
stat = fp.close()
print(stat)
