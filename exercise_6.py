# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    first = ord('a')
    c = first
    for i in range(height):
        if i!=0 and i%2!=0:
            L=[]
            for j in range(width):
                L.append(chr(c))
                c= (c-first+1)%26+first

                

            for k in L[::-1]:
                print(k,end='')
        else:
            for q in range(width):
                print(chr(c),end='')
                c=(c-first+1)%26+first
                
        print()



    # REPLACE THE PREVIOUS LINE WITH YOUR CODE


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    rectangle(17, 4)