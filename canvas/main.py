import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype= np.uint8) + 255 
# the canvas we normally create is 0 so black
# no matter how many you add to this value, it will turn that color. For example, if we add 255, it will turn white.

cv2.line(canvas, (0,0), (512,512), (0,0,255), 5) 
# draws a line. 0,0 corresponds to the upper left place and 512,512 corresponds to the lower right.
# then the color and thickness are set. 255.0.0 is blue and 5 indicates thickness.

cv2.rectangle(canvas, (150,150), (320,320), (255,0,0), 5)
# rectangle works like a line, but creates a square at the coordinates you choose.

cv2.circle(canvas, (420,420), 50, (0,255,0), -1) 
# If we enter -1 instead of  thickness, it fills in. it works on every command.
# circle creates a circle as we know, the logic is the same, we just enter a radius instead of the 2nd coordinate.

font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(canvas, "ilkdeneyim", (100,150), font, 4, (255,0,0), 2)
# Add text on putText. Write whatever you want, but you have to adjust the font, they are all visible.


cv2.imshow("tuval", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()


