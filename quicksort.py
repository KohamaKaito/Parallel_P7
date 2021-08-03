import random, time, sys
from multiprocessing import Process, Pipe


def main():
   
    N = 500000
    if len(sys.argv) > 1: 
        N = int(sys.argv[1])

   
    lystbck = [random.random() for x in range(N)]

    
    lyst = list(lystbck)            
    start = time.time()             
    lyst = quicksort(lyst)         
    elapsed = time.time() - start  
    
        
    print('quicksort: %f sec' % (elapsed))

    
    time.sleep(3)
    
    lyst = list(lystbck)
    
    start = time.time()
    n = 3 
    pconn, cconn = Pipe()
    
    
    p = Process(target=quicksortParallel, \
                args=(lyst, cconn, n))
    p.start()
    
    lyst = pconn.recv()
    
    
    p.join()
    elapsed = time.time() - start


    print('Parallel quicksort: %f sec' % (elapsed))


    time.sleep(3)

    
def quicksort(lyst):
   
    if len(lyst) <= 1:
        return lyst
    pivot = lyst.pop(random.randint(0, len(lyst)-1))
    
    return quicksort([x for x in lyst if x < pivot]) \
           + [pivot] \
           + quicksort([x for x in lyst if x >= pivot])

def quicksortParallel(lyst, conn, procNum):
   

    if procNum <= 0 or len(lyst) <= 1:
        
        conn.send(quicksort(lyst))
        conn.close()
        return

    
    pivot = lyst.pop(random.randint(0, len(lyst)-1))

    leftSide = [x for x in lyst if x < pivot]
    rightSide = [x for x in lyst if x >= pivot]

    
    pconnLeft, cconnLeft = Pipe()
    
    leftProc = Process(target=quicksortParallel, \
                       args=(leftSide, cconnLeft, procNum - 1))
    
    
    pconnRight, cconnRight = Pipe()
    rightProc = Process(target=quicksortParallel, \
                       args=(rightSide, cconnRight, procNum - 1))

    
    leftProc.start()
    rightProc.start()

   
    conn.send(pconnLeft.recv() + [pivot] + pconnRight.recv())
    conn.close()

    
    leftProc.join()
    rightProc.join()



#Call the main method if run from the command line.
if __name__ == '__main__':
    main()