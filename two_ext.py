import numpy as np
import main as m
from translator import trans_ext , trans_num_ext
#mod 61
E = np.array([[4,1],[1,3]])

def Enc_ext(x, matr = E):
    """
    encodes a message according to a given 2x2 matrix(block cypher)-- has to be invertable in Z/61Z.
    :param x: input string, text to encode no numbers
    :param matr: the block cypher matrix
    :return: output string, encoded message.
    """
    try:  # invertibility of E
        gcd = m.Bezout((matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0])%61,61)[0]
        if not (int(gcd) == 1):
            raise Exception()
    except:
        print("! not invertable")
        exit()
    if len(x)%2 ==1:
        x = x + " "
    x = np.transpose(np.array(trans_ext(x)))
    enc = np.transpose((matr @ x)%61)
    return trans_num_ext(enc)


def Dec_ext(y,matr = E):
    """
    Decodes an encoded message
    :param y: input string, encoded messge
    :param matr: matrix used for encoding
    :return: output string, decoded message
    """
    y = np.transpose(np.array(trans_ext(y)))
    D = np.array([[matr[1][1], -matr[0][1]], [-matr[1][0], matr[0][0]]])
    k_inv = m.Bezout((matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0])%61,61)[1]
    dec = np.transpose(((k_inv*D)@y)%61)
    return trans_num_ext(dec)

#print(Enc_ext("Hello There",matr = [[4,-1],[1,1]]))
#print(Dec_ext(Enc_ext("Hello There",matr = [[4,-1],[1,1]]),matr = [[4,-1],[1,1]]))

