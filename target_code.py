with open("exe.txt", "r") as f1, open("exe1.txt", "w") as f2:
    s = []
    for data in f1.read().split():
        s.append({"data": data, "temp": ""})

    i = 0
    len_s = len(s)
    while i < len_s:
        if s[i]["data"] == "=":
            if i+1<len(s):
                f2.write("\nLDA\t" + s[i+1]["data"])
            if i+2<len(s):
                if s[i+2]["data"] == "+":
                    if i+3<len(s):
                        f2.write("\nADD\t" + s[i+3]["data"])
                if s[i+2]["data"] == "-":
                    if i+3<len(s):
                        f2.write("\nSUB\t" + s[i+3]["data"])
            f2.write("\nSTA\t" + s[i-1]["data"])
        i += 1
