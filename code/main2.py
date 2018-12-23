import sys
import time

from epics import caget,caput

import measurement_obj as meas
import objective_function as obj
import parameters as pa
import conj_opt as opt

if __name__ == '__main__':

	file_names = pa.File_Names()
	parameter_list = pa.List_Names(file_names[0])
	arm_list = pa.List_Names(file_names[1])
	tbt_list_X = pa.List_Names(file_names[2])
	tbt_list_Y = pa.List_Names(file_names[3])
	get_value  = pa.Get_Value(tbt_list_X)

	k1=caget('PFRBT:K1:DELAY_SET')
	k3=caget('PFRBT:K3:DELAY_SET')
	k4=caget('PFRBT:K4:DELAY_SET')	

	K1 = []
	K3 = []
	K4 = []
	
	step = 0.02
	ite = 35
#	ite = 80
	
	for i in range(ite):
		K1.append(k1+step*i)
		K3.append(k3+step*i)
		K4.append(k4+step*i)
	
	print K1,K3,K4
	
	with open('../data/tmp.dat','w') as f:
		for i in range(ite):
			caput('PFRBT:K1:DELAY_SET',K1[i])
			caput('PFRBT:K3:DELAY_SET',K3[i])
			caput('PFRBT:K4:DELAY_SET',K4[i])
			sum = 0
			for j in range(5):
				sum += obj.List_Value(arm_list,tbt_list_X)
			f.write(str(i*step)+" "+str(sum)+"\n")
			print i
			f.flush()
		f.write("\n")

