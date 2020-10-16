

def fibbonacci_generator():
    f1 = f2 = 1
    while True:
        yield f2
        f1, f2 = f2, f1 + f2


gen = fibbonacci_generator()

for _ in range(20):
    print(next(gen))
