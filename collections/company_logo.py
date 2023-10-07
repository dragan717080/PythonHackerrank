from collections import  Counter

freqs = dict(Counter(input()))
print("\n".join([f"{item[0]} {str(item[1])}" for item in sorted(freqs.items(), key=lambda item: (-item[1], item[0]))[:3]]))
