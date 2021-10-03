import statistics
import math

data = [60,61,65,63,98,99,90,95,91,96]


mean = statistics.mean(data)

devations = []

for i in data :
    deviation = i - mean
    devations.append(deviation)

squaredeviations=[]
for x in devations :
    squaredeviation = x * x
    squaredeviations.append(squaredeviation)

variances = statistics.mean(squaredeviations)
standarddeviatins = math.sqrt(variances)

print(standarddeviatins)
