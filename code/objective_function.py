import math

from epics import caget, caput

def Record_Value(get_value):
	"""Return the rms date with in the scan range
	
	Returns:
		rms: the rms date of TbT oscillation  
	"""
	sum = 0
	for i in range(200,1000,1):
		sum += (get_value[i]/1000)*(get_value[i]/1000)
	rms = math.sqrt(sum)
	return rms
	
def List_Value(ArmList,RecordList):
	"""Return the rms date of all RecordList
	Inputs:
		RecordList: Libera, TbT or ADC
		ArmList:    Libera, Timing Parameter
	Returns:
		sum: Sum the rms date of TbT oscillation  
	"""
	rms = []
# Please confirm the ArmList[num], Is it a real???
	for num in range(len(RecordList)):
		caput(ArmList[num],1)
#		print ArmList[num],caget(ArmList[num])
	for num in range(len(RecordList)):
		while(1):
			if caget(ArmList[num], timeout=5) == 0:
				break
	for num in range(len(RecordList)):
		val = []
		str = caget(RecordList[num], timeout=5)
		for i in range(200,1000,1):
			val.append((str[i]/1000)*(str[i]/1000))
		rms.append(math.sqrt(sum(val)))
#		print RecordList[num],rms[num]
	return sum(rms)
