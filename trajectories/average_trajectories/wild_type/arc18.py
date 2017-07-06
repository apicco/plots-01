from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories

trajectory_list = load_directory(
		path = '../../raw_trajectories/wild_type/Arc18_WT' , 
		pattern = '.data.txt' ,
		comment_char = '%' , 
		dt = 0.1045 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Arc18-GFP' , 
		date = '02/03/12' , 
		notes = 'Arc18 average trajectory')

best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 500 , 
				output_file = 'arc18' , median = True , fimax = True ) 

