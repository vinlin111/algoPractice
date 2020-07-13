def camel_case(string):
    return "".join(x.title() for x in string.split(" "))

print(camel_case("test case"))