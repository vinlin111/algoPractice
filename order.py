def order(sentence):
    if sentence == "":
        return ""

    else:
        s = sentence.split(" ")
        new = []

        for i in range(len(s)):
            find_int = str(i+1)
            for j in range(len(s)):
                if find_int in s[j]:
                    new.append(s[j])
                else: continue
        return " ".join(new)

print(order("is2 Thi1s T4est 3a"))