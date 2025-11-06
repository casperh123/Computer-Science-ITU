import math

# The idea of using the negative logarithm of take/give comes from Claude.
def weight(give, take):
    return -math.log(take/give)

def bellman_to_the_ford(currencies, exchanges):
    distance = [0] * len(currencies)

    for _ in range(len(currencies) - 1):
        for from_currency, to_currency, give, take in exchanges:
            w = weight(give, take)
            path_cost = distance[from_currency] + w
            
            if path_cost < distance[to_currency]:
                distance[to_currency] =  path_cost


    for from_currency, to_currency, give, take in exchanges:
        if distance[from_currency] + weight(give, take) < distance[to_currency]:
            return "Arbitrage"

    return "Ok"


while True:

    C = int(input())

    if C == 0: 
        break

    currencies = [currency for currency in input().split(" ")]

    exchange_rates_amount = int(input())
    exchange_rates = []

    for rate in range(exchange_rates_amount):
        exchange_rate_string = input().split(" ")
        values = exchange_rate_string[2].split(":")
        from_currency = currencies.index(exchange_rate_string[0])
        to_currency = currencies.index(exchange_rate_string[1])

        give = int(values[0])
        take = int(values[1])

        exchange_rates.append((from_currency, to_currency, give, take))

    print(bellman_to_the_ford(currencies, exchange_rates))
