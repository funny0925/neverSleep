import pyautogui
import datetime
import time
import random

a = random.randint(-50, 50)
b = random.randint(-50, 50)
p, q = pyautogui.size()
t = 0

try:
    while True:
        start_time = time.time()
        x, y = pyautogui.position()     
        datetime_dt = datetime.datetime.today()
        before_dttm = datetime_dt.strftime("%H:%M:%S")
        print(str(before_dttm) + "_" + str(pyautogui.position()))

        time.sleep(120)

        m, n = pyautogui.position()
        datetime_dt = datetime.datetime.today()
        after_dttm = datetime_dt.strftime("%H:%M:%S")
        print(str(after_dttm) + "_" + str(pyautogui.position()))

        # 視為正常人類操作行為
        while abs(x - m) >= 50 or abs(y - n) >= 50:
            t = 0
            print(f"Mouse position changed(不採取動作): ({x}, {y}) -> ({m}, {n})")
            break

        # 視為靜止狀態
        while abs(x - m) < 50 and abs(y - n) < 50:
            if (m >= (p - 150) or m <= 100) or (n >= (q - 150) or n <= 100):
                m = int(p / 2)
                n = int(q / 2)
                
            if t == 0:
                pyautogui.moveTo(p - 2, q - 2)
                pyautogui.click(p - 2, q - 2)
                t += 1
                print(f"Mouse position non-changed(採取動作): ({m}, {n}) -> ({p - 2}, {q - 2})")
                break
            else:
                pyautogui.moveTo(m + a, n + b)
                pyautogui.click(m + a, n + b)
                print(f"Mouse position non-changed(採取動作): ({m}, {n}) -> ({m + a}, {n + b})")
                break

except KeyboardInterrupt:
    print('Exit!')
