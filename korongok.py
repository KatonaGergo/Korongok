korongok = []
interval = range(1, 9)

def megjelenit_tabla(korongok):

    tabla = [["." for _ in range(8)] for _ in range(8)]
    

    for x, y in korongok:
        tabla[x - 1][y - 1] = "O"


    print("  1 2 3 4 5 6 7 8")


    for i, sor in enumerate(tabla):
        print(f"{i + 1} " + " ".join(sor))




while True:
    megjelenit_tabla(korongok)
    if not (korong_x_pos := input("Írd ide a korong sorának számát! [1-8] (Enter: Kilépés): ")):
        break
    if not (korong_y_pos := input("Írd ide a korong oszlopának számát! [1-8] (Enter: Kilépés): ")):
        break

    try:
        korong_x_pos = int(korong_x_pos)
        korong_y_pos = int(korong_y_pos)

        if korong_x_pos in interval and korong_y_pos in interval:
            pozicio = (korong_x_pos, korong_y_pos)
            if pozicio in korongok:
                korongok.remove(pozicio)
                print(f"A pozíció ({korong_x_pos}, {korong_y_pos}) törölve lett a tábláról, mivel már szerepelt benne.")
            else:
                korongok.append(pozicio)
                print(f"Helyes értékek: sor: {korong_x_pos}, oszlop: {korong_y_pos}. Korong hozzáadva.")
        else:
            print("A megadott számok legyenek az intervallumban [1-8]!")

    except ValueError:
        print("Számot adj meg, és az legyen az intervallumban [1-8]!")

print("Kilépés. A táblán maradt korongok:", korongok)

    