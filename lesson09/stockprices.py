# Python


stock_prices = []
with open('stockprices.txt', 'rt') as file_handle:
    for line in file_handle:
        line = line.strip()
        # print(line)
        stock_prices.append(line)


# for price in stock_prices:
#     print(price)

with open('stockprices.rev.txt', 'wt') as file_handle:
    for index in range(len(stock_prices)-1, -1, -1):
        file_handle.write(stock_prices[index])
        file_handle.write('\n')
