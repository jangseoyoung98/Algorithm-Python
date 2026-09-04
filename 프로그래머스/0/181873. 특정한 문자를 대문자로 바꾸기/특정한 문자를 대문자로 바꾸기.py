def solution(my_string, alp):
    new_string = ""
    for l in my_string:
        if l == alp:
            new_string += alp.upper()
            continue
        new_string += l
    return new_string