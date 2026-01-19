import statistics
from collections import Counter
import math
class Statistics:
    def __init__(self,ages):
        self.ages = ages
    def count(self):
        return len(self.ages)
    def sum(self):
        return sum(self.ages)
    def min(self):
        return min(self.ages)
    def max(self):
        return max(self.ages)
    def range(self):
        return max(self.ages)-min(self.ages)
    def mean(self):
        return math.ceil(statistics.mean(self.ages))
    def median(self):
        return statistics.median(self.ages)
    def mode (self):
        return statistics.mode(self.ages)
    def std(self):
        return round(statistics.stdev(self.ages),1)
    def var(self):
        return round(statistics.variance(self.ages),1)
    def freq_dist(self):
        n = len(self.ages)
        counts = Counter(self.ages)
        # Calculate (percentage, value) for each item
        dist = [((count / n) * 100.0, val) for val, count in counts.items()]
        # Sort by percentage descending
        return sorted(dist, key=lambda x: x[0], reverse=True)  
    def describe(self): 
        return (f"Count: {data.count()}\nSum: {data.sum()}\nMin: {data.min()}\nMax: {data.max()}\nRange: {data.range()}\nMean: {data.mean()}\nMedian: {data.median()}\nMode: {data.mode()}\nStandard Deviation: {data.std()}\nVariance: {data.var()}\nFrequency Distribution: {data.freq_dist()}")
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist())
print(data.describe())
