import statistics
from random import randint

nums = []

for i in range(0,5):
    nums.append(randint(1,5))

print(nums)

#平均値
print(statistics.mean(nums))

#中央値
print(statistics.median(nums))

#中央値(low)
print(statistics.median_low(nums))

#最頻値
print(statistics.mode(nums))


#母分散
print(statistics.pvariance(nums))

#標準偏差
print(statistics.pstdev(nums))
