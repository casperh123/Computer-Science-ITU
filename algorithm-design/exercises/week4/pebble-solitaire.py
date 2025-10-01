def get_moves(board: list[int], pebbles: list[int]):
    moves = []

    for i in range(len(pebbles)):
        pebble = pebbles[i]
        
        if pebble + 2 < len(board) and board[pebble + 2] == 0 and board[pebble + 1] == 1:
            moves.append((pebble, pebble + 2))
        if pebble - 2 > 0 and board[pebble - 2] == 0 and board[pebble - 1] == 1:
            moves.append((pebble, pebble - 2))

    return moves

def make_move(board: list[int], pebbles: list[int], move: tuple[int, int]):
    from_pos, to_pos = move
    middle_position = (from_pos + to_pos) // 2

    board[from_pos] = 0
    board[to_pos] = 1
    board[middle_position] = 0

    pebbles.remove(from_pos)
    pebbles.remove(middle_position)
    pebbles.append(to_pos)

def back_track(board: list[int], pebbles: list[int], move: tuple[int, int]):
    from_pos, to_pos = move
    middle_position = (from_pos + to_pos) // 2


    board[from_pos] = 1
    board[to_pos] = 0
    board[middle_position] = 1

    pebbles.append(from_pos)
    pebbles.append(middle_position)
    pebbles.remove(to_pos)


def solve(board: list[int], pebbles: list[int], memo: dict):
    moves = get_moves(board, pebbles)
    key = tuple(pebbles)

    if(key in memo):
        return memo[key]

    if(len(moves) == 0):
        return len(pebbles)
    else:
        best = 1000000000

        for i in range(len(moves)):
            move = moves[i]

            make_move(board, pebbles, move)

            pebbles_left = solve(board, pebbles, memo)

            if(pebbles_left < best):
                best = pebbles_left

            back_track(board, pebbles, move)

        memo[key] = best
        return best


games = int(input())

for i in range(games):
    string_pebbles = input()
    board = []
    pebbles = []

    for j in range(len(string_pebbles)):
        input_character = string_pebbles[j]

        if input_character == 'o':
            board.append(1)
            pebbles.append(j)
        else: 
            board.append(0)

    print(solve(board, pebbles, {}))
