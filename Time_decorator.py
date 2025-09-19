import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()      
        result = func(*args, **kwargs)
        end_time = time.time()        
        elapsed = end_time - start_time
        print(f"function time: {func.__name__}': {elapsed:.6f}")
        return result
    return wrapper


@timing_decorator
def create_list(n):
    return [i for i in range(1, n+1)]


n = int(input("how many numbers is in the list? "))
my_list = create_list(n)
print("list created, length of list:", len(my_list))
