import math
from collections import deque

moves = [
    ( 2,  1),
    ( 2, -1),
    (-2,  1),
    (-2, -1),
    ( 1,  2),
    ( 1, -2),
    (-1,  2),
    (-1, -2),
]

def in_range(n):
    return True if n <=7 and n >= 0 else False

def valid_moves(cell):
    validmoves = []
    for val in moves:
        posx = cell[0] + val[0]
        posy = cell[1] + val[1]
        if in_range(posx) and in_range(posy):
            validmoves.append(val)
    return validmoves

def translate(n, y = None):
    if y == None:
        x = n/8
        y = (n % 8)
        return (x, y)
    return (n*8) + y

def distance(start, end):
    return (start[0] - end[0]) + (start[1] - end[1])

def make_move(pos, move):
    return (pos[0] + move[0], pos[1] + move[1])

def knights_shortest_path(start, end):
    start = translate(start)
    end = translate(end)
    print 'Start: ' + str(start), 'End: ' + str(end)
    been = [start]
    que = deque([{'pos': start, 'count': 0, 'parent': False}])
    while len(que) != 0:
        out = que.popleft()
        current = out['pos']
        count = out['count']
        if current == end:
            print current, count
            moves = deque()
            while out['parent'] != False:
                moves.appendleft(out['pos'])
                out = out['parent']
            moves.appendleft(out['pos'])
            print moves
            return count
        for move in valid_moves(current):
            newpos = make_move(current, move)
            if newpos not in been:
                been.append(newpos)
                que.append({'pos': newpos, 'parent': out, 'count': count + 1})

knights_shortest_path(20,21)
knights_shortest_path(20,50)
knights_shortest_path(1,62)
knights_shortest_path(17,35)
knights_shortest_path(0,10)
