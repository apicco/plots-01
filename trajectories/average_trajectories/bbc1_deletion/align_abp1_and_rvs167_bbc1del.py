from trajalign.align import align
from trajalign.average import load_directory

rvs167_trajectories = load_directory(
		path = '../../raw_trajectories/bbc1_deletion/130806_2061_DW' , 
		pattern = '.W2data$' ,
		comment_char = '%' , 
		dt = 0.2715 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Rvs167-GFP' , 
		date = '06/08/13' , 
		notes = 'the trajectory of the target protein: Rvs167-GFP')

abp1_trajectories = load_directory(
		path = '../../raw_trajectories/bbc1_deletion/130806_2061_DW' , 
		pattern = '.W1data$' ,
		comment_char = '%' , 
		dt = 0.2715 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Abp1-mCherry' , 
		date = '06/08/13' , 
		notes = 'the trajectory of the reference protein: Abp1-mCherry')

align( path_target = 'rvs167_bbc1del.txt' , path_reference = 'abp1_bbc1del.txt' , ch1 = rvs167_trajectories , ch2 = abp1_trajectories , fimax2 = True )
