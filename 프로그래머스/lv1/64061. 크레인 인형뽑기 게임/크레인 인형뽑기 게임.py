def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(stack) < 2:
            continue
        else:
            if stack[-1] == stack[-2]:
                del stack[-2:]
                answer += 1     
                
    return answer * 2