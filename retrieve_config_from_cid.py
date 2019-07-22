import os
import MySQLdb
import bz2
import sys

# given a cid in our database, this function returns the string of the config file used in this compilation.
def get_file(cid):
	try:
		socket=MySQLdb.connect("148.60.11.195", "script2", "ud6cw3xNRKnrOz6H", "IrmaDB_result")
		cursor=socket.cursor()
		query="SELECT config_file FROM compilations WHERE cid = {}".format(cid)        
		cursor.execute(query)
		file=cursor.fetchone()
		if (file is None):
			print ("Unable to retrieve cid=", str(cid))
		try:
			file = bz2.decompress(file[0]).decode()
		except Exception as e:
			print(str(e),"\n" + "Unable to decompress... ", file=sys.stderr)
			exit(-1)

	except Exception as e:
		print(str(e),"\n" + "Unable to connect to database cid = " + str(cid), file=sys.stderr)
		exit(-1)

	finally:
		cursor.close()
		socket.close()
	return file

exp1=[30000, 30400, 30800, 31200, 31600, 32000, 32400, 32800, 33200,
		33600, 34000, 34400, 34800, 35200, 35600, 36000, 36400, 36800,
		37200, 37600, 38000, 38400, 38800, 39200, 39600, 40000, 40400,
		40800, 41200, 41600, 42000, 42800, 43200, 43600, 44000, 44400,
		44800, 45200, 45600, 46000, 46400, 46800, 47200, 47600, 48000,
		48400, 48800, 49200, 49600, 50000, 50400, 50800, 51200, 51600,
		52000, 52400, 52800, 53200, 53600, 54000, 54400, 54800, 55200,
		55600, 56000, 56400, 56800, 57200, 57600, 58000, 58400, 58800,
		59200, 59600, 60000, 60400, 60800, 61200, 61600, 62000, 62400,
		62800, 63200, 63600, 64000, 64400, 64800, 65200, 65600, 66000,
		66400, 66800, 67600, 68000, 68400, 68800, 69200]
		
exp2=[36200, 36600, 37000, 37400, 37800, 38200, 38600, 39000, 39400,
		40200, 40600, 41000, 41400, 41800, 42600, 43000, 43400, 43800,
		44200, 44600, 45000, 45400, 45800, 46200, 46600, 47000, 47400,
		47800, 48200, 48600, 49000, 49400, 49800, 50200, 50600, 51000,
		51400, 51800, 52200, 52600, 53000, 53400, 53800, 54200, 54600,
		55000, 55400, 55800, 56200, 56600, 57000, 57400, 57800, 58200,
		58600, 59000, 59400, 59800, 60200, 60600, 61000]

# We retrieve the desired config files by using the above lists of cid. If you want any, just create a new list.
for c in c2:
	name= "Exp1/configs/" + str(c) + ".config"
	with open("{}".format(name), 'w+') as f:
		f.write(get_file(c))
