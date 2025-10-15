# Generator with yield from

def generator_from_list(lst):
    yield from lst

print(list(generator_from_list([1,2,3])) )