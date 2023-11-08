mario = {}
mario_file = \
    open("mario.csv")
records = mario_file.readlines()
for record in records:
    print(record.split(',', 1)[0])
    record = record.strip()
    fields = record.split(",")
    mario[fields[0].lower()] = fields[3]

while True:
    game = input("game 1: ").lower()
    if game not in mario:
        continue
    break

while True:
    game2 = input("game 2: ").lower()
    if game2 not in mario:
        continue
    break
score = float(mario[game][:3])*10
score2 = float(mario[game2][:3])*10
if score > score2:
    print(f'{game} is {round(score / score2,3)} times better than {game2}')
else:
    print(f'{game2} is {round(score2 / score,3)} times better than {game}')
