#level2 task4 a fibonacci sequence generator
def fibonacci(n):
  if n <= 1:
    return [n]

  fib_seq = [0, 1]
  for i in range(2, n):
    next_term = fib_seq[i - 1] + fib_seq[i - 2]
    fib_seq.append(next_term)

  return fib_seq

num_terms = int(input("Enter the number of terms: "))
fibonacci_sequence = fibonacci(num_terms)
print(fibonacci_sequence)
