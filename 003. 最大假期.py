input: 
a. 有n个城市， 每个城市之间有飞行时间， 
b. 给个飞行时间， 
c. 给个vacation array, 代表每个城市每周的假期。 
d. 从第一个城市开始 意思就是每个周你可以呆在一个城市， 然后享受那个城市的假期。 
还有个限制， 就是城市与城市之间的飞行时间不能超过给定的飞行时间 
output: 求x weeks 你能享受到的最大假期总和 你自己设计输入的数据结构 

如图所示， 最大的应该 week1, A, sum=2; week2, B/C, sum=sum+1; week3, 回到A, sum+=3 total sum =6 

Vacation: Given a matrix of holiday where row is city, column is week, value is holiday number, 
Flights: a matrix represent whether row city can reach column city on time. 
Calculate the maximum number of holiday over the weeks.

