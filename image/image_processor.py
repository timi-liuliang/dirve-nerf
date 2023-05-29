import statistics

data = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

print("mean:{}, median:{}, mode:{}".format(mean, median, mode))