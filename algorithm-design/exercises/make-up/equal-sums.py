from typing import Tuple


def solve(numbers: list[int], memo: dict[int, list[int]]) -> Tuple[list[int], list[int]]:
    subsets_so_far = [[]]
    
    for number in numbers:
        new_subsets = []
        
        for subset in subsets_so_far:
            new_subset = subset + [number]
            
            if new_subset:
                sum = calculate_sum(new_subset)
                
                if sum in memo:
                    return (new_subset, memo[sum])
                
                memo[sum] = new_subset.copy()
                
            new_subsets.append(new_subset)
        
        subsets_so_far.extend(new_subsets)
    
    return None

def calculate_sum(numbers: list[int]) -> int:
    sum = 0

    for number in numbers:
        sum = number + sum

    return sum
        

test_cases = int(input())

for i in range(test_cases):
    numbers = input().split(" ")
    numbers_set = []


    for j in range(1, 21):
        numbers_set.append(int(numbers[j]))

    print(f"Case #{i + 1}:")
    
    result = solve(numbers_set, {})

    if result:
        subset1, subset2 = result
        print(" ".join(map(str, subset1)))
        print(" ".join(map(str, subset2)))
    else:
        print("Impossible")

