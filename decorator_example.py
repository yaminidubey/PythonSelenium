import time
from datetime import datetime


def B(fun):
    def A(x):
        start = datetime.now()
        fun(x)
        time.sleep(5)
        end = datetime.now()
        print("time taken = " + str((end - start).seconds))
    return A

@B
def C(x):
    print(x+1)

C(3)