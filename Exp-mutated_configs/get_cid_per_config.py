# create a list to link the original cid with the cid after .config mutation
origin_config=0
new_cid=0
res=list()

#jobs=[]

# Below is hardcoded the number of the job where to look... Not suitable for parallelization yet.

#for job in jobs:
with open("/temp_dd/igrida-fs1/psaffray/oar_output/job.6981471.output", 'r') as fd:
	line=fd.readline()
	while line:
		if "/mnt/temp_dd/igrida-fs1/psaffray/input_files/configs/" in line:
			origin_config=line.split("/mnt/temp_dd/igrida-fs1/psaffray/input_files/configs/")[1].split(".config")[0]
		elif "Successfully send result with cid : " in line:
			new_cid=line.split("Successfully send result with cid : ")[1][:5]
			res.append([origin_config, new_cid])
		line=fd.readline()
print(len(res))
print(res)
#tmp=[]
#for i in res:
#	tmp.append(i[0])
#print(tmp)
	
