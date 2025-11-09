import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hours = pd.read_csv('hour.csv')
hours_first24hours = hours.loc[0:24, :] 
hours_first48hours = hours.loc[0:48, :]
# print(hours.head())
# print(hours.tail())
# print(hours.describe()) #Summary Statistics


#Objective : Understanding different type of plots with interpretation, motives.






#1. Scatter plot -- Used to show the relationship between two variables over a Period of time. (Relationship/Correlation)



plt.scatter(hours_first24hours['instant'], hours_first24hours['count'], marker="+")
plt.title("Total Count by hour - First Day")
plt.ylabel("Total number of Riders")
plt.xlabel("Hour")
plt.show()

# Communicates the relation between total number of riders w.r.t nth Hour of the day.
# Interpretations: Simple decisions like surge charging, discounts can be made through this scatterplot. The numbers rise during the typical commute hours and are fairly low early Morning.

#2. Bar Chart -- Used to present a quantitative difference between a discrete set of items. (Aggregate)


# season_totals = hours.groupby('season')['count'].sum()
# print(season_totals)

# plt.bar(season_totals.index, season_totals.values)
# plt.xlabel("Seasons")
# plt.ylabel("Total No. of Riders")
# plt.xticks([1,2,3,4], ['Winter', 'Spring', 'Summer', 'Fall'])
# plt.ticklabel_format(style='plain', axis='y') 
# plt.show()

# A bar chart very explicitly presents a total aggregate classified by Seasons. It simply ties the visualizaion in a immediate, human-readable way.->Cont.
# Through that one can guide further analysis - whether its addressing the low demand or maintaining high-performance.



#3. Box plot -- Used to show the over all distribution / behaviour. (Used seaborn for syntactical comfort with boxplot) [Distribution]
#SEASON(s) --> 1 for winter, 2 for spring, 3 for summer, 4 for fall !


# sns.boxplot(x='season', y='count', data=hours)
# plt.xlabel('Seasons')
# plt.ylabel('Rider Count')
# plt.title('Total Rider count by Seasons - over Two Years')
# plt.show()

# The top horizontal line is the Maximum Value, whereas the bototm line is the Minimum Value, the centre line within the rectangle is the Median value.
# The distance from median to max value is the upper Quartile, distance from median to minimum value is the lower Quartile.
# Interpretations : Since, The number of riders in season 1 are comparatively low, A company can sell off a few bikes during that season to have more cash in hand-> Cont.
# Figure out which location has the most number of bikes during winters and solely focus on that, We can also go into the detail of Maximum value of Season '3' -> Cont.
# and figure out ways to multiply business during that time even further.


#4. Line Chart -- Used to show a trend (over a period of time)
# plt.plot(hours_first48hours['instant'], hours_first48hours['count'])
# plt.xlabel("Hour")
# plt.ylabel("Total No. of Riders")
# plt.title("Rider Count by Hour - for Two Days")
# plt.xticks(range(0,49))
# plt.show()

# Interpretation: with the help of Line Graphs, We can easily understand a trend. The graph for these two days show, the peak hours for our riders. ->Cont
# We can also plot two lines, like one for registered users and one for casual and follow the trends to understand data better.