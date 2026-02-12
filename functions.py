
# iterative factorial
def faci(n) :
    f = 1
    for i in range(1, n+1) : f *= i 
    return f

# recursive factorial
def fac(n) :
    if n == 0 : return 1
    return n * fac(n-1)

# fibonacci recursive
def fib(n) :
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-1) + fib(n-2)

# fibonacci dynamic programming
def fibd(n) :
    f = []
    f.append(0)
    f.append(1)

    for i in range(2, n+1) :
        f.append(f[i-1] + f[i-2])

    return f[n]

# the sieve of Eratosthenes (in iterative form)
def sievei(n) :
    ps = []
    for i in range(2, n+1) :

        isprime = True
        for p in ps :
            if not i % p :
                isprime = False
                break

        if isprime :
            print(i)
            ps.append(i)

# sieve of Eratosthenes (with a finite list...)
def sieve(xs) :
  if not xs : return []

  p, *ps = xs

  #print(p, ps)

  return [p] + sieve([x for x in ps if x % p])

# Ackermann's function
def ack(m,n) :
  if m == 0 : return n+1
  if n == 0 : return ack(m-1,1)
  return ack(m-1, ack(m, n-1))

# ack(3,4) = 2^(n+3) - 3 = 125
# ack(4,1) = 2^2^2^2 - 3 = 65533

# Ackermann's function (iterative version)
# credit: Alexandre Geraldo
def acki(m,n) :
    s = []
    s.append(m)
    while s :
        m = s.pop()
        if m == 0 :
            n = n+1
        elif n == 0 :
            n = 1
            s.append(m-1)
        else :
            n = n-1
            s.append(m-1)
            s.append(m)
    return n
