"""Calculate gcd and lcm of 2 natural numbers"""

def gcd(a, b):
    """Calculate gcd of a and b (the Euclidean Algorithm)"""
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    """Calculate lcm of a and b"""
    return (a * b) // gcd(a,b)

# Driver code
if __name__ == "__main__":
    a = 16
    b = 40

    # Function call
    print(f"gcd({a},{b}) = {gcd(a, b)}")
    print(f"lcm({a},{b}) = {lcm(a, b)}")
