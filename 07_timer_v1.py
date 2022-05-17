"""Test code to see if finding the difference between a start time variable
and end time variable will work to find the total time taken"""
import time


start_time = time.time()
x = input("How long will it take you to type something here? ")
end_time = time.time()

total_time = end_time - start_time
print(total_time)
