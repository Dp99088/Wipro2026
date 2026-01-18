import threading
def task():
    print("Thread is running")
    for i in range(2000):
        print(f"Count: {i}")
def task2():
    print("Second thread is running")
    for i in range(2001,4000):
        print(f"Count: {i}")
t=threading.Thread(target=task)
t2 = threading.Thread(target=task2)
t.start()
t2.start()
t.join()
t2.join()
print("Thread has finished")