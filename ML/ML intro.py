import numpy
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

mean = numpy.mean(speed)
median = numpy.median(speed)
mode = stats.mode(speed)
std = numpy.std(speed)
var = numpy.var(speed)
percentile = numpy.percentile(ages, 75)

print(mean)
print(median)
print(mode)
print(std)
print(var)
print(percentile)
