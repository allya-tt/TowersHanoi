def towers(n, a, b, c):
    if n == 1:
        printing(a, b)
    else:
        towers(n-1, a, c, b)
        print("Move ring ", n, ' from ', a, ' rod to ', c, ' rod.', sep='')
        towers(n - 1, c, b, a)
    return ''


n = int(input('Enter the number of the rings: '))   # the number of rings
a = int(input('Number of the rod, from which is needed to move: '))   # starting rod
b = int(input('Number of the rod, to where its needed to replace: '))   # finish rod
c = 6-a-b
towers(n, a, b, c)
