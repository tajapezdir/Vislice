import model


def izpis_igre(igra):
    tekst = (
        'Število preostalih poskusov: {preostali}\n\n'
        ' {pravilni_del}\n\n'
        'Neuspeli poskusi: {neuspeli_poskusi}\n\n'
    ).format(
        preostali=model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1, 
        pravilni_del=igra.pravilni_del_gesla(),
        neuspeli_poskusi=igra.nepravilni_ugibi()
    )
    return tekst

def izpis_zmage(igra):
    tekst = (
        'Bravo, zmagali ste! Geslo je bilo: {geslo} \n\n'
    ).format(
        geslo=igra.geslo()
    )
    return tekst

def izpis_poraza(igra):
    tekst = (
        'Škoda, izgubili ste! Geslo je bilo: {geslo} \n\n'
    ).format(
        geslo=igra.geslo()
    )
    return tekst

def zahtevaj_vnos():
    return input('Črka: ')

def pozeni_vmesnik():
    
    igra = model.nova_igra()

    while True:
        # najprej izpisemo stanje, da vidimo, koliko crk je ipd.
        print(izpis_igre(igra))
        # čakamo na črko od uporabnika
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)
        if igra.zmaga():
            print(izpis_zmage(igra))
            break
        elif igra.poraz():
            print(izpis_poraza)
            break
    
    return

# zaženi igro:
pozeni_vmesnik()


