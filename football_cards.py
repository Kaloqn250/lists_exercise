team_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
cards = input().split()

game_terminated = False

for card in cards:
    if card in team_A:
        team_A.remove(card)
    elif card in team_B:
        team_B.remove(card)

    if len(team_A) < 7 or len(team_B) < 7:
        game_terminated = True
        break
if game_terminated:
    print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')
    print('Game was terminated')
else:
    print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')