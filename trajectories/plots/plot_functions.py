from numpy import transpose, concatenate, convolve, sqrt, array
from trajalign.traj import Traj

import matplotlib
matplotlib.use('Agg')
from matplotlib.patches import Polygon

def dofilter( t , v ) :

	output = Traj()


	for a in t.attributes() :
		
		x = getattr( t , '_' + a )

		if '_err' in a :
			
			if a == 'coord_err' :

				output.input_values( a , [ 
					sqrt( convolve( x[ 0 ] ** 2 , array( v ) ** 2 , 'valid' ) ) , 
					sqrt( convolve( x[ 1 ] ** 2 , array( v ) ** 2 , 'valid' ) )
					] )

			else :
	
				output.input_values( a , sqrt( convolve( x ** 2 , array( v ) ** 2 , 'valid' ) ) )

		else :

			if a == 'coord' :

				output.input_values( a , [ convolve( x[ 0 ] , v , 'valid' ) , convolve( x[ 1 ] , v , 'valid' ) ] )

			else :

				output.input_values( a , convolve( x , v  , 'valid' ) )

	return output


def myplot( obj , tt , what , label , col , t0 = 0 , x0 = 0 , x_scale = 1 , v = [] , smooth_bin = 1 ) :
	
	def smooth_myplot( x , smooth_bin , maxval = True ) :

		output = []
		bins = range( 0 , len( x ) , smooth_bin )
		output.append( x[ 0 ] )
		for b in bins :
			sels = [ b + i for i in range( smooth_bin ) if ( b + i ) < len( x ) ]
			t =  [ x[ i ][ 0 ] for i in sels ]
			vals =  [ x[ i ][ 1 ] for i in sels ]
			if maxval : output.append( x[ b + vals.index( max( vals ) ) ] ) 
			else : output.append( x[ b + vals.index( min( vals ) ) ] ) 
		output.append( x[ len( x ) - 1 ] )
		return( output)
			
	if len( v ) :

		t = dofilter( tt , v )

	else :

		t = tt

	x = getattr( t , '_' + what )
	x_err = getattr( t , '_' + what + '_err' )

	if x.ndim > 1 : 

		#then the attribute has more than one dimention and we are interested
		#only in the first one.
		x = ( x[ 0 ] - x0 ) * x_scale
		x_err = x_err[ 0 ] * x_scale


	lower_error_boundary =  transpose( 
			[ t.t() - t0 , x - 1.96 * x_err ]
			)

	upper_error_boundary =  transpose( 
			[ t.t() - t0 , x + 1.96 * x_err ] 
			)

	lower_error_boundary = [ x for x in lower_error_boundary if x[ 1 ] == x[ 1 ] ]	
	upper_error_boundary = [ x for x in upper_error_boundary if x[ 1 ] == x[ 1 ] ]	

	if smooth_bin > 1 :
		lower_error_boundary = smooth_myplot( lower_error_boundary , smooth_bin , maxval = False )
		upper_error_boundary = smooth_myplot( upper_error_boundary , smooth_bin )
	
	error_boundary = concatenate( ( 
		lower_error_boundary , upper_error_boundary[ ::-1 ] 
		) )

	error_area = Polygon( error_boundary , True , color = col , alpha = 0.3 )

	#print( error_boundary )
	obj.add_patch( error_area )

	#plot the trajectory

	obj.plot( t.t() - t0 , x , linewidth = 1.5 , color = col , label = label )

#--------------GRAPHICS-DEFINITIONS---------------------
def ref_lines( obj , xlim , ylim ) :

	#colors of r lines
	mt_color ="#000000" #"#8e857e"#"#cbbeb5"
	zero_color = "#CDCDCD"
	t0_color = zero_color #"#8e857e"

	obj.plot( [ 0 , 0 ] , ylim , color = t0_color , linestyle = '-' ) #, label = '$t = 0$ s' )
	obj.plot( [ -2 , -2 ] , ylim , color = mt_color , linestyle = '--' , label = '$t = -2$ s' )
	obj.plot( xlim , [ 0 , 0 ] , color = zero_color , linestyle = '-' )


def area( obj , a , b , ylim , col , t0 = 0 ) :

	area_boundary = transpose( [ 
		[ a  , b , b , a ] - t0 , [ ylim[ 0 ] , ylim[ 0 ] , ylim[ 1 ] , ylim[ 1 ] ] 
			] )
	
	patch = Polygon( area_boundary , True , color = col , alpha = 0.3 )
	obj.add_patch( patch )
	
