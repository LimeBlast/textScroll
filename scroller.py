import unicornhat as unicorn
import time

unicorn.rotation(180) # adjust for your Pi's orientation
unicorn.brightness(0.4) # warning: altering this value can make the LED very bright!

font_dictionary={' ': [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], '$': [[0.15, 1, 1, 1, 0.15], [1, 0.15, 1, 0.15, 1], [1, 0.15, 1, 0, 0.15], [0.15, 1, 1, 0.75, 0.15], [0.15, 0, 1, 0.15, 1], [1, 0.15, 1, 0.15, 1], [0.15, 1, 1, 1, 0.15], [0, 0, 1, 0, 0]], '(': [[0, 0.75, 0.15], [0.15, 0.75, 0], [0.75, 0.15, 0], [1, 0.15, 0], [1, 0, 0], [1, 0.15, 0], [0.75, 0.15, 0], [0.15, 0.75, 0]], ',': [[0], [0], [0], [0], [0], [0], [1], [1]], '0': [[0.15, 0.75, 1, 0.75, 0.15], [0.75, 0.75, 0.15, 0.75, 0.75], [1, 0.15, 0, 0.15, 1], [1, 0, 0, 0, 1], [1, 0.15, 0, 0.15, 1], [0.75, 0.75, 0.15, 0.75, 0.75], [0.15, 0.75, 1, 0.75, 0.15], [0, 0, 0, 0, 0]], '4': [[0, 0.15, 1, 0], [0, 0.15, 1, 0], [0, 0.15, 1, 0], [0.15, 0, 1, 0], [0.15, 0, 1, 0], [1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0]], '8': [[0.15, 1, 1, 1, 0.15], [1, 0.15, 0, 0.15, 1], [1, 0.15, 0, 0.15, 1], [0.15, 1, 1, 1, 0.15], [1, 0.15, 0, 0.15, 1], [1, 0.15, 0, 0.15, 1], [0.15, 1, 1, 1, 0.15], [0, 0, 0, 0, 0]], '<': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0.15], [0, 0, 0.15, 0.75, 0.75], [0.15, 0.75, 0.15, 0, 0], [0.15, 0.75, 0.75, 0.15, 0], [0, 0, 0.15, 0.75, 0.75], [0, 0, 0, 0, 0]], '@': [[0, 1, 1, 1, 1, 1, 0], [1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]], 'D': [[1, 1, 1, 0.75, 0.15], [1, 0, 0.15, 0.75, 0.75], [1, 0, 0, 0.15, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0.15, 1], [1, 0, 0.15, 0.75, 0.75], [1, 1, 1, 0.75, 0.15], [0, 0, 0, 0, 0]], 'H': [[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 'L': [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]], 'P': [[1, 1, 1, 1, 0.15], [1, 0, 0, 0.15, 1], [1, 0, 0, 0.15, 1], [1, 1, 1, 1, 0.15], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 'T': [[1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], 'X': [[0.15, 0.75, 0, 0, 0.75, 0.15], [0, 0.75, 0.15, 0.15, 0.75, 0], [0, 0.15, 1, 0.75, 0.15, 0], [0, 0, 0.75, 0.75, 0, 0], [0, 0.15, 0.75, 0.75, 0.15, 0], [0.15, 1, 0.15, 0.15, 0.75, 0], [0.75, 0.75, 0, 0, 0.75, 0.75], [0, 0, 0, 0, 0, 0]], '\\': [[1, 0.15, 0], [0.75, 0.15, 0], [0.15, 0.75, 0], [0.15, 0.75, 0], [0, 1, 0.15], [0, 0.75, 0.15], [0, 0.15, 0.75], [0, 0, 0]], 'd': [[0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0.15, 1, 1, 0.75, 1], [1, 0.75, 0.15, 0.75, 1], [1, 0.15, 0, 0.15, 1], [1, 0.75, 0.15, 0.75, 1], [0.15, 1, 1, 0.75, 1], [0, 0, 0, 0, 0]], 'h': [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0.75, 1, 0.75], [1, 0.15, 0.15, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0]], 'l': [[1], [1], [1], [1], [1], [1], [1], [0]], 'p': [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0.75, 1, 0.15], [1, 0.15, 0.15, 1], [1, 0, 0, 1], [1, 0.15, 0.15, 1], [1, 0.75, 1, 0.15], [1, 0, 0, 0]], 't': [[0, 0, 0], [0, 1, 0], [1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0.15], [0, 1, 1], [0, 0, 0]], 'x': [[0, 0, 0, 0], [0, 0, 0, 0], [0.75, 0.15, 0.15, 0.75], [0, 0.75, 0.75, 0.15], [0, 0.75, 0.75, 0], [0.15, 0.75, 0.75, 0.15], [0.75, 0.15, 0.15, 0.75], [0, 0, 0, 0]], "'": [[1], [1], [0.15], [0], [0], [0], [0], [0]], '+': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 0], [1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 0, 0]], '/': [[0, 0.15, 0.75], [0, 0.75, 0.15], [0, 1, 0.15], [0.15, 0.75, 0], [0.15, 0.75, 0], [0.75, 0.15, 0], [1, 0.15, 0], [0, 0, 0]], '3': [[0.15, 1, 1, 1, 0.15], [1, 0.15, 0, 0.15, 1], [0, 0, 0.15, 0.15, 1], [0, 0, 1, 1, 0.15], [0, 0, 0, 0.15, 1], [1, 0.15, 0, 0.15, 1], [0.15, 1, 1, 1, 0.15], [0, 0, 0, 0, 0]], '7': [[1, 1, 1, 1], [0, 0, 0.15, 0.75], [0, 0, 0.75, 0.15], [0, 0.15, 0.75, 0], [0, 0.15, 0.75, 0], [0, 0.75, 0.15, 0], [0, 1, 0.15, 0], [0, 0, 0, 0]], ';': [[0], [0], [1], [0], [0], [0], [1], [1]], '?': [[0.75, 1, 1, 0.15], [1, 0.15, 0.15, 1], [0, 0, 0.15, 1], [0, 0.15, 1, 0.15], [0, 1, 0.15, 0], [0, 0.15, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 'C': [[0, 0.75, 1, 1, 0.75, 0.15], [0.75, 0.75, 0.15, 0.15, 0.15, 1], [1, 0.15, 0, 0, 0, 0], [1, 0.15, 0, 0, 0, 0], [1, 0.15, 0, 0, 0, 0], [0.75, 0.75, 0.15, 0, 0.15, 1], [0, 0.75, 1, 1, 0.75, 0.15], [0, 0, 0, 0, 0, 0]], 'G': [[0, 0.75, 1, 1, 1, 0.75, 0.15], [0.75, 1, 0.15, 0.15, 0.15, 0.75, 0.75], [1, 0.15, 0, 0, 0, 0, 0], [1, 0.15, 0, 0, 1, 1, 1], [1, 0.15, 0, 0, 0, 0.15, 1], [0.15, 1, 0.15, 0.15, 0.15, 0.75, 1], [0, 0.15, 1, 1, 1, 0.15, 1], [0, 0, 0, 0, 0, 0, 0]], 'K': [[1, 0, 0, 0.15, 0.75, 0.15], [1, 0, 0.15, 1, 0.15, 0], [1, 0.15, 1, 0.15, 0, 0], [1, 0.75, 1, 0.15, 0, 0], [1, 0.15, 0.15, 0.75, 0, 0], [1, 0, 0, 0.75, 0.15, 0], [1, 0, 0, 0.15, 1, 0.15], [0, 0, 0, 0, 0, 0]], 'O': [[0, 0.15, 1, 1, 1, 0.15, 0], [0.15, 1, 0.15, 0.15, 0.15, 1, 0.15], [1, 0.15, 0, 0, 0, 0.15, 1], [1, 0.15, 0, 0, 0, 0.15, 1], [1, 0.15, 0, 0, 0, 0.15, 1], [0.15, 1, 0.15, 0.15, 0.15, 1, 0.15], [0, 0.15, 1, 1, 1, 0.15, 0], [0, 0, 0, 0, 0, 0, 0]], 'S': [[0.15, 1, 1, 1, 0.15], [1, 0.15, 0, 0.15, 1], [1, 0.15, 0, 0, 0], [0.15, 1, 0.75, 0.75, 0.15], [0, 0, 0.15, 0.75, 1], [1, 0.15, 0, 0.15, 1], [0.15, 1, 1, 1, 0.15], [0, 0, 0, 0, 0]], 'W': [[1, 0.15, 0, 0.15, 0.75, 0, 0, 0.75], [0.75, 0.15, 0, 0.75, 1, 0.15, 0, 1], [0.15, 0.75, 0, 1, 0.75, 0.15, 0.15, 1], [0.15, 0.75, 0.15, 0.75, 0.15, 0.75, 0.15, 0.75], [0, 1, 0.75, 0.75, 0, 1, 0.75, 0.15], [0, 0.75, 1, 0.15, 0, 0.75, 1, 0.15], [0, 0.75, 1, 0, 0, 0.75, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]], '[': [[1, 0.75], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]], '_': [[], [], [], [], [], [], [], []], 'c': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.15, 0.75, 1, 1, 0.15], [0.75, 0.75, 0.15, 0.15, 1], [1, 0.15, 0, 0, 0], [1, 0.75, 0.15, 0.15, 1], [0.15, 0.75, 1, 1, 0.15], [0, 0, 0, 0, 0]], 'g': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.15, 1, 1, 0.75, 1], [1, 0.15, 0.15, 0.75, 1], [1, 0.15, 0, 0.15, 1], [1, 0.15, 0.15, 0.75, 1], [0.15, 1, 1, 0.75, 1], [1, 0.15, 0.15, 0.75, 1]], 'k': [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0.75, 0.75, 0], [1, 0.75, 0.75, 0, 0], [1, 0.75, 0.75, 0, 0], [1, 0, 0.75, 0.15, 0], [1, 0, 0.15, 1, 0.15], [0, 0, 0, 0, 0]], 'o': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.15, 0.75, 1, 1, 0.15], [0.75, 0.75, 0.15, 0.75, 1], [1, 0.15, 0, 0.15, 1], [0.75, 0.75, 0.15, 0.75, 1], [0.15, 0.75, 1, 1, 0.15], [0, 0, 0, 0, 0]], 's': [[0, 0, 0, 0], [0, 0, 0, 0], [0.15, 1, 1, 0.15], [1, 0.15, 0.15, 1], [0.75, 1, 0.75, 0.15], [1, 0.15, 0.15, 1], [0.15, 1, 1, 0.75], [0, 0, 0, 0]], 'w': [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 0.15, 1, 0, 0.75, 0.75], [0.75, 0.15, 0.75, 1, 0.15, 0.75, 0.15], [0.15, 0.75, 1, 0.75, 0.15, 0.75, 0], [0.15, 0.75, 1, 0.15, 1, 0.75, 0], [0, 0.75, 0.75, 0, 1, 0.15, 0], [0, 0, 0, 0, 0, 0, 0]], '{': [[0, 0.75, 1], [0, 1, 0.15], [0, 1, 0], [0.15, 1, 0], [0.75, 0.75, 0], [0.15, 1, 0], [0, 1, 0], [0, 1, 0.15]], '"': [[1, 1], [1, 1], [0.15, 0.15], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], '&': [[0, 0.15, 1, 0.15, 0, 0], [0, 1, 0.15, 1, 0, 0], [0, 0.75, 0.75, 0.75, 0, 0], [0.15, 0.75, 0.75, 0.15, 0.15, 0], [1, 0.15, 0.15, 1, 0.75, 0], [1, 0.15, 0.15, 1, 0.75, 0], [0.15, 1, 1, 0.15, 0.75, 0.15], [0, 0, 0, 0, 0, 0]], '*': [[0.15, 1, 0.15], [0.75, 1, 0.75], [0.15, 0.15, 0.15], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], '.': [[0], [0], [0], [0], [0], [0], [1], [0]], '2': [[0.15, 1, 1, 1, 0.15], [1, 0.15, 0.15, 0.15, 1], [0, 0, 0, 0.15, 1], [0, 0, 0.15, 1, 0.15], [0, 0.15, 0.75, 0.15, 0], [0, 0.15, 0, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0]], '6': [[0, 0.75, 1, 1, 0.15], [0.75, 0.75, 0.15, 0.75, 0.75], [1, 0.15, 0, 0, 0], [1, 0.75, 1, 1, 0.15], [1, 0.15, 0, 0.15, 1], [0.75, 0.15, 0, 0.15, 1], [0.15, 1, 1, 1, 0.15], [0, 0, 0, 0, 0]], ':': [[0], [0], [1], [0], [0], [0], [1], [0]], '>': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.15, 0, 0, 0, 0], [0.15, 0.75, 0.75, 0.15, 0], [0, 0, 0.15, 0.75, 0.75], [0, 0.15, 0.75, 0.75, 0.15], [0.15, 0.75, 0.15, 0, 0], [0, 0, 0, 0, 0]], 'B': [[1, 1, 1, 1, 0.15], [1, 0, 0, 0.15, 1], [1, 0, 0, 0.15, 1], [1, 1, 1, 1, 0.15], [1, 0, 0, 0.15, 1], [1, 0, 0, 0.15, 1], [1, 1, 1, 1, 0.15], [0, 0, 0, 0, 0]], 'F': [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]], 'J': [[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [1, 0.15, 0.15, 1], [0.75, 1, 1, 0.15], [0, 0, 0, 0]], 'N': [[1, 0.15, 0, 0, 1], [1, 0.75, 0, 0, 1], [1, 0.75, 0.15, 0, 1], [1, 0, 0.75, 0, 1], [1, 0, 0.15, 0.15, 1], [1, 0, 0, 0.75, 1], [1, 0, 0, 0.15, 1], [0, 0, 0, 0, 0]], 'R': [[1, 1, 1, 1, 0.15, 0], [1, 0, 0, 0.15, 1, 0], [1, 0, 0, 0.15, 1, 0], [1, 1, 1, 1, 0.15, 0], [1, 0, 0, 0.15, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0.75], [0, 0, 0, 0, 0, 0]], 'V': [[0.75, 0.15, 0, 0, 0.15, 0.75], [0.15, 0.75, 0, 0, 0.75, 0.15], [0.15, 1, 0, 0.15, 1, 0], [0, 0.75, 0.15, 0.15, 0.75, 0], [0, 0.15, 0.75, 0.75, 0.15, 0], [0, 0.15, 1, 0.75, 0, 0], [0, 0, 0.75, 0.75, 0, 0], [0, 0, 0, 0, 0, 0]], 'Z': [[0.75, 1, 1, 1, 1, 0.15], [0, 0, 0, 0.15, 1, 0.15], [0, 0, 0.15, 1, 0.15, 0], [0, 0, 0.75, 0.15, 0, 0], [0, 0.75, 0.75, 0, 0, 0], [0.15, 0.75, 0, 0, 0, 0], [0.75, 1, 1, 1, 1, 0.15], [0, 0, 0, 0, 0, 0]], '^': [[0, 0.75, 0.75, 0], [0, 0.75, 0.75, 0.15], [0.15, 0.15, 0.15, 0.75], [0.15, 0.15, 0, 0.15], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 'b': [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0.75, 1, 0.15], [1, 0.15, 0.15, 1], [1, 0, 0, 1], [1, 0.15, 0.15, 1], [1, 0.75, 1, 0.15], [0, 0, 0, 0]], 'f': [[0, 0.75, 1], [0, 1, 0.15], [1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]], 'j': [[0, 1], [0, 0], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0.15, 1]], 'n': [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0.75, 1, 0.75], [1, 0.15, 0.15, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0]], 'r': [[0, 0, 0], [0, 0, 0], [1, 0.75, 0.75], [1, 0.15, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 0, 0]], 'v': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.75, 0.15, 0, 0.75, 0.15], [0.75, 0.15, 0, 0.75, 0], [0.15, 0.75, 0.15, 0.75, 0], [0, 0.75, 0.75, 0.15, 0], [0, 0.75, 0.75, 0, 0], [0, 0, 0, 0, 0]], 'z': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.75, 1, 1, 1, 0], [0, 0, 0.15, 0.75, 0], [0, 0.15, 0.75, 0, 0], [0.15, 0.75, 0, 0, 0], [0.75, 1, 1, 1, 0.15], [0, 0, 0, 0, 0]], '~': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.75, 1, 0.75, 0.15, 1], [1, 0.15, 0.75, 1, 0.75], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], '!': [[1], [1], [1], [1], [0.75], [0.15], [1], [0]], '%': [[0.15, 1, 1, 0.15, 0, 0.15, 0.15, 0], [1, 0.15, 0.15, 1, 0, 0.15, 0, 0], [1, 0.15, 0.15, 1, 0.15, 0.15, 0, 0], [0.15, 1, 1, 0.15, 0.75, 0, 0, 0], [0, 0, 0, 0.75, 0.15, 0.75, 1, 0.75], [0, 0, 0.15, 0.75, 0, 1, 0.15, 1], [0, 0, 0.75, 0.15, 0, 0.75, 1, 0.75], [0, 0, 0, 0, 0, 0, 0, 0]], ')': [[0.15, 0.75, 0], [0, 0.75, 0.15], [0, 0.15, 0.75], [0, 0.15, 1], [0, 0, 1], [0, 0.15, 1], [0, 0.15, 0.75], [0, 0.75, 0]], '-': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 1, 0.15], [0, 0, 0], [0, 0, 0], [0, 0, 0]], '1': [[0.15, 1], [1, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 0]], '5': [[0.15, 1, 1, 1, 0.75], [0.15, 0.75, 0, 0, 0], [0.15, 0.75, 1, 1, 0.15], [0.75, 0.75, 0.15, 0.75, 1], [0, 0, 0, 0.15, 1], [1, 0.75, 0.15, 0.75, 0.75], [0.15, 1, 1, 0.75, 0.15], [0, 0, 0, 0, 0]], '9': [[0.15, 0.75, 1, 0.75, 0.15], [0.75, 0.75, 0.15, 0.75, 0.75], [1, 0.15, 0, 0.15, 1], [1, 0.75, 0.15, 0.75, 1], [0.15, 1, 1, 0.75, 1], [0.75, 0.75, 0.15, 0.75, 0.75], [0.15, 1, 1, 0.75, 0.15], [0, 0, 0, 0, 0]], '=': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.75, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0.75, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 'A': [[0, 0, 0.75, 0.75, 0, 0], [0, 0.15, 0.75, 1, 0.15, 0], [0, 0.15, 0.75, 0.75, 0.15, 0], [0, 0.75, 0.15, 0.15, 0.75, 0], [0.15, 1, 1, 1, 1, 0.15], [0.15, 0.75, 0, 0, 0.75, 0.15], [0.75, 0.15, 0, 0, 0.15, 0.75], [0, 0, 0, 0, 0, 0]], 'E': [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]], 'I': [[1], [1], [1], [1], [1], [1], [1], [0]], 'M': [[1, 0.75, 0, 0, 0.75, 1], [1, 0.75, 0, 0, 0.75, 1], [1, 0.75, 0.15, 0.15, 0.75, 1], [1, 0.15, 0.15, 0.15, 0.15, 1], [1, 0.15, 0.75, 0.75, 0.15, 1], [1, 0, 0.75, 0.75, 0, 1], [1, 0, 0.75, 0.75, 0, 1], [0, 0, 0, 0, 0, 0]], 'Q': [[0, 0.15, 1, 1, 1, 0.15, 0], [0.15, 1, 0.15, 0.15, 0.15, 1, 0.15], [1, 0.15, 0, 0, 0, 0.15, 1], [1, 0.15, 0, 0, 0, 0.15, 1], [1, 0.15, 0, 0, 0.15, 0.15, 1], [0.15, 1, 0.15, 0.15, 0.75, 1, 0.15], [0, 0.15, 1, 1, 1, 0.75, 0.75], [0, 0, 0, 0, 0, 0, 0.15]], 'U': [[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0.15, 0.15, 0.15, 1], [0.15, 1, 1, 1, 0.15], [0, 0, 0, 0, 0]], 'Y': [[0.15, 1, 0, 0, 0, 1, 0.15], [0, 0.75, 0.15, 0, 0.15, 0.75, 0], [0, 0.15, 1, 0.15, 1, 0.15, 0], [0, 0, 0.75, 1, 0.75, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]], ']': [[1, 0.75], [0, 0.75], [0, 0.75], [0, 0.75], [0, 0.75], [0, 0.75], [0, 0.75], [0, 0.75]], 'a': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.15, 1, 1, 0.75, 0], [1, 0.15, 0.15, 1, 0], [0.15, 0.75, 0.75, 1, 0], [1, 0.75, 0.75, 1, 0.15], [0.75, 1, 0.75, 0.75, 0.75], [0, 0, 0, 0, 0]], 'e': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.15, 0.75, 1, 1, 0.15], [0.75, 0.15, 0.15, 0.15, 0.75], [1, 1, 1, 1, 1], [0.75, 0.15, 0.15, 0.75, 0.75], [0.15, 0.75, 1, 0.75, 0.15], [0, 0, 0, 0, 0]], 'i': [[1], [0], [1], [1], [1], [1], [1], [0]], 'm': [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 0.75, 0.75, 0.75, 1, 0.75], [1, 0.15, 1, 0.15, 0.15, 1], [1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0]], 'q': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.15, 1, 1, 0.75, 1], [0.75, 0.75, 0.15, 0.75, 1], [1, 0.15, 0, 0.15, 1], [1, 0.75, 0.15, 0.75, 1], [0.15, 1, 1, 0.75, 1], [0, 0, 0, 0, 1]], 'u': [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0.15, 0.15, 1], [0.75, 1, 0.75, 1], [0, 0, 0, 0]], 'y': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0.75, 0.15, 0, 0.75, 0.15], [0.75, 0.75, 0, 0.75, 0], [0.15, 0.75, 0.15, 0.75, 0], [0, 0.75, 0.75, 0.15, 0], [0, 0.15, 1, 0, 0], [0, 0.75, 0.75, 0, 0]], '}': [[1, 0.75, 0], [0.15, 1, 0], [0, 1, 0], [0, 1, 0.15], [0, 0.75, 0.75], [0, 1, 0.15], [0, 1, 0], [0.15, 1, 0]]} # paste font dictionary here

string_to_show=raw_input("Enter the text to scroll: ")
scroll_rows=[[0]*8]*8 # blank space at start of message

for character in string_to_show:
    if character in font_dictionary:
        character_rows = font_dictionary[character]
    else:
        character_rows = font_dictionary['-']
    for i in range(8):
       scroll_rows[i] = scroll_rows[i]+character_rows[i]
       scroll_rows[i] += [0] # gap between letters

for i in range(8):
    scroll_rows[i]+=[0]*8 # blank space at end of message

for scroll_position in range(len(scroll_rows[0])-8):
    for y in range(8):
        thisrow = scroll_rows[y]
        for x in range(8):
            pixel_shade=thisrow[x+scroll_position]
            unicorn.set_pixel(x,y,int((95+x*20)*pixel_shade),int(100*pixel_shade),int((95+y*20)*pixel_shade))
    unicorn.show()
    time.sleep(0.04)
