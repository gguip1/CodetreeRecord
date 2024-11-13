Q = int(input())

command = []

mountains = []

for i in range(Q):
    command.append(list(map(int, input().split())))

for index, value in enumerate(command):
    if value[0] == 100:
        mountains.append(value[1:])
    elif value[0] == 200:
        mountains[0].append(value[1])
    elif value[0] == 300:
        mountains[0].pop()
    elif value[0] == 400:

        position = 0
        score = 0
        max_ = 0

        min_ = 1000001
        min_index = 0

        for i, v in enumerate(mountains[0]):
            if min_ > v:
                min_ = v
                min_index = i

        for i, v in enumerate(mountains[0]):

            if position == value[1] - 1:
                position = min_index
                max_ = mountains[0][position]
                score += 1000000
                break
            else:
                if max_ < v:
                    max_ = v
                    score += 1000000
                    position += 1
        
        for i, v in enumerate(mountains[0][position:]):
            if max_ < v:
                    max_ = v
                    score += 1000000
                    position += 1

        score += max_

        print(score)
