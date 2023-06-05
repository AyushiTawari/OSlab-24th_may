#Python program for the above approach
 
import threading
import time
 
# Shared Memory variables
CAPACITY = 10
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0
 
# Declaring Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)
 
# Producer Thread Class
class Producer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index
    global mutex, empty, full
     
    items_produced = 0
    counter = 0
     
    while items_produced < 20:
      empty.acquire()
      mutex.acquire()
       
      counter += 1
      buffer[in_index] = counter
      in_index = (in_index + 1)%CAPACITY
      print("Producer produced : ", counter)
       
      mutex.release()
      full.release()
       
      time.sleep(1)
       
      items_produced += 1
 
# Consumer Thread Class
class Consumer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index, counter
    global mutex, empty, full
     
    items_consumed = 0
     
    while items_consumed < 20:
      full.acquire()
      mutex.acquire()
       
      item = buffer[out_index]
      out_index = (out_index + 1)%CAPACITY
      print("Consumer consumed item : ", item)
       
      mutex.release()
      empty.release()      
       
      time.sleep(2.5)
       
      items_consumed += 1
 
# Creating Threads
producer = Producer()
consumer = Consumer()
 
# Starting Threads
consumer.start()
producer.start()
 
# Waiting for threads to complete
producer.join()
consumer.join()

#Output
Producer produced :  1
Consumer consumed item :  1
Producer produced :  2
Producer produced :  3
Consumer consumed item :  2
Producer produced :  4
Producer produced :  5
Consumer consumed item :  3
Producer produced :  6
Producer produced :  7
Producer produced :  8
Consumer consumed item :  4
Producer produced :  9
Producer produced :  10
Consumer consumed item :  5
Producer produced :  11
Producer produced :  12
Producer produced :  13
Consumer consumed item :  6
Producer produced :  14
Producer produced :  15
Consumer consumed item :  7
Producer produced :  16
Producer produced :  17
Consumer consumed item :  8
Producer produced :  18
Consumer consumed item :  9
Producer produced :  19
Consumer consumed item :  10
Producer produced :  20
Consumer consumed item :  11
Consumer consumed item :  12
Consumer consumed item :  13
Consumer consumed item :  14
Consumer consumed item :  15
Consumer consumed item :  16
Consumer consumed item :  17
Consumer consumed item :  18
Consumer consumed item :  19
Consumer consumed item :  20
