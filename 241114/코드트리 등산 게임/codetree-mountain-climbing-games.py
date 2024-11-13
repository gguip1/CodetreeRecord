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

        for i, v in enumerate(mountains[0]):
            if position == value[1] - 1:
                # position = 2

                v_c_t = 0
                v_index = 0

                for j in range(0, len(mountains[0])):
                    v_c = 0
                    for i_, v_ in enumerate(mountains[0][j:]):
                        if mountains[0][j] < v_:
                            v_c += 1
                    
                    if v_c_t < v_c:
                        v_c_t = v_c
                        v_index = j
                
                position = v_index
                # print('position', position)
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
                # print(score)
            position += 1

        score += max_

        # print('mountains', mountains)
        print(score)
