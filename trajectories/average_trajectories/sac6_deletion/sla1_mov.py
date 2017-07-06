from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories

trajectory_list = load_directory(
		path = '../../raw_trajectories/sac6_deletion/150303_MKY3060_mov' , 
		pattern = '.txt' ,
		comment_char = '%' , 
		dt = 0.351 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
		date = '03/03/15' , 
		notes = 'Sla1-GFP trajectory showing succesful invagination, in the sac6 deletion strain.'
		)

average_trajectories( trajectory_list , max_frame = 101 , 
		output_file = 'sla1_mov_sac6del' , median = True , fimax = False )

