import time
import math

import numpy as np
from epics import caget, caput

import objective_function as obj

def Gradient(obj_record,arm_list,tbt_list):
	"""Return the gradient for the objective function
	Input the file name:  ObjRecord, RecordList: Libera, TbT or ADC
	Return the list : [knob1, knob2, objective value]
	"""
	X = []
	Y = []
	x = []
	x = caget(obj_record,timeout=5)
#	print x
	X = [x*0.995,x,x*1.005]
#	print X
	for i in range(0,3,1):
		sum = 0
		caput(obj_record,x*(0.995+0.005*i))
		for n in range(5):
			sum += obj.List_Value(arm_list,tbt_list)/1000
		Y.append(sum)
#		print i,0.99+0.01*i
	caput(obj_record,x)
#	print X
#	print Y
	A = np.array([X,np.ones(len(X))])
	A = A.T
	a,b = np.linalg.lstsq(A,Y)[0]
	print a
	return a


def Conjugate(LearningRate,obj_record_list,arm_list,tbt_list):
	"""Optimize 
	Input : objective record name list
	Output: non
	"""
	Rate = LearningRate
	grad = []
	knob = []
	tmp = []
	for i in range(len(obj_record_list)):
		grad.append(Gradient(obj_record_list[i],arm_list,tbt_list))
		knob.append(caget(obj_record_list[i]),timeout=5)
	tmp = knob
	print grad,knob,tmp
	
 	for i in range(5):
 		if i == 0:
 			prev = obj.List_Value(arm_list,tbt_list)
 			follw = prev
# 		if prev<follw:
# 			for j in range(len(obj_record_list)):
# 				caput(obj_record_list[j],tmp[j])		
# 			break
 		for j in range(len(obj_record_list)):
	 		tmp[j] = knob[j] - LearningRate*grad[j]
#		for j in range(len(obj_record_list)):
#			caput(obj_record_list[j],tmp[j])
		follw = obj.List_Value(arm_list,tbt_list)
		LearningRate += Rate
		print tmp,LearningRate,follw
#	return i


def test(LearningRate,obj_record_list,arm_list,tbt_list):
	"""Optimize 
	Input : objective record name list
	Output: non
	"""
	Rate = LearningRate
	x = []
	y = []
	grad = []
	knob = []
	tmp = []
	tmp2 = []
	for i in range(len(obj_record_list)):
		grad.append(Gradient(obj_record_list[i],arm_list,tbt_list))
		knob.append(caget(obj_record_list[i],timeout=5))
	tmp = knob
	tmp2 = knob
#	print grad,knob,tmp
	k = 0	
	sum = 0
	sum2 = 0 # prev
	sum3 = 0 # follow
 	for i in range(10):
# 		if i==0:
# 			for k in range(5):
# 				sum += obj.List_Value(arm_list,tbt_list)
# 			prev = sum
# 			follw = prev
 		if i>=1 and prev<follw:
	 		for j in range(len(obj_record_list)):		
#				tmp[j] = knob[j] - (LearningRate-Rate)*grad[j]
				caput(obj_record_list[j],tmp2[j])
			break
		
		sum2 = 0
		for k in range(8):
 			sum2 += obj.List_Value(arm_list,tbt_list) 
 		prev = sum2
 		
 		for j in range(len(obj_record_list)):
	 		tmp[j] = knob[j] - LearningRate*grad[j]
		for j in range(len(obj_record_list)):
			caput(obj_record_list[j],tmp[j])
		tmp2 = tmp
		sum3 = 0
		for k in range(8):
			sum3 += obj.List_Value(arm_list,tbt_list)
		follw = sum3
#		x.append(LearningRate)
#		y.append(follw/100000)
		print tmp,LearningRate,follw
		LearningRate += Rate

	print "optimized =",tmp,LearningRate,follw	
#	print x,y
# Fitting and searching minimum point
#	c = np.poly1d(np.polyfit(x,y,2)) 
#	crit = c.deriv().r
#	r_crit = crit[crit.imag==0].real
#	test = c.deriv(2)(r_crit)
#	x_min = r_crit[test>0]
# Update the knob parameters
#	print x_min
#	for j in range(len(obj_record_list)):
#		tmp[j] = knob[j] + x_min*grad[j]
#	for j in range(len(obj_record_list)):
#		caput(obj_record_list[j],tmp[j])



