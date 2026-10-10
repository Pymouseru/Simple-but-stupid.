#I don't speak English, so I used Google Translate. If you would like to help with the translation, please visit GitHub.
import os
import msvcrt

red = "\033[41m  \033[0m"#red
blue = "\033[46m  \033[0m"#blue
brown = "\033[48;5;94m  \033[0m"#brown

#HR FUNCTIONS

def c0_0():
    print(blue + red + brown)
    print(brown * 3)
    print(brown * 3)
def c0_1():
    print(red + blue + brown)
    print(brown * 3)
    print(brown * 3)
def c0_2():
    print(red  * 2 + blue)
    print(brown * 3)
    print(brown * 3)
def c1_0():
    print(red  * 2 + brown )
    print(blue + brown * 2)
    print(brown * 3)
def c1_1():
    print(red  * 2 + brown )
    print(brown  + blue + brown  )
    print(brown * 3)
def c1_2():
    print(red  * 2 + brown )
    print(brown * 2 + blue )
    print(brown * 3)
def c2_0():
    print(red  * 2 + brown )
    print(brown * 3)
    print(blue + brown * 2 )
def c2_1():
    print(red  * 2 + brown )
    print(brown * 3)
    print(brown+  blue +brown)
def c2_2():
    print(red  * 2 + brown )
    print(brown * 3)
    print(brown * 2 + blue)
# coordinates + function
shots = {
    (0, 0): c0_0,
    (0, 1): c0_1,
    (0, 2): c0_2,
    (1, 0): c1_0,
    (1, 1): c1_1,
    (1, 2): c1_2,
    (2, 0): c2_0,
    (2, 1): c2_1,
    (2, 2): c2_2,
}

x, y = 1, 1 
checking_button_events = 0
checking_for_events_at_coordinates = 0
while True:
    os.system ('cls')
    # Showing the current frame
    if (x, y) in shots:
        shots[(x, y)] ()
    else:
        print("Wall")
    print(f"\ncoordinates: ({x}, {y})")
    print(f"checking button events:{checking_button_events}")
    print (f"checking for events at coordinates:{checking_for_events_at_coordinates}")
    ход = msvcrt.getch().decode('utf-8').lower()
    old_x, old_y = x, y
    # movement
    if ход == 'w':
        x -= 1 
    elif ход == 's':
        x+= 1
    elif ход == 'a':
        y -= 1
    elif ход == 'd':
        y += 1
    elif ход == 'q':
     break
    elif ход == 'e': 
         input ("checking button events.Enter...")
    
         checking_button_events +=1
    if (x,y) == (0, 0) or (x,y) == (0, 1):
        input ("checking for events at coordinates.Enter...")
   
        checking_for_events_at_coordinates += 1
    elif (x, y) not in shots :
        print("\nWall")
        x, y = old_x, old_y
        input("Enter...")