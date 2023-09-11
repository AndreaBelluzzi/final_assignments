### Animation 1 MRIcroGL ###
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
    
    for stp in range(1, steps):
        # Note how you could have simplified the following in a dictionary to avoid the excess
        # of conditionals:
        # azimuthelevation_args_dict = {1: {"x": (starting_pos[0]+(stp),starting_pos[1]),
        #                                   "y": (starting_pos[0],starting_pos[1]+stp)}, ...}
        # 
        # args = azimuthelevation_args_dict[direction_step][axis2rotate]
        # gl.azimuthelevation(*args) (equivalent to gl.azimuthelevation(args[0], args[1]))
        
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
    for p in range(1, time):
        gl.wait(1)       
        save_name = cumulative_steps + p
        print(save_name)
        
        if take_screen == 1:
            gl.savebmp( path +str(save_name)+ '.png')
            gl.bmpzoom(zoom_factor )
            
    cumulative_steps +=  p 
    
    return cumulative_steps


#=== General Settings ===# 

zoom_factor = 1   	#Higher zoom, higher resolution of screenshot(range from 1 to N) 
                    #e.g., zoom_factor = 2 takes the screen resolution and double it 
take_screen = 0  # LP Why does this has to be an int? make it a bool so you don't compare if ==0 and just use the vale!

path = 'C:\\Users\\andrea.belluzzi\\Desktop\\video_network\\frames_ani1\\'      #where to save screen

gl.scriptformvisible(0)			#remove script window (take bigger screenshot)
gl.shadername('OverlaySurface')		#type of shader 
gl.shaderquality1to10(10)		#shader quality
gl.shaderadjust('overlayDepth', 24)	#If I put OverlaySurface as shader, I have to decide the depth of the visualized cluster

gl.cameradistance(1.3)  
gl.colorbarposition(0)		#remove colorbar 

#=== Time to Dance - animation 1===#

gl.azimuthelevation(0,10)  #little adjustmentto the camera
gl.cutout(0.00, 0.50, 0.50, 0.00, 0.00, 1.00)    #Whole brain

#Complete Revolution
cum_steps0 = pause(30,take_screen,0)
cum_steps1 = animation(360,1,[0,10],"x",take_screen,cum_steps0+1 )

#Medial View
gl.cutout(0.50, 0.00, 0.00, 0.00, 1.00, 1.00)    #remove left hemisphere
cum_steps2 = pause(60,take_screen,cum_steps1+1)
cum_steps3 = animation(180,1,[0 ,10],"x",take_screen,cum_steps2+1 )

gl.cutout(0.50, 0.00, 0.00, 1.00, 1.00, 1.00)    #remove right hemisphere
cum_steps4 = pause(30,take_screen,cum_steps3+1)
cum_steps5 = animation(180,1,[180 ,10],"x",take_screen,cum_steps4+1 )

#Superior view
gl.cutout(0.00, 0.50, 0.50, 0.00, 0.00, 1.00)    #Whole brain
cum_steps6 = pause(10,take_screen,cum_steps5+1)
cum_steps7 = animation(80,1,[0 ,10],"y",take_screen,cum_steps6+1 )

#Inferior view
cum_steps8 = pause(60,take_screen,cum_steps7+1)
cum_steps9 = animation(180,-1,[0 ,90],"y",take_screen,cum_steps8+1)
