from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

hours = pd.read_csv("hour.csv")
print(hours.head())
print(hours.tail())

# years = [2017, 2018, 2019, 2020, 2021, 2022]
# prize_winnings = [8000, 50000,100000, 200000, 100000, 70000]

# plt.plot(years, prize_winnings, color = "red", marker = "+")
# plt.title("sh1vy Esports Prize Winnings")
# plt.xlabel("Years")
# plt.ylabel("Prize Money won")
# plt.legend()
# plt.show()

# movies = ["A", "B", "C", "D", "E",]
# number_of_awards = [5,6,11,13,1]

# plt.bar(range(len(movies)), number_of_awards)
# plt.xlabel("Movies")
# plt.ylabel("Awards won")
# plt.title("Award Winning Movies")

# plt.xticks(range(len(movies)), movies)
# plt.show()

grades = [83, 95, 91, 87,70, 0, 85,82,100,67,73,77,0]

#Bucket grades by decile, put 100 in with 90

# histogram = Counter(min(grade // 10 * 10 ,90) for grade in grades)

# plt.bar([x+5 for x in histogram.keys()], histogram.values(), 10, edgecolor = (0,0,0))
# plt.axis([-5,105,0,5])

# plt.xticks([10*i for i in range(11)])
# plt.xlabel("Decile")
# plt.ylabel("# of Students")
# plt.title("Distribution of Exam Graeds")
# plt.show()

#Line chart - Showing variance, bias^2 and total error on a line chart

# variance = [1,2,4,8,16,32,64,128,256]
# bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
# total_error = [x+y for x,y in zip(variance,bias_squared)]
# xs = [i for i, _ in enumerate(variance)] #Can also do xs = [range(len(variance))]

# plt.plot(xs, variance, 'g-', label = 'Variance')
# plt.plot(xs, bias_squared, 'r--', label = 'Bias Square')
# plt.plot(xs, total_error, 'b:', label= 'Total Error')

# plt.xlabel("Model Complexity")
# plt.xticks([])
# plt.title("The bias-variance Tradeoff")
# plt.legend(loc = 9) #Can also set locations - Argument: loc = 9 (9 means "top center"), read document for more.
# plt.show()


#Scatter plot - Visualizing the relationship between two sets of data / variables

# friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
# minutes = [175, 170, 205, 120, 220, 130,105,145,190]
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


# plt.scatter(friends, minutes)


# for label, friend_count, time_count in zip (labels, friends, minutes):
#     plt.annotate(label,
#                  xy=(friend_count,time_count),
#                  xytext = (5, -5),
#                  textcoords = 'offset points')

# plt.title("Daily Minutes VS Number of Friends")
# plt.xlabel("# of Friends")
# plt.ylabel("Daily minutes spent")
# plt.show()