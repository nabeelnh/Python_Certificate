# for number in range(1, 10 + 1):
#     print(number)

def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step
        

for each_number in gen_range(5, start=0):
    print(each_number)

print(list(gen_range(10)))


##########################
# Fib generator
##########################
def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        return b

# fib = gen_fib()
# [next(fib) for _ range(50)][-1]