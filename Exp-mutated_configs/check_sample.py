import os
import subprocess

l=list()
new=0
count=0
cpt=0
cpt2=0
with open("diffs.txt", "r") as fd:
    line=fd.readline()
    while line:
        if "With " in line:
            count+=1
            new=1
            config=line.split("With ")[1].split(".config")[0]
        elif(new==1 and line=="\n"):
            l.append(config)
            print("find unchanged .config : {}".format(config))
            new=0
        line=fd.readline()

print("unchanged configs : {}/{}".format(len(l), count))
print(l)

# Select only the first 100 configs for the experiment
for i in range(100):
    subprocess.call(["cp", "produced_configs/{}.config".format(l[i]), "sample_configs/{}.config".format(l[i])])

