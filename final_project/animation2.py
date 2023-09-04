### Animation 2 MRIcroGL ###
#Upload the script from MRIcroGL, "Scripting" menu, "open"

import gl
import sys

#=== Function Animation ===#

def animation(steps,direction_step,starting_pos,axis2rotate,take_screen,cumulative_steps):
    """ How to animate your Render
    steps = by how many degrees to rotate the render (from 0 to N, only integer)
    direction_step = 1 clockwise on X axis, torward superior portion for Y axis
    -1 is the opposite direction, counterclockwise on X axis, torward inferior portion for Y axis
    starting_pos = x,y coordinates from where to start, [0,0] is occipital view
    axis2rotate = "x" rotate on X axis | "y" rotate on Y axis
    take_screen = 1 make screenshot in bitmap [there aren't other options :( ] | 0 no screenshot
    cumulative_steps = crucial for saving the screenshot without deleting the old ones generated from other animation
    """
    
    for stp in range(0, steps):
        if direction_step == 1:   
            if axis2rotate == "x":            
                gl.azimuthelevation(starting_pos[0]+(stp),starting_pos[1])
                gl.wait(0)
            elif axis2rotate == "y":          
                gl.azimuthelevation(starting_pos[0],starting_pos[1]+stp)            
                gl.wait(0)
        elif direction_step == -1:  
            if axis2rotate == "x":            
                gl.azimuthelevation(starting_pos[0]-(stp),starting_pos[1])
                gl.wait(0)
            elif axis2rotate == "y":        
                gl.azimuthelevation(starting_pos[0],starting_pos[1]-stp)            
                gl.wait(0)
            
        save_name = cumulative_steps  + stp
        print(save_name)
        
        if take_screen == 1:
            gl.savebmp( path +str(save_name)+ '.png')
            gl.bmpzoom(zoom_factor )
            
    cumulative_steps +=  stp
    
    return cumulative_steps

#=== Function Pause ===#
def pause(time,take_screen,cumulative_steps):
    """ How to animate your Render
    time = how many milliseconds to wait
    take_screen = 1 make screenshot in bitmap [there aren't other options :( ] | 0 no screenshot
    cumulative_steps = crucial for saving the screenshot without deleting the old ones generated from other animation
    """
    
    cumulative_steps_new = 0
    for p in range(0, time):
        gl.wait(1)       
        save_name = cumulative_steps + p
        print(save_name)
        
        if take_screen == 1:
            gl.savebmp( path +str(save_name)+ '.png')
            gl.bmpzoom(zoom_factor )
            
    cumulative_steps +=  p 
    
    return cumulative_steps

#=== Function Clipping ===#

def clipping(starting_slice,end_slice,step_slices,take_screen,cumulative_steps,azimuth_slice,elevation_slice=0):

    """ Animation with clipping (cutting stuff)
    starting_slice =floats from 0 to 1.0, where to start with the clipping 
    end_slice =floats from 0 to 1.0, final slice of the clipping
    step_slices = higher value, slower is the processing of "cutting" the brain with thinner slices making the animation more gradual
    pause = how many milliseconds to wait between each slice 
    take_screen = 1 make screenshot in bitmap [there aren't other options :( ] | 0 no screenshot
    cumulative_steps = crucial for saving the screenshot without deleting the old ones generated from other animation
    
    azimuth_slice = azimuth coordinates for the clipping
    elevation_slice = inclination for the clipping, default = 0
    """

    for slc in range(int(starting_slice*step_slices),int(end_slice*step_slices)):
        gl.wait(1)
        gl.clipazimuthelevation(slc/step_slices, azimuth_slice, elevation_slice);
        
        save_name = cumulative_steps + slc
        print(save_name)
        
        if take_screen == 1:
            gl.savebmp( path +str(save_name)+ '.png')
            gl.bmpzoom(zoom_factor )
            
    cumulative_steps +=  slc 
    return cumulative_steps


#=== General Settings ===# 

zoom_factor = 1   	#Higher zoom, higher resolution of screenshot(range from 1 to N) 
                    #e.g., zoom_factor = 2 takes the screen resolution and double it 
take_screen = 0

path = 'C:\\Users\\andrea.belluzzi\\Desktop\\video_network\\frames_ani2\\'      #where to save screen

gl.scriptformvisible(0)			#remove script window (take bigger screenshot)
gl.shadername('OverlaySurface')		#type of shader 
gl.shaderquality1to10(10)		#shader quality
gl.shaderadjust('overlayDepth', 24)	#If I put OverlaySurface as shader, I have to decide the depth of the visualized cluster

gl.cameradistance(1.3)  
gl.colorbarposition(0)		#remove colorbar 


#=== Time to dance 2=== #

gl.cutout(0.00, 0.50, 0.50, 0.00, 0.00, 1.00) 
gl.azimuthelevation(90,0)

#roast chicken animation
cum_steps0 = pause(60,take_screen,0)
cum_steps1 = animation(360,1,[90,0],"y",take_screen,cum_steps0+1 )
cum_steps2 = pause(30,take_screen,cum_steps1+1)

#Clipping from left to right hemisphere 
gl.shaderadjust('overlayDepth', 5)
clipping(0,1.0,1000,take_screen,cum_steps2+1,270)
