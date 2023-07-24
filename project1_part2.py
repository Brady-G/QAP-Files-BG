import matplotlib.pyplot as plot

MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
]

Sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for Index in range(12):
    Month = MONTHS[Index]
    while True:
        AmountOfSales = input(f"Enter the sales for {Month} or 0 if the month has not passed: ")
        try:
            AmountOfSales = int(AmountOfSales)
            break
        except:
            print("Sales entered was not a number try again.")
    Sales[Index] = AmountOfSales

plot.plot(MONTHS, Sales)

plot.xlabel('Months')
plot.ylabel('Sales')
plot.title('Monthly Sales')
plot.grid(True)
plot.show()
