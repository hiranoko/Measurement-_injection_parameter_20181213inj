import os
from epics import caget

def File_Names():
	"""Return the file name 
	Inputs:  Nothing
	Returns: File names including rerative pass
	"""
	files = []
	path = "../parameter_list"
	files = os.listdir(path)
	for i in range(len(files)):
		files[i] = path + "/" + files[i]
	return files

def List_Names(file_names):
	"""Return the list  name 
	Inputs:  file names
	Returns: Recoed name included in the file path
	"""
	list_names = []
	with open(file_names,'r') as f:
		list_names = f.read().split()		
	return  list_names
	
def Get_Value(list_names):
	"""Return the file name 
	Inputs:  list name
	Returns: list value
	"""
	value_list = []
	for i in range(len(list_names)):	
		value_list.append(caget(list_names[i]))
	return value_list

"""if __name__ == "__main__":
	file_names = File_Names()
	print file_names
	print type(file_names)
	r = List_Names(file_names[0])
	print r
	v =  Get_Value(r)
	print v
"""
