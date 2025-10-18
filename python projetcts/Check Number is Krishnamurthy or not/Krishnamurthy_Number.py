import math

def is_krishnamurthy(n):
    temp = n
    sum_fact = 0
    while temp > 0:
        digit = temp % 10
        sum_fact += math.factorial(digit)
        temp //= 10
    return sum_fact == n

# Example usage
for num in range(1, 100000):
    if is_krishnamurthy(num):
        print(f"{num} is a Krishnamurthy number")