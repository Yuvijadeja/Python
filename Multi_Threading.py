from time import sleep
from threading import *


class Hello(Thread):
    # run is built in method of thread
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)  # it will wait for 1 sec to run thread again


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

# it will wait to finish both thread and then print Bye
t1.join()
t2.join()

print("Bye")
