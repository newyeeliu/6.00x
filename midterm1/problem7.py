def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    a = 0
    b = 0
    c = 0

    while 6*a + 9*b + 20*c < n:
        while 6*a + 9*b + 20*c < n:
            while 6*a + 9*b + 20*c < n:
                c += 1
            if 6*a + 9*b + 20*c == n:
                print a, b, c
                return True
            c = 0
            b += 1
        if 6*a + 9*b + 20*c == n:
            print a, b, c
            return True
        b = 0
        a += 1


    return False


print McNuggets(15)
print McNuggets(16)
print McNuggets(115)
print McNuggets(145)
print McNuggets(69)
print McNuggets(3)
print McNuggets(34534543324234)