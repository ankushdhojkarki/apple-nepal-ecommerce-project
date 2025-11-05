import time
import threading

def task1():
    print("Task 1 starting...")
    Product.objects.create(product_name = "Random")
    time.sleep(3)
    print("Task 1 finished!")

def task2():
    print("Task 2 starting...")
    time.sleep(2)
    print("Task 2 finished!")

t1 = time.time()

# Run tasks concurrently
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

t2 = time.time()

print("Total execution time (seconds):", t2 - t1)
