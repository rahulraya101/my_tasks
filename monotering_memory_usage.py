# importing the module
import tracemalloc

# code or function for which memory
# has to be monitored
def app():
	lt = []
	for i in range(0, 100000):
		lt.append(i)

# starting the monitoring
tracemalloc.start()

# function call
app()

# displaying the memory
print(tracemalloc.get_traced_memory())

# stopping the library
tracemalloc.stop()


###########################################################################################################


#OUT Put will show

#The output is given in form of (current, peak),i.e, current memory is the memory 
#the code is currently using and peak memory is the maximum space the program used while executing.

#(0,3617252)


#source
#https://www.geeksforgeeks.org/monitoring-memory-usage-of-a-running-python-program/
