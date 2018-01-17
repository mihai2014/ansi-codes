from __future__ import print_function
from ansi_codes import *

def test():
    print(sys.version_info.major)
    for i in range(100):
        if sys.version_info.major == 3:
            print(Green,EraseDisplay,XY(0,0),"Origin-(0,0)",sep='')
            print(Blue,XY(10,5),EraseLine,i,"%",sep='',end='',flush=True)
            print(Red,XY(11,5),EraseLine,i,"%",sep='',end='',flush=True)
        else:
            print(Green,EraseDisplay,XY(0,0),"Origin-(0,0)")
            sys.stdout.write(Blue + XY(10,5) + EraseLine + str(i) + "%")
            sys.stdout.write(Red + XY(11,5) + EraseLine + str(i) + "%")
            sys.stdout.flush()
        time.sleep(.1)
    print(Reset)


test()
