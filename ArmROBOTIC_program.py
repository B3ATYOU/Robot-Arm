import math
import tkinter
import time

#Display Window
LENGTH, WIDTH = 1800 , 700

ground = 30
radius = 20

angle_change_const = 1

PI = math.pi

arm_1_px = 200
arm_2_px = 300
arm_3_px = 300

arm_1_offset_px = 400

tpx_length = 600
tpx_width = 600


arm_1_a = 90
arm_2_a = 0
arm_3_a = 0

def deg_rad(deg):
    return 2*PI*deg/360

#base of the first arm will be at (0,total_pixels_width)


program_done = False

#Create basic window
window = tkinter.Tk()

geom_str = "" + str(LENGTH) + "x" + str(WIDTH)
window.geometry(geom_str)
window.title("Keyboard Interaction Example")

#Define commands (functions)
def sec_angle_inc(event=" "):
    global arm_2_a, angle_change_const
    arm_2_a = arm_2_a + angle_change_const
    print(arm_2_a)

def sec_angle_dec(event = " "):
    global arm_2_a, angle_change_const
    arm_2_a = arm_2_a - angle_change_const
    print(arm_2_a)

def third_angle_inc(event = " "):
    global arm_3_a, angle_change_const
    arm_3_a = arm_3_a + angle_change_const
    print(arm_3_a)

def third_angle_dec(event = " "):
    global arm_3_a, angle_change_const
    arm_3_a = arm_3_a - angle_change_const
    print(arm_3_a)

def draw_circle(x_px, y_px, rad_px):

    ball = canvas.create_oval(x_px-rad_px, y_px - rad_px, x_px+rad_px, y_px + rad_px, outline = "green", width = 3)

def draw_circle_inner(x_px, y_px, rad_px):
    rad_px_2 = 8

    ball = canvas.create_oval(x_px-rad_px_2, y_px - rad_px_2, x_px+rad_px_2, y_px + rad_px_2, fill = "black", width = 2)


def end_program(event=" "):
    global program_done
    program_done = True


#Bind or make a connection between a keyboard key, and
#a command (function)
window.bind("<w>", sec_angle_inc)
window.bind("<q>", sec_angle_dec)
window.bind("<Right>", third_angle_inc)
window.bind("<Left>", third_angle_dec)
window.bind("<Escape>", end_program)

counter = 1

while not program_done:

    
    arm1_px_base = [0,0]
    arm2_px_base = [0,arm_1_px]
    height_a2 = int(arm_2_px*math.sin(deg_rad(arm_2_a)))
    length_a2 = int(arm_2_px*math.cos(deg_rad(arm_2_a)))

    #ROTATIONAL PIVOTS
    arm3_px_base = [length_a2, arm_1_px + height_a2]

    pivot_points = [[0,arm_1_px],[length_a2,height_a2],[length_a2, arm_1_px + height_a2]]
    MOVE_HORIZ = 10

    counter=counter+1
    canvas = tkinter.Canvas(window, width=LENGTH, height=WIDTH, bg="light blue")

    ground_create = canvas.create_polygon((0,WIDTH),(0,WIDTH-ground),(LENGTH,WIDTH-ground),(LENGTH,WIDTH),(0,WIDTH),
        fill = "#FFF66C")

    arm_1_line = canvas.create_line(arm_1_offset_px + 0,WIDTH-ground,arm_1_offset_px + 0,WIDTH-arm_1_px - ground,width=5)
    arm_2_line = canvas.create_line(arm_1_offset_px + 0   ,  WIDTH-arm_1_px - ground   ,  int(arm_1_offset_px + 0 + arm_2_px * math.cos(deg_rad(arm_2_a)))   , int(WIDTH-arm_1_px + arm_2_px*math.sin(deg_rad(arm_2_a)) - ground)  ,
        width=5)
    arm_3_line = canvas.create_line(int(arm_1_offset_px + 0 + arm_2_px * math.cos(deg_rad(arm_2_a)))  ,   int(WIDTH-arm_1_px + arm_2_px*math.sin(deg_rad(arm_2_a))) - ground, int(arm_1_offset_px + 0 + arm_2_px * math.cos(deg_rad(arm_2_a)) + arm_3_px * math.cos(deg_rad(arm_2_a+arm_3_a)) )   , int(WIDTH-arm_1_px + arm_2_px*math.sin(deg_rad(arm_2_a)) + arm_3_px * math.sin(deg_rad(arm_2_a+arm_3_a))-ground ) , 
        width=5)
    
    exit_instructions = canvas.create_text (0 ,0, anchor = "nw",
                                            font = "Helvetica",
                                            text="Press ESC to exit; (q and w) and (left and right arrow keys) to control arms")

    draw_circle(arm_1_offset_px + 0,WIDTH-arm_1_px - ground,
        radius)
    draw_circle(int(arm_1_offset_px + 0 + arm_2_px * math.cos(deg_rad(arm_2_a))), int(WIDTH-arm_1_px + arm_2_px*math.sin(deg_rad(arm_2_a))) - ground, 
        radius )
    # draw_circle(int(arm_1_offset_px + 0 + arm_2_px * math.cos(deg_rad(arm_2_a)) + arm_3_px * math.cos(deg_rad(arm_2_a+arm_3_a)) ), int(WIDTH-arm_1_px + arm_2_px*math.sin(deg_rad(arm_2_a)) + arm_3_px * math.sin(deg_rad(arm_2_a+arm_3_a))-ground ), 
    #     radius )

    
    draw_circle_inner(arm_1_offset_px + 0,WIDTH-arm_1_px - ground,
        radius)
    draw_circle_inner(int(arm_1_offset_px + 0 + arm_2_px * math.cos(deg_rad(arm_2_a))), int(WIDTH-arm_1_px + arm_2_px*math.sin(deg_rad(arm_2_a))) - ground, 
        radius )
    draw_circle_inner(int(arm_1_offset_px + 0 + arm_2_px * math.cos(deg_rad(arm_2_a)) + arm_3_px * math.cos(deg_rad(arm_2_a+arm_3_a)) ), int(WIDTH-arm_1_px + arm_2_px*math.sin(deg_rad(arm_2_a)) + arm_3_px * math.sin(deg_rad(arm_2_a+arm_3_a))-ground ), 
        radius )


    canvas.pack()
    canvas.update()
    #After the user has seen the image, clear the window for the next image
    canvas.destroy()

#This statement executes when the loop is exited
exit()