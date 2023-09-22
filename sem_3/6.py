
#x = [5 4 5 6]
y = [6 7 8 9]
def least_squares(xdata, ydata):
     a = (sum([x * y for x, y in zip(xdata, ydata)]) - mean(ydata) * sum(xdata)) / (sum([x**2 for x in xdata]) - mean(xdata) * sum(xdata))
     b = mean(ydata) - a * mean(xdata)
     return a, b

print(least_squares(x,y))
