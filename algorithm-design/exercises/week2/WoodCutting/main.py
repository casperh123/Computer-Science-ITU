test_cases = int(input())

for i in range(test_cases):
    customers = int(input())
    wait_time = 0
    wood_pieces = []

    for j in range(customers):
        input_numbers = [int(x) for x in input().split(" ")]
        wood_pieces.append(sum(input_numbers[1:]))

    wood_pieces.sort()

    customer_time = 0
    total_time = 0

    for length in wood_pieces:
        customer_time += length
        total_time += customer_time

    print(total_time / customers)