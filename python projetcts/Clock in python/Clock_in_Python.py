import time

def digital_clock():
    while True:
        current_time = time.strftime("%H:%M:%S")  # 24-hour format
        print(current_time, end="\r")  # overwrite the same line
        time.sleep(1)

digital_clock()