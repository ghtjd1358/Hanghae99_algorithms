    
# ===================== 테스트 6 ===================================

S = input()

results = set()

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        results.add(S[i:j])

print(len(results))
