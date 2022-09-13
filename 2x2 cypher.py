import numpy as np
import main as m
from translator import trans , trans_num
#mod 26
E = np.array([[4,1],[1,3]])

def Enc(x, matr = E):
    """
    encodes a message according to a given 2x2 matrix(block cypher)-- has to be invertable in Z/26Z.
    :param x: input string, text to encode no numbers
    :param matr: the block cypher matrix
    :return: output string, encoded message.
    """
    try:  # invertibility of E
        gcd = m.Bezout((matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0])%26,26)[0]
        if not (int(gcd) == 1):
            raise Exception()
    except:
        print("! not invertable")
        exit()
    if len(x)%2 ==1:
        x = x + "ZZZ"
    x = np.transpose(np.array(trans(x)))
    enc = np.transpose((matr @ x)%26)
    return trans_num(enc)


def Dec(y,matr = E):
    """
    Decodes an encoded message
    :param y: input string, encoded messge
    :param matr: matrix used for encoding
    :return: output string, decoded message
    """
    y = np.transpose(np.array(trans(y)))
    D = np.array([[matr[1][1], -matr[0][1]], [-matr[1][0], matr[0][0]]])
    k_inv = m.Bezout((matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0])%26,26)[1]
    dec = np.transpose(((k_inv*D)@y)%26)
    return trans_num(dec)

print(Enc("MATH",matr = [[4,-1],[1,1]]))
print(Dec("YNTB",matr = [[4,-1],[1,1]]))

