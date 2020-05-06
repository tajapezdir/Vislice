def je_deljivo_s_katerim_od(n, seznam):
    if seznam == []:
        return False
    else:
        return n % seznam[0] == 0 or je_deljivo_s_katerim_od(n, seznam[1:])


def prastevila_do(n):
    if n <= 1:
        return []
    manjsa_prastevila = prastevila_do(n - 1)
    if je_deljivo_s_katerim_od(n, manjsa_prastevila):
        return manjsa_prastevila
    else:
        return manjsa_prastevila + [n]

def je_prastevilo(n):
    if n <= 1:
        return False
    else:
        prastevila = prastevila_do(round(n ** 0.5))
        return not je_deljivo_s_katerim_od(n, prastevila)

for i in range(1, 201):
    if je_prastevilo(i):
        print(i)
