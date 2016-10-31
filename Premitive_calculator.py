def solve(n):
  v = [0]*(n+1)
  # so that v[n] is there
  v[1] = 1  # length of the sequence to 1 is 1
  for i in range(1,n):
    if not v[i]: continue
    if v[i+1] == 0 or v[i+1] > v[i] + 1: 
      v[i+1] = v[i] + 1
    # Similar for i*2 and i*3
    if v[i+1] == 0 or v[i+1] > 2*v[i]: 
      v[i+1] = 2*v[i]
    if v[i+1] == 0 or v[i+1] > 3*v[i]: 
      v[i+1] = 3*v[i]

  solution = []
  print v
  while n > 1:
    solution.append(n)
    if v[n-1] == v[n] - 1: n = n-1
    if n%2 == 0 and v[n//2] == v[n] -1: n = n//2
    if n%3 == 0 and v[n//3] == v[n] -1: n = n//3
    # Likewise for n//3
  solution.append(1)
  return solution

print solve(10)