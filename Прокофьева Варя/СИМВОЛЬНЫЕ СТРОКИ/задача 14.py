count = 0
def TumbaWords (A, w, L):
    global count
    if len (w) == L:
        print ( w )
        count += 1
        return
    for c in A:
        TumbaWords (A, w+c, L)
print(TumbaWords("ЫШЧО", "", 3))
print( count )

