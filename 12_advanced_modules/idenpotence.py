# Idempotence

# This is not considered as idempotence as this function changes
# the result if it is passed to itself
def fun(n):
    return n+10

print(fun(10))
print(fun(fun(10)))

# So, idempotence is there if f(f()) = f()
# Take this simple example

print(abs(-10))
print(abs(abs(-10)))
