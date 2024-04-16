#贪心算法
number = 3
days = 3
hold = [4,5,6]
price = [[1, 2, 3], [4, 3, 2], [1, 5, 3]]

m = len(price)
n = len(price[0])
total_profit = 0
for index in range(m):
    for day in range(n-1):
        if price[index][day+1] > price[index][day]:
            total_profit += hold[index]*(price[index][day+1]-price[index][day])
print(total_profit)
