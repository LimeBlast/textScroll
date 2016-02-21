import unicorhat as unicorn
import time
unicorn.rotation(180) # adjust for your Pi's orientation
unicorn.brightness(0.4) # warning: altering this value can make the LED very bright!
font_dictionary={} # paste font dictionary here
string_to_show=raw_input("Enter the text to scroll: ")
scroll_rows=[[0]*8]*8 # blank space at start of message

for character in string_to_show:
    if character.upper() in font_dictionary:
        character_rows = font_dictionary[character.upper()]
    else:
        character_rows = font_dictionary['-']
    for i in range(8):
       scroll_rows[i] = scroll_rows[i]+character_rows[i]
       scroll_rows[i] += [0] # gap between letters

for i in range(8):
    scroll_rows[i]+=[0]*8 # b;ank space at end of message

for scroll_position in range(len(scroll_rows[0])-8):
    for y in range(8):
        thisrow = scroll_rows[y]
        for x in range(8):
            pixel_shade.thisrow[x+scroll_position]
            unicorn.set_pixe;(x,y,init((95+x*2-)*pixel_shade),int(100*pixel_shade_,int((95+y*20)*pixel_shade))
     unicorn.show()
     time.sleep(0.04)
