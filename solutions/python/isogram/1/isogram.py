def is_isogram(s):
    found = set()
    for c in s:
        if c == ' ' or c == '-': continue
        c = c.lower()
        if c in found: return False
        found.add(c)
    return True
            
