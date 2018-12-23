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
TdpBpm03 = 'pflibera03:TT:WFX'
TdpBpm09 = 'pflibera09:TT:WFX'
TbtObjList = [TdpBpm03,TdpBpm09]

ArmBpm03 = 'pflibera03:TT:ARM'
ArmBpm09 = 'pflibera09:TT:ARM'
ArmObjList = [ArmBpm03,ArmBpm09]

AdcBpm03 = 'pflibera03:TT:WFA'
AdcBpm09 = 'pflibera09:TT:WFA'
AdcObjList = [AdcBpm03,AdcBpm09]

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
# put ArmList
	for num in range(len(RecordList)):
		caput(ArmList[num],1)
	for num in range(len(RecordList)):
		while(1):
			if caget(ArmList[num]) != 1:
				break
# get Value
	for num in range(len(RecordList)):
		val = []
		str = caget(RecordList[num])
		for i in range(0,2,1):
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

if __name__ == "__main__":
	SettingParameter = GetSettingValue(ParameterList)
	print(SettingParameter)
	print(ListObjectiveValue(ObjListH))
	LearningRate = 0.000
	Step         = 0.001
# 勾配ベクトルの生成(ite=0)		
	x = caget(ParameterList[2])
	y = caget(ParameterList[3])
	gr1 = Gradient(ParameterList[2],TbtObjList,ArmObjList)
	gr2 = Gradient(ParameterList[3],TbtObjList,ArmObjList)
        for i in range(10):
		x2 = x - LearningRate*gr1
		y2 = y - LearningRate*gr2
		print(x2,y2,LearningRate)
		if i == 0:
			val_pre =  ListObjectiveValue(TbtObjList,ArmObjList)
			val = val_pre
		if val_pre < val or i ==9 :
			x2 = x - LearningRate*gr1
			y2 = y - LearningRate*gr2
#			x  = caput(ParameterList[2],x2)
#			y  = caput(ParameterList[3],y2)
			print(x,y)
			break
		caput(ParameterList[2],x2)
		caput(ParameterList[3],y2)
		val = ListObjectiveValue(TestList)
		LearningRate += Step
	gr3 = Gradient(ParameterList[2])
	gr4 = Gradient(ParameterList[3])
# 共役ベクトルの生成(ite>0)
# test用に2回だけのループ
	Step = 0.001
	for i in range(10):
		LearningRate = 0.000
		for j in range(1,10,1):
			x2 = x - LearningRate*(gf3-(gf3*gf3)/(gf1*gf1+gf2*gf2)
			y2 = y - LearningRate*(gf4-(gf4*gf4)/(gf1*gf1+gf2*gf2)
			if i == 0:
				val_pre =  ListObjectiveValue(TbtObjList,ArmObjList)
				val = val_pre
			if val_pre < val or i ==9 :
				x2 = x - LearningRate*gr1
				y2 = y - LearningRate*gr2
				gf1 = gf3
				gf2 = gf4
				gf3 = Gradient(ParameterList[2],TbtObjList,ArmObjList)
				gf4 = Gradient(ParameterList[3],TbtObjList,ArmObjList)
#				x  = caput(ParameterList[2],x2)
#				y  = caput(ParameterList[3],y2)
				if i == 1:
					step /= 10
				if i == 9:
					step *= 10
				print(x,y)
				break
			caput(ParameterList[2],x2)
			caput(ParameterList[3],y2)
			val = ListObjectiveValue(TestList)
			LearningRate += Step
# 終了条件はGrade探索で傾き検知をできないとき
#		if(gf1<0.1 and gf2):
#			break

# ite回数の調整でどう変化した?
	SettingParameter = GetSettingValue(ParameterList)
	print(SettingParameter)
	print(ListObjectiveValue(ObjListH))

