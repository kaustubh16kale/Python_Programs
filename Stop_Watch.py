import time
def stopwatch():
    # start=print("space to start the watch: ")
    # stop=None
    # seconds=0
    # if start==" ":
    #     while stop!="*":
    #         time.sleep(1)
    #         seconds+=1
    #         print(seconds)
    #         print(" enter * to stop the watch ")

    input("Press Enter to start the stopwatch")
    start = time.time()
    input("Press Enter to stop the stopwatch")
    end = time.time()
    elapsed = end - start
    print("Elapsed time:", round(elapsed, 2), "seconds")

def main():
    stopwatch()

if __name__=="__main__":
    main()

        

