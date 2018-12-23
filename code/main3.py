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

	ite = 100
#	ite = 80
	
	
	with open('../data/err_bar100.dat','w') as f:
		for i in range(ite):
			sum = obj.List_Value(arm_list,tbt_list_X)
			f.write(str(i)+" "+str(sum)+"\n")
			print i
			f.flush()
		f.write("\n")
