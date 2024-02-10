def is_palin(s):
    s=s.replace(" ", "").lower()
    return s==s[::-1]