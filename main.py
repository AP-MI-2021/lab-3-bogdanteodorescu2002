def prime(n):
    '''
    functia determina daca un numar este prim sau nu
    :param n: numar intreg
    :return: True daca numarul este prim, False daca nu
    '''
    if n < 2:
        return False
    for i in range (2, n // 2 + 1, 1):
        if n % i == 0:
            return False
    return True

def get_longest_all_primes(l):
    '''
    functia determina cea mai lunga subsecventa de numere prime a unui sir
    :param l: lista de numere
    :return: subsecventa cu cele mai multe numere prime consecutive
    '''
    length = 0
    maxim = 0
    finalindex = 0
    lst = []
    for i in range (len(l)):
        if prime(l[i]) == True:
            length += 1
            if length > maxim:
                maxim = length
                finalindex = i
        else:
            length = 0
    for i in range (finalindex - maxim + 1, finalindex + 1):
        lst.append(l[i])
    return lst

def number_div_count (n):
    '''
    functia calculeaza numarul de divizori ai numarului n
    :param n: numar intreg
    :return: numarul de divizori
    '''
    d = 1
    if n == 0:
        return 0
    if n < 0:
        n = -n
    for i in range(1,n // 2 + 1):
        if n % i == 0:
            d += 1
    return d

def get_longest_same_div_count(s):
    '''
    functia determina cea mai lunga subsecventa de numere cu acelasi numar de divizori dintr-o lista
    :param s: lista initiala
    :return: cea mai lunga subsecventa de numere cu acelasi numar de divizori dintr-o lista
    '''
    lst = []
    l = 1
    maxim = 0
    finalIndex = 0
    p = number_div_count(s[0])
    for i in range (1, len(s)):
        if p == number_div_count(s[i]):
            l += 1
            if l > maxim:
                maxim = l
                finalIndex = i
        else:
            l = 1
        p = number_div_count(s[i])
    for i in range (finalIndex - maxim + 1, finalIndex + 1):
        lst.append(s[i])
    return lst

def readList():
    l = []
    p = input("Introduceti elemnetele sirului separate prin virgula, ")
    numberAsString = p.split(",")
    for x in numberAsString:
        l.append(int(x))
    return l

def prime_digits(n):
    '''
    functia verifica daca un numar are toate cifrele numere prime
    :param n: numar intreg
    :return: True daca numarul are toate cifrele numere prime, si False daca nu
    '''
    while n > 0:
        if prime(n % 10) == True:
            n = n // 10
        else:
            return False
    return True

def get_longest_prime_digits(l):
    '''
    functia determina cea mai lunga subsecventa de numere consecutive care au toate cifrele numere prime
    :param l: lista initiala
    :return: cea mai lunga subsecventa de numere consectutive care au toate cifrele numere prime
    '''
    length = 0
    maxim = 0
    finalindex = 0
    lst = []
    for i in range(len(l)):
        if prime_digits(l[i]) == True:
            length += 1
            if length > maxim:
                maxim = length
                finalindex = i
        else:
            length = 0
    for i in range(finalindex - maxim + 1, finalindex):
        lst.append(l[i])
    return lst

if __name__ == '__main__':
    finish = False
    while not finish:
        print("Exercitiul 2. Toate numerele sunt prime.")
        print("Exercitiul 12. Toate numerele același număr de divizori.")
        print("Exercitiul 13. Toate numerele sunt formate din cifre prime.")
        print("x. Iesiti din program")
        option = input("Dati optiunea: ")
        if option == '2':
            l = readList()
            print("Subsecventa cautata este: ")
            print(get_longest_all_primes(l))
            #test_get_largest_prime_below()
        elif option == '12':
            l = readList()
            print(get_longest_same_div_count(l))
            #test_get_perfect_squares()
        elif option == '13':
            l = readList()
            print(get_longest_prime_digits(l))
            #test_get_perfect_squares()
        elif option == 'x':
            finish = True
        else:
            print("Optiunea nu este valida")
