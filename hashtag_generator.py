def generate_hastag(s):
    hashtag = "#" + "".join([x.strip(" ").title() for x in s.split()])
    if len(hashtag) > 140 or s == "":
        return "false"
    else: return hashtag
    


x = "    Hello     World   "
print(generate_hastag(x))