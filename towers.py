def Towers(n, a, b, c):
    if n==1:
        print("Move ring ", n, ' from ', a, ' rod to ', b, ' rod.', sep='')
    else:
        Towers(n-1, a, c, b)
        print("Move ring ", n, ' from ', a, ' rod to ', c, ' rod.', sep='')
        Towers(n - 1, c, b, a)
    return ''
def printing(a, b):
    print("Move ring ", n, ' from ', a, ' rod to ', b, ' rod.', sep='')
# Driver code
n = int(input('Enter the number of the rings: ')) #the number of rings
a=int(input('Number of the rod, from which is needed to move: ')) #starting rod
b=int(input('Number of the rod, to where its needed to replace: ')) #finish rod
c=6-a-b
Towers(n, a, b, c)
