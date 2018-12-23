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

# Please check if libera works.
#	print obj.Record_Value(get_value[0]) # libera02
#	print obj.Record_Value(get_value[1]) # libera03
#	print obj.Record_Value(get_value[2]) # libera04
#	print obj.Record_Value(get_value[3]) # libera05
#	print obj.Record_Value(get_value[4]) # libera07
#	print obj.Record_Value(get_value[5]) # libera09

# Please check list name of arms is OK?
#	print arm_list
#	print obj.List_Value(arm_list,tbt_list_X)
#	print obj.List_Value(arm_list,tbt_list_Y)
	
# Measurement scan 
	meas.Get_Concave_angle(step=0.005,ite=6)
	meas.Get_Concave_delay(step=0.005,ite=6)

# Optimization ocject list
#	obj_record_list = ['PFRBT:K3:DELAY_SET','PFRBT:K4:DELAY_SET']
#	obj_record_list = ['PFRBT:K3:ANGLE_SET','PFRBT:K4:ANGLE_SET']
#	print opt.Gradient(obj_record_list[0],arm_list,tbt_list_X)
#	print opt.Gradient(obj_record_list[1],arm_list,tbt_list_X)
#	LearningRate = 0.0000001
#	opt.test(LearningRate,obj_record_list,arm_list,tbt_list_X)
#	LearningRate = 0.0000001
#	opt.test(LearningRate,obj_record_list,arm_list,tbt_list_X)
#	print test
#	print ite
#	opt.Conjugate(LearningRate,obj_record_list,arm_list,tbt_list_X)
#	print "END"	




