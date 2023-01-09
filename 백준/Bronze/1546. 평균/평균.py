import statistics
N = int(input())
scores = list(map(int,input().split()))

change_scores = [i/max(scores)*100 for i in scores ]
print(statistics.mean(change_scores))