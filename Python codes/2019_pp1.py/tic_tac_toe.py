# Matrix=[
#         ["_","_","_"],
#         ["_","_","_"],
#         ["_","_","_"]
#         ]
# Player_code=["X","O"]
# Players=["Player_1","Player_2"]
# run=True
# while run:
#     for player in Player_code:
#         if run==True:
#             Play=int(input())
#             position=(Play-1)%3
#             row_num=(Play-1)//3
#             Matrix[row_num][position]=player
#             for row in Matrix:
#                 print(*row)
#             for k in range(2):
#                 for i in range(3):
#                     for j in range(3):
#                         if Matrix[i][j]==Player_code[k]:
#                             continue
#                         else:
#                             break
#                     else:
#                         winner=Players[k]
#                         run=False
#                 for i in range(3):
#                     if Matrix[i][i]==Player_code[k]:
#                         continue
#                     else:
#                         break
#                 else:
#                     winner=Players[k]
#                     run=False

#                 for i in range(3):
#                     if Matrix[i][2-i]==Player_code[k]:
#                         continue
#                     else:
#                         break
#                 else:
#                     winner=Players[k]
#                     run=False

#                 for i in range(3):
#                     for j in range(3):
#                         if Matrix[j][i]==Player_code[k]:
#                             continue
#                         else:
#                             break
#                     else:
#                         winner=Players[k]
#                         run=False

# print(winner,"wins")



Matrix=[
        ["_","_","_"],
        ["_","_","_"],
        ["_","_","_"]
        ]
Player_code=["X","O"]
Players=["Player_1","Player_2"]
run=True
while run:
    for player in Player_code:
        if run:
            Play=int(input())
            position=(Play-1)%3
            row_num=(Play-1)//3
            if Matrix[row_num][position] != "_":
                print("Invalid move")
                continue
            Matrix[row_num][position]=player
            for row in Matrix:
                print(*row)      
            for i in range(3):
                if all(Matrix[i][j]==player for j in range(3)):
                    winner=Players[Player_code.index(player)]
                    run=False
            for i in range(3):
                if all(Matrix[j][i]==player for j in range(3)):
                    winner=Players[Player_code.index(player)]
                    run=False
            if all(Matrix[i][i]==player  for i in range(3)):
                    winner=Players[Player_code.index(player)]
                    run=False
            if all(Matrix[i][2-i]==player  for i in range(3)):
                    winner=Players[Player_code.index(player)]
                    run=False
print(winner,"wins")
