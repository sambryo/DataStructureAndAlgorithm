import time 

def timing_functions(some_functions): 

    def wrapper(): 
        t1 = time.time()
        some_functions()
        t2 = time.time()
        return "Time it took to run the functions : " + str((t2-t1)) + "\n"
        
    return wrapper()

@timing_functions
def some_functions(): 
    num_list = []
    for i in range(1, 10000): 
        num_list.append(i)
    print ("Sum of all the numbers:" + str(sum(num_list)))

