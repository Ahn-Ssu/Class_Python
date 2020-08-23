import time
import threading

def longTask():
    for i in range(1,6):
        time.sleep(1)
        print("working:%s" %i)

    

print("Start")
threads = []

for i in range(5):
    t = threading.Thread(target=longTask)
    threads.append(t)

for t in threads :
    t.start()

for t in threads :
    t.join()

print("End")