from trajalign.align import average_ch1
from trajalign.average import load_directory

las17_trajectories = load_directory(
		path = '../../raw_trajectories/bbc1_deletion/140305_2103_DW' , 
		pattern = '.W2data$' ,
		comment_char = '%' , 
		dt = 0.2715 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
		date = '24/07/13' , 
		notes = 'the trajectory of the target protein: Las17-GFP')

abp1_trajectories = load_directory(
		path = '../../raw_trajectories/bbc1_deletion/140305_2103_DW' , 
		pattern = '.W1data$' ,
		comment_char = '%' , 
		dt = 0.2715 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Abp1-mCherry' , 
		date = '24/07/13' , 
		notes = 'the trajectory of the reference protein: Abp1-mCherry')

average_ch1( path_reference = 'abp1_bbc1del.txt' , ch1 = las17_trajectories , ch2 = abp1_trajectories , output_file = 'las17_bbc1del' , max_frame = 300 , fimax = True )
