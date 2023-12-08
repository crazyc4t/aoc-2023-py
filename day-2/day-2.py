def read_file(file: str) -> list:
    lines = []
    fread = open(file, "r")
    while True:
        text = fread.readline()
        if len(text) == 0:
            break
        else:
            x = text.split("; ")
            y = []
            for i in x:
                y.append(i.strip())
            z = y[0].split(": ")
            del y[0]
            w = z + y
            lines.append(w)
    fread.close()
    return split_sets(lines)


def split_sets(matrix: list) -> list:
    r = []
    for i in range(len(matrix)):
        x = [matrix[i][0]]
        for j in range(1, len(matrix[i]), 1):
            y = matrix[i][j]
            z = y.split(", ")
            for k in z:
                x.append(k)
        r.append(x)
    return r


def split_colors(matrix: list) -> dict:
    colors = ["red", "green", "blue"]
    d = {}
    for i in range(len(matrix)):
        r = []
        g = []
        b = []
        t = matrix[i][0]
        init = int(t.replace("Game ", ""))
        for j in range(1, len(matrix[i]), 1):
            t = matrix[i][j]
            for k in colors:
                if t.find(k) != -1:
                    if k == "red":
                        r.append(int(t.replace(" red", "")))
                    if k == "green":
                        g.append(int(t.replace(" green", "")))
                    if k == "blue":
                        b.append(int(t.replace(" blue", "")))
        d[init] = {"red": r, "green": g, "blue": b}
    return d


def sum_id(keys: list, games: dict) -> int:
    checked_bags = 0
    for i in keys:
        game_passed = True
        r = games.get(i).get("red")
        g = games.get(i).get("green")
        b = games.get(i).get("blue")
        print(f"The game {i} has: {r} red cubes, {g} green cubes, {b} blue cubes")
        for j in r:
            if j > 12:
                game_passed = False
        for j in g:
            if j > 13:
                game_passed = False
        for j in b:
            if j > 14:
                game_passed = False
        if game_passed:
            print(f"The game {i} is accepted")
            checked_bags += i

    return checked_bags


def list_max(l: list) -> int:
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max


def sum_powers(keys: list, games: dict) -> int:
    powers_sum = 0
    for i in keys:
        colors = []
        r = games.get(i).get("red")
        g = games.get(i).get("green")
        b = games.get(i).get("blue")
        print(f"The game {i} has: {r} red cubes, {g} green cubes, {b} blue cubes")
        colors.append(list_max(r))
        colors.append(list_max(g))
        colors.append(list_max(b))
        powers_sum += colors[0] * colors[1] * colors[2]
    return powers_sum


lines = read_file("input.txt")
games = split_colors(lines)
games_keys = list(games.keys())
print(f"The total sum of the powers is: {sum_powers(games_keys, games)}")
