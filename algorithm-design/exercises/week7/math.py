
from typing import Dict, List, Set, Tuple

def solve():
    assignment: Dict[int, int] = {}
    result_to_pair: Dict[int, int] = {}

    for pair_index in range(len(pairs)):
        visited = set()
        if not augment(pair_index, assignment, result_to_pair, visited):
            print("impossible")
            return
        
    operands = ["+", "-", "*"]

    for i in range(len(pairs)):
        a, b = pairs[i]
        operand_index = assignment[i]
        result = get_result(a, b, operand_index)

        print(f"{a} {operands[operand_index]} {b} = {result}")



def augment(pair_index: int, assignment: Dict[int, int], result_to_pair: Dict[int, int], visited: Set[int]):
    if pair_index in visited:
        return False
    
    visited.add(pair_index)

    for operand_index in range(3):
        a, b = pairs[pair_index]
        result = get_result(a, b, operand_index)

        if result not in result_to_pair:
            assignment[pair_index] = operand_index
            result_to_pair[result] = pair_index
            visited.remove(pair_index)
            return True
        
        conflicting_pair_index = result_to_pair.get(result)

        if augment(conflicting_pair_index, assignment, result_to_pair, visited):

            if pair_index in assignment:
                old_result = get_result(a, b, assignment[pair_index])
                if old_result in result_to_pair:
                    del result_to_pair[old_result]

            assignment[pair_index] = operand_index
            result_to_pair[result] = pair_index
            visited.remove(pair_index)
            return True

    visited.remove(pair_index)
    return False


def get_result(a: int, b: int, operand_index: int):
    if operand_index == 0: return a + b
    if operand_index == 1: return a - b
    if operand_index == 2: return a * b


pair_count = int(input())

PLUS = 0
MINUS = 1
MULTIPLICATION = 2

pairs: List[Tuple[int, int]] = []

for i in range(pair_count):
    string_pair = input().split(" ")
    pair = (int(string_pair[0]), int(string_pair[1]))

    pairs.append(pair)

solve()