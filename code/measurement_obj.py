import sys
import time

from epics import caget,caput

import objective_function as obj
import parameters as pa

def Get_Concave_angle(step,ite):
	"""Return the varing objective value
	Input the file name:  RecordList: Libera, TbT or ADC
	Return the list : [knob1, knob2, objective value]
	"""
	file_names = pa.File_Names()
	arm_list = pa.List_Names(file_names[1])
	tbt_list = pa.List_Names(file_names[2])
	X1 = []
	X2 = []
	x1 = caget('PFRBT:K3:ANGLE_SET')
	x2 = caget('PFRBT:K4:ANGLE_SET')
	print x1,x2
	for i in range(ite):
		X1.append(x1+step*i-ite/2*step)
		X2.append(x2+step*i-ite/2*step)
	print X1,X2
	
	with open('../data/measKK.dat','w') as f:
		for i in range(ite):
			caput('PFRBT:K3:ANGLE_SET',X1[i])
			for j in range(ite):
				caput('PFRBT:K4:ANGLE_SET',X2[j])
				sum = 0
				for k in range(5):
					sum += obj.List_Value(arm_list,tbt_list)
				print X1[i],X2[j],sum
				f.write(str(X1[i])+" "+str(X2[j])+" "+str(sum)+"\n")
				f.flush()
			f.write("\n")
			print "\n"
	caput('PFRBT:K3:ANGLE_SET',x1)
	caput('PFRBT:K4:ANGLE_SET',x2)

def Get_Concave_delay(step,ite):
	"""Return the varing objective value
	Input the file name:  RecordList: Libera, TbT or ADC
	Return the list : [knob1, knob2, objective value]
	"""
	file_names = pa.File_Names()
	arm_list = pa.List_Names(file_names[1])
	tbt_list = pa.List_Names(file_names[2])
	X1 = []
	X2 = []
	x1 = caget('PFRBT:K3:DELAY_SET')
	x2 = caget('PFRBT:K4:DELAY_SET')
	print x1,x2
	for i in range(ite):
		X1.append(x1+step*i-ite/2*step)
		X2.append(x2+step*i-ite/2*step)
	print X1,X2
	
	with open('../data/measDD.dat','w') as f:
		for i in range(ite):
			caput('PFRBT:K3:DELAY_SET',X1[i])
			for j in range(ite):
				caput('PFRBT:K4:DELAY_SET',X2[j])
				sum = 0
				for k in range(5):
					sum += obj.List_Value(arm_list,tbt_list)
				print X1[i],X2[j],sum
				f.write(str(X1[i])+" "+str(X2[j])+" "+str(sum)+"\n")
				f.flush()
			f.write("\n")
			print "\n"
	caput('PFRBT:K3:DELAY_SET',x1)
	caput('PFRBT:K4:DELAY_SET',x2)
