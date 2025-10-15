# Simple number generator
def simple_gen():
    for i in range(5):
        yield i

for val in simple_gen():
    print(val)