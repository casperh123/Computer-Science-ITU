def solve(remaining_price: int, money: list[int], index: int, memo):
     
     key = (remaining_price, index)

     if key in memo:
         return memo[key]

     if(remaining_price <= 0):
         result = (abs(remaining_price), 0)
         memo[key] = result
         return result

     if(index >= len(money)):
         result = (1000000, 0)
         memo[key] = result
         return result

     use_coin = solve(remaining_price - money[index], money, index + 1, memo)
     use_coin_result = (use_coin[0], use_coin[1] + 1)
     
     skip_coin = solve(remaining_price, money, index + 1, memo)

     if (use_coin_result[0] < skip_coin[0] or 
        (use_coin_result[0] == skip_coin[0] and use_coin_result[1] < skip_coin[1])):
        best_result = use_coin_result
     else:
        best_result = skip_coin
                  
     memo[key] = best_result
     return best_result







cases = int(input())

for i in range(cases):
    price = int(input())
    bills_coins_amount = int(input())

    money = dict();

    for j in range(bills_coins_amount):
        bill_or_coin = int(input())


        current = money.get(bill_or_coin, 0)

        money[bill_or_coin] = current + 1

        money_list = [denom for denom, count in money.items() for _ in range(count)]

    result = solve(price, money_list, 0, {})
    print(price + result[0], result[1])