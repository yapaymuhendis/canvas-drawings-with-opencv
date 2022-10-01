import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype= np.uint8) + 255 
# normalde oluşturduğumuz tuval 0 yani siyah
# bu değere kaç eklersen o renge döner. mesela 255 eklersek beyaza döner.

cv2.line(canvas, (0,0), (512,512), (0,0,255), 5) 
# çizgi çizdirir. 0,0 sol üst yere, 512,512 ise sağ alt yere denk gelir.
# daha sonra renk ve kalınlık ayarlanır. 255,0,0 mavi, 5 ise kalınlığı gösterir.

cv2.rectangle(canvas, (150,150), (320,320), (255,0,0), 5)
# rectangle ise line gibi çalışır ama seçtiğin koordinatlarda bir kare oluşturur.

cv2.circle(canvas, (420,420), 50, (0,255,0), -1) 
# kalınlık yerine -1 girersek içini doldurur. her komutta çalışır.
# circle bildiğimiz gibi daire oluşturur, bununda mantığı aynı sadece 2.kordinat yerine yarıçap giricez.

font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(canvas, "ilkdeneyim", (100,150), font, 4, (255,0,0), 2)
# putText adı üstünde yazı ekleme. ne istersen onu yaz ama fontunu ayarlaman lazım hepsi gözüküyor zaten.




cv2.imshow("tuval", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()


