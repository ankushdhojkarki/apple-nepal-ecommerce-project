import time

def task1():
    print("Task 1 starting...")
    time.sleep(3)
    print("Task 1 finished!")

def task2():
    print("Task 2 starting...")
    time.sleep(2)
    print("Task 2 finished!")

# Record start time
t1 = time.time()

# Run both tasks (sequentially)
task1()
task2()

# Record end time
t2 = time.time()

# Calculate total execution time  
print("Total execution time (seconds):", t2 - t1)

