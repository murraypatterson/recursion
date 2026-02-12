
-- factorial
fac :: Int -> Int
fac 0 = 1
fac n = n * fac (n-1)

-- Fibonacci
fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

-- sieve of Eratosthenes
sieve (p:ps) = p : sieve [x | x <- ps, mod x p /= 0]

-- Ackermann's function
a :: Int -> Int -> Int
a 0 n = n + 1
a m 0 = a (m-1) 1
a m n = a (m-1) (a m (n-1))
