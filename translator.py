"""translator from  letters to integers"""

alphabet = ("A","B","C","D","E",
            "F","G","H","I","J",
            "K","L","M","N","O",
            "P","Q","R","S","T",
            "U","V","W","X","Y","Z")

def divide_chunks(l, n=2):
    """
    by GeeksForGeeks
    use list(function to get  matrix)
    """
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


def trans(str):
    ls = []
    str = (str.upper()).replace(" ","")
    for i in str:
        ls.append((alphabet.index(i)) + 1)
    return list(divide_chunks(ls))

def trans_num(ls):
    inc = [j for i in ls for j in i] # divides everything into elements
    for i in range(len(inc)):
        inc[i] = alphabet[inc[i] - 1]
    return "".join(inc)   # joins all the elements together
"""
Extended alphatet
"""
alphabet_ext = ("A","a","B","b","C","c","D","d","E","e",    # extended alphabet
                "F","f","G","g","H","h","I","i","J","j",    # this has 61 characters, 61 is a prime thus there are
                "K","k","L","l","M","m","N","n","O","o",    # more matrecies that are invertable in Z/61Z
                "P","p","Q","q","R","r","S","s","T","t",
                "U","u","V","v","W","w","X","x","Y","y",
                "Z","z"," ",",",".","!","-","_",":",";",
                "?")

def trans_ext(str):
    ls = []
    for i in str:
        ls.append((alphabet_ext.index(i)) + 1)
    return list(divide_chunks(ls))

def trans_num_ext(ls):
    inc = [j for i in ls for j in i]
    for i in range(len(inc)):
        inc[i] = alphabet_ext[inc[i] - 1]
    return "".join(inc)