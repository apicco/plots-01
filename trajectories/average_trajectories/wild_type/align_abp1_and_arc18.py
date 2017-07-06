from trajalign.align import align
from trajalign.average import load_directory

arc18_trajectories = load_directory(
		path = '../../raw_trajectories/wild_type/abp1_and_arc18' ,
		pattern = '.arc18_data.txt$' ,
		comment_char = '%' , 
		dt = 0.2715 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Arc18-GFP' , 
		date = '05/03/12' , 
		notes = 'the trajectory of the target protein')

abp1_trajectories = load_directory(
		path = '../../raw_trajectories/wild_type/abp1_and_arc18' ,
		pattern = '.abp1_data.txt$' ,
		comment_char = '%' , 
		dt = 0.2715 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Abp1-mCherry' , 
		date = '05/03/12' , 
		notes = 'the trajectory of the reference protein')

align( path_target = 'arc18.txt' , path_reference = 'abp1.txt' , ch1 = arc18_trajectories , ch2 = abp1_trajectories , fimax1 = True , fimax2 = True )
