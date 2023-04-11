# https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    player_to_index = {val:idx  for idx,val in enumerate(players)}
    index_to_player = {idx:val for idx,val in enumerate(players)}

    for player1 in callings:
        index1 = player_to_index[player1]
        index2 = index1 - 1
        player2 = index_to_player[index2]
        
        player_to_index[player1] -= 1
        player_to_index[player2] += 1
        index_to_player[index1] = player2
        index_to_player[index2] = player1
    
    return [i[0] for i in sorted(player_to_index.items(), key=lambda x: x[1])]

a = ["mumu", "soe", "poe", "kai", "mine"]
b = ["kai", "kai", "mine", "mine"]
solution(a, b)