## for gcd f(a,b)
## if a b are even => 2*f(a,b)
## if a is even b is odd => f(a/2, b) ## if b is even a is odd => f(a, b/2)
## if a b are odd => f(b, a-b)
def gcd(a:int, b:int) -> int:
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    is_even_a = a % 2 == 0
    is_even_b = b % 2 == 0
    if is_even_a and is_even_b:
        return 2 * gcd(a>>1, b>>1)
    elif is_even_a:
        return gcd(a>>1, b)
    elif is_even_b:
        return gcd(a, b>>1)
    else:
        return gcd(b, a-b)


print(gcd(512, 1024))


def lcm(a:int, b:int) -> int:
    return a*b / gcd(a, b)