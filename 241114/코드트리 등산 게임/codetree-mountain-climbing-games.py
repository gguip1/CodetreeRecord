Q = int(input())

command = []

mountains = []

for i in range(Q):
    command.append(list(map(int, input().split())))

# for index, value in enumerate(command):
#     if value[0] == 100:
#         mountains.append(value[1:])
#     elif value[0] == 200:
#         mountains[0].append(value[1])
#     elif value[0] == 300:
#         mountains[0].pop()
#     elif value[0] == 400:

#         position = 0
#         score = 0
#         max_ = 0

        # for i, v in enumerate(mountains[0]):
        #     if position == value[1]:

                # v_c_t = 0
                # v_index = 0

                # for j in range(0, len(mountains[0])):
                #     v_c = 0
                #     for i_, v_ in enumerate(mountains[0][j:]):
                #         if mountains[0][j] < v_:
                #             v_c += 1

                #     if v_c_t < v_c:
                #         v_c_t = v_c
                #         v_index = j
                
#                 position = v_index
#                 max_ = mountains[0][position]
#                 score += 1000000
#                 break
#             else:
#                 if max_ < v:
#                     max_ = v
#                     score += 1000000
#                 position += 1

#         print(score)

        # for i, v in enumerate(mountains[0][position:]):
        #     if max_ < v:
        #         max_ = v
        #         score += 1000000
        #     position += 1

#         score += max_

#         print(mountains)
#         print(score)

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

            if position == value[1]:
                score += 1000000

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

                max_ = mountains[0][position]

                break
            
            if position == len(mountains[0]) - 1:
                break

            if position == 0:
                score += 1000000

                max_ = mountains[0][position]

            if max_ < mountains[0][position + 1]: 

                # print(f'before : score[{score}] max_[{max_}] position[{position}]')

                score += 1000000

                max_ = mountains[0][position + 1]
                
                # print(f'after : score[{score}] max_[{max_}] position[{position}]')
            
            position += 1

        # print(score)

        for i, v in enumerate(mountains[0][position:]):

            if position == len(mountains[0]) - 1:
                break

            if max_ < mountains[0][position + 1]:

                # if len(mountains[0]) == 11:
                #     print(f'before : score[{score}] max_[{max_}] position[{position}]')

                score += 1000000

                max_ = mountains[0][position + 1]

            # if len(mountains[0]) == 11:
            #     print(f'after : score[{score}] max_[{max_}] position[{position}]')
            
            position += 1

        score += max_

        # print(mountains)
        print(score)

