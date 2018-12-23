# python 2.5.2
# -*- coding: utf-8 -*-

import math
import numpy as np
import sys
import time

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

def RecordObjectiveValue(record):
	"""Return the rms date with in the scan range
	
	Returns:
		rms: the rms date of TbT oscillation  
	"""
	str = caget(record)
	sum = 0
	for i in range(0,2,1):
		sum += (str[i]/1000)*(str[i]/1000)
		print(abs(str[i]))
	rms = math.sqrt(sum)
	return rms
	
def ListObjectiveValue(RecordList,ArmList):
	"""Return the rms date of all RecordList
	Inputs:
		RecordList: Libera, TbT or ADC
		ArmList:    Libera, Timing Parameter
	Returns:
		sum: Sum the rms date of TbT oscillation  
	"""
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
		for i in range(0,2,1):
			val.append((str[i]/1000)*(str[i]/1000))
			print(str[i])
		rms.append(math.sqrt(sum(val)))
		print rms[num]
	return sum(rms)
	
def GetSettingValue(RecordList):
	"""Return the value of record list including Kicker Delay timing [usec] and Angle [mrad]
	Inputs:
		RecordList: Libera, TbT or ADC
	Returns:
		Parameter: Record list value
	"""
	Parameter = []
	for i in range(len(RecordList)):
		Parameter.append(float(caget(RecordList[i])))
	return Parameter
	
def Gradient(record,ObjList,ArmList):
	"""Return the value of record list including Kicker Delay timing [usec] and Angle [mrad]
	Inputs:
		record:  Delay time or Angle
		ObjList: Objective value of Tbt or ADC
		ArmList: Timing 
	Returns:
		a : Graditen of y=ax+b
	"""
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


if __name__ == "__main__":
