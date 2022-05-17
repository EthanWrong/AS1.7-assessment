"""Test code to organise that into minutes and seconds"""
import time


# start_time = time.time()
# x = input("How long will it take you to type something here? ")
# end_time = time.time()

# total_time = round((end_time - start_time), 2)
# print(total_time)
total_time = int(input("Number of seconds to convert to seconds and minutes "
                       ">>> "))

minutes = int(total_time // 60)
if str(minutes)[-1] != "1":
    min_s = "s"
else:
    min_s = ""

and_seconds = int(total_time % 60)
if str(and_seconds)[-1] != "1":
    sec_s = "s"
else:
    sec_s = ""

print(f"{minutes} minute{min_s} and {and_seconds} second{sec_s}")
