def calculate_score(X, N):
  points = X // 10
  return points * N
t = int(input())
for _ in range(t):
  X, N = map(int, input().split())
  score = calculate_score(X, N)
  print(score)
