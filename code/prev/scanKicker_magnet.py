import time
import sys
#from epics import caget
from epics import caget, caput

# Free Parmeters
K1Delay = 'PFRBT:K1:DELAY_SET'
K2Delay = 'PFRBT:K2:DELAY_SET'
K3Delay = 'PFRBT:K3:DELAY_SET'
K4Delay = 'PFRBT:K4:DELAY_SET'
DelayList = [K1Delay,K2Delay,K3Delay,K4Delay]

# Objective Parameter
TdpBpm03 = 'pflibera03:TT:WFX'
TdpBpm09 = 'pflibera09:TT:WFX'
TbtObjList = [TdpBpm03,TdpBpm09]
ArmBpm03 = 'pflibera03:TT:ARM'
ArmBpm09 = 'pflibera09:TT:ARM'
ArmObjList = [ArmBpm03,ArmBpm09]
AdcBpm03 = 'pflibera03:TT:WFA'
AdcBpm09 = 'pflibera09:TT:WFA'
AdcObjList = [AdcBpm03,AdcBpm09]

# Free parameter
# Return current values
def GetSettingValue(RecordList):
	Parameter = []
	for i in range(len(RecordList)):
		Parameter.append(float(caget(RecordList[i])))
	return Parameter
	
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
		for i in range(0,2,1):
			val.append((str[i]/1000)*(str[i]/1000))
			print(str[i])
		rms.append(math.sqrt(sum(val)))
		print rms[num]
	return sum(rms)
	
if __name__ == "__main__":
	DP = GetSettingValue(DelayList)
	print(DP)
#	for i in range(60):
	i = 0
	path = ("./date/out%02d.dat"%i)
	f = open(path,'w')
#		caput(DelayList[0],DP[0]+0.025*i)
#		caput(DelayList[1],DP[1]+0.025*i)
#		caput(DelayList[2],DP[2]+0.025*i)
#		caput(DelayList[3],DP[3]+0.025*i)
	for j in range(10):
		caput(ArmObjList[0],1)
		while(1):
			if caget(ArmObjList[0]) != 1:
				break
		s = caget(AdcObjList[0])
		for j in s:
			f.write(str(j)+" ")		
		f.write("\n")
#		print(i)
#	caput(DelayList[0],DP[0])
#	caput(DelayList[1],DP[1])
#	caput(DelayList[2],DP[2])
#	caput(DelayList[3],DP[3])
	f.close()
