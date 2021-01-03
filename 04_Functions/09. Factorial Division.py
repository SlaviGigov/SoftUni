n = int(input())
m = int(input())
n_factorial = 1
m_factorial = 1

for i in range(1, n+1):
    n_factorial *= i

for i in range(1, m+1):
    m_factorial *= i

print(f"{n_factorial / m_factorial:.2f}")