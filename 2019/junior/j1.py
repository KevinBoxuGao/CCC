team_one = []
team_two = []
for i in range(3,0,-1):
    team_one.append(int(input())*i)
for i in range(3,0,-1):
    team_two.append(int(input())*i)

if sum(team_one) > sum(team_two):
    print("A")
elif sum(team_one) == sum(team_two):
    print("T")
else:
    print("B")