filename = "uzdevumatexts2.txt"

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        linija = line.split()
        
        if len(linija) >= 4:
            print(linija[3])