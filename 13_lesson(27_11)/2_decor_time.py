from datetime import datetime

def timer():
    current_time = datetime.now()
    start = current_time.strftime("%H:%M:%S")
    return start

print(timer())