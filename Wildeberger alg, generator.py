def sol(D):
    import numpy as np
    R = np.array([[1, 1], [0, 1]])
    L = np.array([[1, 0], [1, 1]])

    try:  # checks for perfect squareds
        d = D ** .5
        if (int(d) == d):
            raise Exception()
    except:
        print("!")
        exit()

    Q = np.array([[1, 0], [0, -D]])

    T = lambda x: sum(sum(x))  # the sum of all elements

    Right = lambda x: L @ x @ R  # the steps(matrix multiplicaion
    Left = lambda x: R @ x @ L

    A = Right(Q) if T(Q) < 0 else Left(Q) if T(Q) > 0 else np.array([[]])  # first step

    I = np.eye(2, 2) @ R if T(Q) < 0 else np.eye(2, 2) @ L if T(Q) > 0 else np.eye(2, 2)

    while not np.equal(A, Q).all():  # don't us <bla> == True , it is assumed
        # print(I)
        if T(A) < 0:  # right
            A = Right(A)
            I = I @ R
        elif T(A) > 0:  # left
            A = Left(A)
            I = I @ L

    [x, y] = I[:, 0]
    x = int(x)
    y = int(y)
    #print(f" x= {x} \n y={y}")
    #print(f"{x}^2 - {D}*{y}^2 = {(x ** 2) + (-D) * (y ** 2)}")
    return  [x,y]

print(sol(6))

Sol_x = []
Sol_y = []
