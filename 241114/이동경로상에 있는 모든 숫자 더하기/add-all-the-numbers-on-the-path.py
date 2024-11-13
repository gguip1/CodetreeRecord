N, T = map(int, input().split())

command = input().split()

map_ = []

for i in range(N):
    map_.append(list(map(int, input().split())))

dir_ = 'N'
position = [int(round((N - 1)/2)), int(round((N - 1)/2))]

score = map_[position[1]][position[0]]

def dir_controllerL(dir_):
    if dir_ == 'N':
        return 'W'
    elif dir_ == 'W':
        return 'S'
    elif dir_ == 'S':
        return 'E'
    elif dir_ == 'E':
        return 'N'

def dir_controllerR(dir_):
    if dir_ == 'N':
        return 'E'
    elif dir_ == 'E':
        return 'S'
    elif dir_ == 'S':
        return 'W'
    elif dir_ == 'W':
        return 'N'

def position_controller(position_, dir_, score_):
    if dir_ == 'N' and position_[1] > 0:
        position_[1] -= 1
        score_ += map_[position_[1]][position_[0]]
    elif dir_ == 'S' and position_[1] < N - 1:
        position_[1] += 1
        score_ += map_[position_[1]][position_[0]]
    elif dir_ == 'W' and position_[0] > 0:
        position_[0] -= 1
        score_ += map_[position_[1]][position_[0]]
    elif dir_ == 'E' and position_[0] < N - 1:
        position_[0] += 1
        score_ += map_[position_[1]][position_[0]]
    
    return position_, score_

for i in range(T):
    if command[0][i] == 'L':
        dir_ = dir_controllerL(dir_)
    elif command[0][i] == 'R':
        dir_ = dir_controllerR(dir_)
    elif command[0][i] == 'F':
        position, score = position_controller(position, dir_, score)

print(score)
