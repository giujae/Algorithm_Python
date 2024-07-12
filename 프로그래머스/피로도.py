from itertools import permutations

def solution(k, dungeons):
    possible = []
    ways = permutations(dungeons)
    for way in ways:
        cnt = 0
        energy = k
        for dungeon in way:
            if energy >= dungeon[0]:
                energy -= dungeon[1]
                cnt += 1
        possible.append(cnt)
    return max(possible)

print(solution(80, [[80,20],[50,40],[30,10]]))