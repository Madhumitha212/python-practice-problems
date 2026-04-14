def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    temp = s1 + s1
    return s2 in temp

print(is_rotation("abcd", "cdab"))