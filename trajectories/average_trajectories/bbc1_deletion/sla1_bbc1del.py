from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories

trajectory_list = load_directory(
		path = '../../raw_trajectories/bbc1_deletion/101222_Sla1_bbc1delta_MD' , 
		pattern = '.data' ,
		comment_char = '%' , 
		dt = 0.1045 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
		date = '22/12/10' , 
		notes = 'Sla1-GFP trajectory in the bbc1 deletion strain.'
		)

best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 500 , 
				output_file = 'sla1_bbc1del' , median = True , fimax = False )

