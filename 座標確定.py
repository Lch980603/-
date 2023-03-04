# 東海大学
# 工学研究科　機械工学専攻
# 稲田研究室　
# 1CEMM106　李春暉

import time
import pyautogui as pag
try:
 while True:

  screenWidth, screenHeight = pag.size()

  x,y = pag.position()
  posStr ='座標：' + str(x).rjust(4)+','+str(y).rjust(4)
  print(posStr)
  time.sleep(1)

except KeyboardInterrupt:
 print('end....')