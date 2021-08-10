from joblib import Memory

memory = Memory(cachedir='/tmp/')

@memory.cache
def expensive_function(x):
    return x**2   # some computationally expensive operation here

def test_other_function():
    input_ds = expensive_function(x=10)
    ## run some tests with input_ds