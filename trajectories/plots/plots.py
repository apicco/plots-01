from plot_functions import myplot , area , ref_lines
from matplotlib import pyplot as plt
import matplotlib as mpl
plt.style.use( 'paper' )
from trajalign.traj import Traj
import numpy as np

#--------------TRAJECTORY DEFINITIONS---------------------
#load the aligned trajectories in the wild type
abp1 = Traj()
abp1.load( '../average_trajectories/wild_type/abp1.txt' )
arc18 = Traj()
arc18.load( '../average_trajectories/wild_type/arc18_aligned.txt' )
sla1 = Traj()
sla1.load( '../average_trajectories/wild_type/sla1_aligned.txt' )
rvs167 = Traj()
rvs167.load( '../average_trajectories/wild_type/rvs167_aligned.txt' )

#load the aligned trajectories in bbc1 deletion
abp1_bd = Traj()
abp1_bd.load( '../average_trajectories/bbc1_deletion/abp1_bbc1del.txt' )
arc18_bd = Traj()
arc18_bd.load( '../average_trajectories/bbc1_deletion/arc18_bbc1del_aligned.txt' )
sla1_bd = Traj()
sla1_bd.load( '../average_trajectories/bbc1_deletion/sla1_bbc1del_aligned.txt' )
rvs167_bd = Traj()
rvs167_bd.load( '../average_trajectories/bbc1_deletion/rvs167_bbc1del_aligned.txt' )

#normalise the fluorescence intensities
abp1.n_mol( 240.3 , 20.6 )
arc18.n_mol( 115.5 , 29.7 )
sla1.n_mol( 47.5 , 4.5 )
rvs167.n_mol( 51.3 , 6.3 )
abp1_bd.n_mol( 397.6 , 44 )
arc18_bd.n_mol( 151.6 , 38.8 )
sla1_bd.n_mol( 60.3 , 6.8 )
rvs167_bd.n_mol( 92.5 , 13.3 )

#load the aligned trajectories in sac6 deletion
sla1_sdr = Traj()
sla1_sdr.load( '../average_trajectories/sac6_deletion/sla1_ret_sac6del.txt' )
#the trajectories start with nan, which causes problems to myplot. remove the first nan values
not_nan = [ i for i in range( len( sla1_sdr ) ) if sla1_sdr.coord()[ 0 ][ i ] == sla1_sdr.coord()[ 0 ][ i ] ] 
sla1_sdr.start(  sla1_sdr.t( not_nan[ 0 ] ) )

sla1_sdm = Traj()
sla1_sdm.load( '../average_trajectories/sac6_deletion/sla1_mov_sac6del.txt' )

#--------------TRAJECTORY TIME AND SPATIAL ALIGNMENT WILD TYPE---------------------
sgf = [ -3/35 , 12/35 , 17/35 , 12/35 , -3/35 ] #Savitzky-Golay filter

sp = np.nanargmax( np.convolve( sla1.f() , sgf ) )
rp = np.nanargmax( np.convolve( rvs167.f() , sgf ) )
t0 = rvs167.t( rp ) 
x0 = np.nanmean( sla1.extract( range( 0 , sp ) ).coord()[ 0 ] )

#--------------COLORS---------------------
yellow = "#F9F47F"
red = "#FAB199"

###################################
#     		FIGURE 2
###################################

#--------------TRAJECTORY TIME AND SPATIAL ALIGNMENT WILD TYPE---------------------
x0_sdr = -0.08
x0_sdm = -0.1
t0_sdr = 23.5
t0_sdm = 26.8

#axis lims
movlim = ( -80 , 280 )
tlim = ( -28 , 16 )

f , ( sdr , sdm ) = plt.subplots( 1 , 2 , gridspec_kw = { 'height_ratios' : [ 1 , 1 ] } , figsize = ( 9 , 9 ) , sharey = True )

myplot( sdm , sla1 , what = 'coord' , col = '#000000' , label = 'Sla1' , x_scale = 100 , t0 = t0 , x0 = x0 )
myplot( sdm , sla1_sdm , what = 'coord' , col = '#D7110E' , x_scale = 64.5 , t0 = t0_sdm , x0 = x0_sdm , label = 'Sla1 $sac6\Delta$\n(n=' + str( int( max( sla1_sdm.n() ) ) ) + ')' , smooth_bin = 2 )
#sdm.errorbar( sla1_sdm.t() - t0_sdm , 64.5 * ( sla1_sdm.coord()[ 0 ] - x0_sdm ) , yerr = 1.96 * 64.5 * sla1_sdm.coord_err()[ 0 ] , color = '#D7110E' , fmt = '.' , label = 'Sla1 $sac6\Delta$\n(n=' + str( int( max( sla1_sdm.n() ) ) ) + ')' )

ref_lines( sdm , tlim , movlim )

myplot( sdr , sla1 , what = 'coord' , col = '#000000' , label = 'Sla1' , x_scale = 100 , t0 = t0 , x0 = x0 )
myplot( sdr , sla1_sdr , what = 'coord' , col = '#D7110E' , x_scale = 64.5 , t0 = t0_sdr , x0 = x0_sdr , label = 'Sla1 $sac6\Delta$\n(n=' + str( int( max( sla1_sdr.n() ) ) ) + ')' , smooth_bin = 2 )
#sdr.errorbar( sla1_sdr.t() - t0_sdr , 64.5 * ( sla1_sdr.coord()[ 0 ] - x0_sdr ) , yerr = 1.96 * 64.5 * sla1_sdr.coord_err()[ 0 ] , color = '#D7110E' , fmt = '.' , label )

ref_lines( sdr , tlim , movlim )
#myplot( sdr , sla1_sdr , what = 'coord' , col = '#D7110E' , label = 'Sla1 $sac6\Delta$' , x_scale = 64.5 , t0 = t0_sdr , x0 = x0_sdr )

#NOTE: PROBABLY WANT TO REMOVE THE OPTION TO SHOTEN THE TRAJECTORY TO THE MEAN START AND END FOR SLA1 MOV, TOO FEW TRAJECTORIES!!!

plt.subplot( sdr )
plt.ylabel( 'Inward movement (nm)' , fontsize = 24 )
plt.xlabel( 'Time (' + abp1_bd.annotations( 't_unit' ) + ')' , fontsize = 24 )
plt.xlim( tlim )
plt.ylim( movlim )
plt.legend( loc = 'upper left' , numpoints = 1 )

plt.subplot( sdm )
plt.xlabel( 'Time (' + abp1_bd.annotations( 't_unit' ) + ')' , fontsize = 24 )
plt.xlim( tlim )
plt.legend( loc = 'upper left'  , numpoints = 1 )


#f.tight_layout()
f.savefig( 'sla1_in_sac6deletion.pdf' )


###################################
#     		FIGURE 3
###################################

#--------------TRAJECTORY TIME AND SPATIAL ALIGNMENT bbc1delta---------------------

sp_bd = np.nanargmax( np.convolve( sla1_bd.f() , sgf ) )
rp_bd = np.nanargmax( np.convolve( rvs167_bd.f() , sgf ) )

#distribute possible error in the alignment of the average trajectories but centering both 
#plots on the center of mass defined by the trajectory points before the peak of fluorescence
#intensity of both Sla1 and Rvs167. Abp1 is not used, firstly because the behaviour of Abp1 is 
#different in the WT and bd, secondly because the relative position of Abp1 in the 
#WT and bd is interesting per se.

shift_x0 = 0#- 0.05
shift_t0 = 0

x0_bd = np.nanmean( sla1_bd.extract( range( 0 , sp_bd ) ).coord()[ 0 ] ) - shift_x0
t0_bd = rvs167_bd.t( rp_bd ) - shift_t0

#axis lims
movlim = ( -50 , 450 )
filim = ( -50 , 1000 )
tlim = ( -27 , 10 )

f , ( s , r , a , fi ) = plt.subplots( 4 , 1 , gridspec_kw = { 'height_ratios' : [ 1 , 1 , 1 , 1 ] } , figsize = ( 5 , 20) , sharex = True )


area( s , abp1_bd.start() , sla1_bd.end() , movlim , yellow , t0 = t0_bd )
area( s , sla1_bd.end() , abp1_bd.end() , movlim , red , t0 = t0_bd )
myplot( s , sla1 , what = 'coord' , col = '#000000' , label = 'Sla1' , x_scale = 100 , t0 = t0 , x0 = x0 )
myplot( s , sla1_bd , what = 'coord' , col = '#D7110E' , label = 'Sla1 $bbc1\Delta$' , x_scale = 100 , t0 = t0_bd , x0 = x0_bd )
ref_lines( s , tlim , movlim )

area( r , abp1_bd.start() , abp1_bd.end() , movlim , yellow , t0 = t0_bd )
area( r , rvs167_bd.start() , rvs167_bd.end() , movlim , red , t0 = t0_bd )
myplot( r , rvs167 , what = 'coord' , col = '#000000' , label = 'Rvs167' , x_scale = 100 , t0 = t0 , x0 = x0 )
myplot( r , rvs167_bd , what = 'coord' , col = '#D7110E' , label = 'Rvs167 $bbc1\Delta$' , x_scale = 100 , t0 = t0_bd , x0 = x0_bd )
ref_lines( r , tlim , movlim )

myplot( a , abp1 , what = 'coord' , col = '#000000' , label = 'Abp1' , x_scale = 100 , t0 = t0 , x0 = x0 )
myplot( a , abp1_bd , what = 'coord' , col = '#D7110E' , label = 'Abp1 $bbc1\Delta$' , x_scale = 100 , t0 = t0_bd , x0 = x0_bd )
ref_lines( a , tlim , movlim )

myplot( fi , abp1 , what = 'mol' , col = '#000000' , label = 'Abp1' , x_scale = 100 , t0 = t0 , x0 = x0 )
myplot( fi , abp1_bd , what = 'mol' , col = '#D7110E' , label = 'Abp1 $bbc1\Delta$' , t0 = t0_bd , x0 = x0_bd )
ref_lines( fi , tlim , filim )

plt.subplot( a )
plt.ylabel( 'Inward movement (nm)' , fontsize = 24 )
plt.ylim( movlim )
plt.legend( loc = 'upper left' )

plt.subplot( r )
plt.ylabel( 'Inward movement (nm)' , fontsize = 24 )
plt.ylim( movlim )
plt.legend( loc = 'upper left' )

plt.subplot( s )
plt.ylabel( 'Inward movement (nm)' , fontsize = 24 )
plt.ylim( movlim )
plt.legend( loc = 'upper left' )

plt.subplot( fi )
plt.ylabel( 'Number of molecules' , fontsize = 24 )
plt.ylim( filim )
plt.legend( loc = 'upper left' )

plt.xlabel( 'Time (' + abp1_bd.annotations( 't_unit' ) + ')' , fontsize = 24 )
plt.xlim( tlim )

#f.tight_layout()
f.savefig( 'panel_trajectories.pdf' )

#plot
f, ( trj , fi ) = plt.subplots( 2 , 1 , gridspec_kw = { 'height_ratios' : [ 2 , 1 ] } , figsize = ( 8 , 11 ) , sharex = True )

myplot( trj , abp1_bd , what = 'coord' , col = '#D7110E' , label = 'Abp1' , t0 = t0_bd , x0 = x0_bd , x_scale = 100 )
myplot( trj , sla1_bd , what = 'coord' , col = '#336CFF' , label = 'Sla1' , t0 = t0_bd , x0 = x0_bd , x_scale = 100 )
myplot( trj , rvs167_bd , what = 'coord' , col = '#006400' , label = 'Rvs167' , t0 = t0_bd , x0 = x0_bd , x_scale = 100 )
#
myplot( trj , abp1 , what = 'coord' , col = '#D7110E' , label = 'Abp1' , t0 = t0 , x0 = x0 , x_scale = 100 )
myplot( trj , sla1 , what = 'coord' , col = '#336CFF' , label = 'Sla1' , t0 = t0 , x0 = x0 , x_scale = 100 )
myplot( trj , rvs167 , what = 'coord' , col = '#006400' , label = 'Rvs167' , t0 = t0 , x0 = x0 , x_scale = 100 )

trj.plot( [ -2 , -2 ] , [ - 100 , 500 ] , '--' )

myplot( fi , abp1 , what = 'mol' , col = '#D7110E' , label = 'Abp1' , t0 = t0 )
myplot( fi , sla1 , what = 'mol' , col = '#336CFF' , label = 'Sla1' , t0 = t0 )
myplot( fi , rvs167 , what = 'mol' , col = '#006400' , label = 'Rvs167' , t0 = t0 )
myplot( fi , abp1_bd , what = 'mol' , col = '#D7110E' , label = 'Abp1' , t0 = t0_bd )
myplot( fi , sla1_bd , what = 'mol' , col = '#336CFF' , label = 'Sla1' , t0 = t0_bd )
myplot( fi , rvs167_bd , what = 'mol' , col = '#006400' , label = 'Rvs167' , t0 = t0_bd )

plt.subplot( trj )
plt.ylabel( 'Inward movement (nm)' , fontsize = 24 )
plt.legend( loc = 'best' )

plt.subplot( fi )
plt.ylabel( 'FI (a.u.)' , fontsize = 24 )
plt.xlabel( 'Time (' + abp1_bd.annotations( 't_unit' ) + ')' , fontsize = 24 )
plt.legend( loc = 'best' )

f.tight_layout()
f.savefig( 'plot_bbc1del_trajectories.png' )

#--------------TRAJECTORY TIME AND SPATIAL ALIGNMENT bbc1delta---------------------

las17 = Traj()
las17.load('las17.txt' , t = 0 , coord = ( 2 , 3 ) , mol = 8 , coord_err = ( 4 , 5 ) , mol_err = 9 , n = 10 )
las17.input_values( 'mol_err' , las17.mol_err() / 1.96 )

las17_bd = Traj()
las17_bd.load('las17_bbc1del.txt' , t = 0 , coord = ( 2 , 3 ) , mol = 8 , coord_err = ( 4 , 5 ) , mol_err = 9 , n = 10 )
las17_bd.input_values( 'mol_err' , las17_bd.mol_err() / 1.96 )

f , ( m ) = plt.subplots( 1 , 1 , figsize = ( 5 , 5 ) , sharex = True )
myplot( m , las17 , what = 'mol' , col = '#000000' , label = 'Las17' , t0 = 0 )
myplot( m , las17_bd , what = 'mol' , col = '#D7110E' , label = 'Las17' , t0 = 0 )
ref_lines( m , ( -27 , 3 ) , ( -20 , 120 ) )

plt.subplot( m )
plt.ylabel( 'Number of molecules' , fontsize = 24 )
plt.xlim( ( -27 , 3 ) )
plt.ylim( ( -20 , 120 ) )
plt.legend( loc = 'upper left' )

plt.xlabel( 'Time (' + abp1_bd.annotations( 't_unit' ) + ')' , fontsize = 24 )
plt.savefig( 'las17.pdf' )

###################################
#     		FIGURE 3 - figure supplement 1
###################################


#--------------Rvs167 lifetime and arc18 in bbc1delta---------------------

f , ( r_fi , arc , arc_fi ) = plt.subplots( 3 , 1 , gridspec_kw = { 'height_ratios' : [ 1 , 1 , 1 ] } , figsize = ( 5 , 15) , sharex = True )

area( r_fi , abp1_bd.start() , abp1_bd.end() , movlim , yellow , t0 = t0_bd )
area( r_fi , rvs167_bd.start() , rvs167_bd.end() , movlim , red , t0 = t0_bd )
myplot( r_fi , rvs167 , what = 'mol' , col = '#000000' , label = 'Rvs167' , x_scale = 100 , t0 = t0 , x0 = x0 )
myplot( r_fi , rvs167_bd , what = 'mol' , col = '#D7110E' , label = 'Rvs167 $bbc1\Delta$' , x_scale = 100 , t0 = t0_bd , x0 = x0_bd )
ref_lines( r_fi , tlim , ( -10 , 350 ) )

myplot( arc , arc18 , what = 'coord' , col = '#000000' , label = 'Arc18' , x_scale = 100 , t0 = t0 , x0 = x0 )
myplot( arc , arc18_bd , what = 'coord' , col = '#D7110E' , label = 'Arc18 $bbc1\Delta$' , x_scale = 100 , t0 = t0_bd , x0 = x0_bd )
ref_lines( arc , tlim , ( -50 , 600 ) )

myplot( arc_fi , arc18 , what = 'mol' , col = '#000000' , label = 'Arc18' , x_scale = 100 , t0 = t0 , x0 = x0 )
myplot( arc_fi , arc18_bd , what = 'mol' , col = '#D7110E' , label = 'Arc18 $bbc1\Delta$' , t0 = t0_bd , x0 = x0_bd )
ref_lines( arc_fi , tlim , ( -25 , 450 ) )

plt.subplot( r_fi )
plt.ylabel( 'Number of molecules' , fontsize = 24 )
plt.ylim( ( -10 , 350 ) )
plt.legend( loc = 'upper left' )

plt.subplot( arc )
plt.ylabel( 'Inward movement (nm)' , fontsize = 24 )
plt.ylim( ( -50 , 600 ) )
plt.legend( loc = 'upper left' )

plt.subplot( arc_fi )
plt.ylabel( 'Number of molecules' , fontsize = 24 )
plt.ylim( ( -25 , 450 ) )
plt.legend( loc = 'upper left' )

plt.xlabel( 'Time (' + abp1_bd.annotations( 't_unit' ) + ')' , fontsize = 24 )
plt.xlim( tlim )

#f.tight_layout()
f.savefig( 'panel_trajectories_supp.pdf' )
