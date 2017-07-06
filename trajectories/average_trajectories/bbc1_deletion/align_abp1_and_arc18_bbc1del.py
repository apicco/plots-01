from trajalign.align import align
from trajalign.average import load_directory

arc18_trajectories = load_directory(
		path = '../../raw_trajectories/bbc1_deletion/140116_3015_DW' , 
		pattern = '.W2data$' ,
		comment_char = '%' , 
		dt = 0.2755 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Arc18-GFP' , 
		date = '14/01/16' , 
		notes = 'the trajectory of the target protein: Arc18-GFP')

abp1_trajectories = load_directory(
		path = '../../raw_trajectories/bbc1_deletion/140116_3015_DW' , 
		pattern = '.W1data$' ,
		comment_char = '%' , 
		dt = 0.2755 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Abp1-mCherry' , 
		date = '14/01/16' , 
		notes = 'the trajectory of the reference protein: Abp1-mCherry')

align( path_target = 'arc18_bbc1del.txt' , path_reference = 'abp1_bbc1del.txt' , ch1 = arc18_trajectories , ch2 = abp1_trajectories , fimax1 = True , fimax2 = True )
