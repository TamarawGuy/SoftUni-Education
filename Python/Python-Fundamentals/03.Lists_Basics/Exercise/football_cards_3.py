A = [1,2,3,4,5,6,7,8,9,10,11]
B = [1,2,3,4,5,6,7,8,9,10,11]

line = input().split(" ")
for item in line:
    tokens = item.split("-")
    team = tokens[0]
    player = int(tokens[1])
    if team == 'A':
        if player in A:
            A.remove(player)
            if len(A) < 7:
                print(f"Team A - {len(A)}; Team B - {len(B)}")
                print("Game was terminated")
                break
            else:
                continue

    elif team == 'B':
        if player in B:
            B.remove(player)
            if len(B) < 7:
                print(f"Team A - {len(A)}; Team B - {len(B)}")
                print("Game was terminated")
                break
            else:
                continue
        
if len(A) >=7 and len(B) >= 7:
    print(f"Team A - {len(A)}; Team B - {len(B)}")