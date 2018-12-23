# python 2.5.2
# -*- coding: utf-8 -*-

import time
import sys
import math
import numpy as np
from epics import caget, caput

# Set Parameter
K1Angle = 'PFRBT:K1:ANGLE_SET'
K2Angle = 'PFRBT:K2:ANGLE_SET'
K3Angle = 'PFRBT:K3:ANGLE_SET'
K4Angle = 'PFRBT:K4:ANGLE_SET'
K1Delay = 'PFRBT:K1:DELAY_SET'
K2Delay = 'PFRBT:K2:DELAY_SET'
K3Delay = 'PFRBT:K3:DELAY_SET'
K4Delay = 'PFRBT:K4:DELAY_SET'
ParameterList = [K1Angle,K2Angle,K3Angle,K4Angle,K1Delay,K2Delay,K3Delay,K4Delay]

# Objective function
TdpBpm02 = 'pflibera02:TT:WFX'
TdpBpm03 = 'pflibera03:TT:WFX'
TbtObjList = [TdpBpm02,TdpBpm03]

ArmBpm02 = 'pflibera02:TT:ARM'
ArmBpm03 = 'pflibera03:TT:ARM'
ArmObjList = [ArmBpm02,ArmBpm03]

AdcBpm02 = 'pflibera02:TT:WFA'
AdcBpm03 = 'pflibera03:TT:WFA'
AdcObjList = [AdcBpm02,AdcBpm03]

# Libera
# return the rms data within the scan range
def RecordObjectiveValue(record):
	str = caget(record)
	sum = 0
	for i in range(0,2,1):
		sum += (str[i]/1000)*(str[i]/1000)
		print(abs(str[i]))
	rms = math.sqrt(sum)
	return rms
	
# Libera input:Record List, output:sum of rms data
# return the rms data within the scan range
def ListObjectiveValue(RecordList,ArmList):
	rms = []
	for num in range(len(RecordList)):
		caput(ArmList[num],1)
	for num in range(len(RecordList)):
		while(1):
			if caget(ArmList[num]) != 1:
				break
	for num in range(len(RecordList)):
		val = []
		str = caget(RecordList[num])
		for i in range(100,1000,1):
			val.append((str[i]/1000)*(str[i]/1000))
#			print(str[i])
		rms.append(math.sqrt(sum(val)))
#		print rms[num]
	return sum(rms)
	
# Free parameter
# Return current values
def GetSettingValue(RecordList):
	Parameter = []
	for i in range(len(RecordList)):
		Parameter.append(float(caget(RecordList[i])))
	return Parameter
	
# Free parameter
# Get the gradient using least squares method
def Gradient(record,ObjList,ArmList):
	X = []
	Y = []
	x = caget(record)
	X = [x*0.99,x,x*1.01]
	for i in range(0,3,1):
		sum = 0
		caput(record,x*(0.99+0.01*i))
		for n in range(10):
			sum += ListObjectiveValue(ObjList,ArmList)/1000
		Y.append(sum)
	caput(record,x)
	print X
	print Y
	A = np.array([X,np.ones(len(X))])
	A = A.T
	a,b = np.linalg.lstsq(A,Y)[0]
	return a
	
def GetConcave():
	X1 = []
	X2 = []
	x1 = caget(ParameterList[2])
	x2 = caget(ParameterList[3])
	for i in range(20):
		X1.append(x1*(0.90+i*0.01))
		X2.append(x2*(0.90+i*0.01))
	print X1,X2
#def comment():
	print ParameterList[2],ParameterList[3]
	f = open('tmp.dat','w')
	for i in range(20):
		caput(ParameterList[2],X1[i])
		for j in range(20):
			caput(ParameterList[3],X2[j])
			sum = 0
			for k in range(5):
				sum += ListObjectiveValue(TbtObjList,ArmObjList)/10
			print X1[i],X2[j],sum
			f.write(str(X1[i])+" "+str(X2[j])+" "+str(sum)+"\n")
		print "\n"
		f.write("\n")
	f.close()
	caput(ParameterList[2],x1)
	caput(ParameterList[3],x2)

if __name__ == "__main__":
	print(GetSettingValue(ParameterList))
	GetConcave()
	print(GetSettingValue(ParameterList))

	
