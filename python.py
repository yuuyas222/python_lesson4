
player_1 = "戦士"
player_2 = "魔法使い"

print(player_1)
print(player_2)

team = ["勇者", "魔法使い", 100, player_1]
print(team)

print(team[0])
num = 1 
print(team[num + 1])
print(len(team))

team = ["勇者","魔法使い"]

print(team)
print(team[0])
print(len(team))

team.append("戦士")
print(team)

team[2] = "ドラゴン"
print(team)

team.pop(2)
print(team)

team = ["勇者","戦士","魔法使い","盗賊"]
# print(team)
# print(team[0])
print("<select name='job'>")
for job in team:
    print("<option>" + job + "</option>")
print("</select>")

line = input().rstrip().split(",")
print(line)
print(len(line))

for enemy in line:
    print(enemy + "が現れた！")