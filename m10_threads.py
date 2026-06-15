import threading
import time
import asyncio

print("MODULE 10 HANDS-ON: MULTI-THREADED TASK RUNNER")
print("-" * 60)

# --------------------------------------------------
# SHARED DATA
# --------------------------------------------------
completed_tasks = 0
lock = threading.Lock()

# --------------------------------------------------
# THREAD FUNCTION
# --------------------------------------------------
def run_task(task_name, duration):
    global completed_tasks

    print(f"{task_name} started")
    time.sleep(duration)

    with lock:
        completed_tasks += 1
        print(f"{task_name} completed")
        print(f"Total completed tasks: {completed_tasks}")

# --------------------------------------------------
# CREATE AND START THREADS
# --------------------------------------------------
print("\n1. THREADING DEMONSTRATION")

thread1 = threading.Thread(target=run_task, args=("Task 1", 2))
thread2 = threading.Thread(target=run_task, args=("Task 2", 3))
thread3 = threading.Thread(target=run_task, args=("Task 3", 1))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("All threads finished execution")

# --------------------------------------------------
# ASYNCIO DEMONSTRATION
# --------------------------------------------------
print("\n2. ASYNCIO DEMONSTRATION")

async def async_task(task_name, delay):
    print(f"{task_name} started")
    await asyncio.sleep(delay)
    print(f"{task_name} completed")

async def run_async_tasks():
    await asyncio.gather(
        async_task("Async Task A", 2),
        async_task("Async Task B", 1)
    )

asyncio.run(run_async_tasks())

print("\nLab completed successfully.")
import threading

counter = 0

def task():
    global counter
    counter += 1

threads = []

for i in range(1000):
    t = threading.Thread(target=task)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(counter)

