import os
import subprocess

# This script needs to be executed in the kernel sources folder.

files=[]
path="myconfigs/"

if not os.path.exists(path):
    os.makedirs(path)
for f in os.walk(path):
    for i in f[2]:
        files.append(i)
with open("diffs.txt", 'a+') as res:
    for config in files:
        res.write("\nWith {} :\n".format(config))
        res.flush()
        subprocess.call(["cp", "myconfigs/{}".format(config), ".config"])
        subprocess.call(["scripts/config", "-e", "CONFIG_CC_OPTIMIZE_FOR_SIZE", "-d", "CONFIG_CC_OPTIMIZE_FOR_PERFORMANCE"])
        subprocess.call(["make", "olddefconfig"])
        #subprocess.call(["scripts/config", "-s", "CONFIG_KMEMCHECK"], stdout=res)
        #subprocess.call(["scripts/config", "-s", "CONFIG_CC_OPTIMIZE_FOR_SIZE"], stdout=res)
        #subprocess.call(["scripts/config", "-s", "CONFIG_CC_OPTIMIZE_FOR_PERFORMANCE"], stdout=res)
        subprocess.call(["scripts/diffconfig", ".config.old",  ".config"], stdout=res)
        subprocess.call(["cp", ".config", "produced_configs/{}".format(config)])
        subprocess.call(["rm", ".config", ".config.old"])

