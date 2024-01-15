def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_seq=[0,1]
        fib_seq.extend(map(lambda i: fib_seq[i-1]+fib_seq[i-2],range(2,n)))
        return fib_seq


print(fibonacci(20))