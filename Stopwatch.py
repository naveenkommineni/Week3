import time
def Stopwatch(sec):
    mins=sec//60
    sec=sec%60
    hours=mins//60
    mins=mins%60
    print("Time elapsed={0}:{1}:{2}".format(int(hours),int(mins),sec))
input("press enter to start")
start_time=time.time()
input("Press enter to end")
end_time=time.time()
time_lapsed=end_time-start_time


Stopwatch(time_lapsed)
