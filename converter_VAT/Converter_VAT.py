def summary_brutto(sum_choose, choose_vat):
    take_brutto = sum_choose * (choose_vat / 100)

    return take_brutto

def summary_netto(sum_choose_1, choose_vat_1):
    vat_kwoty_brutto = (sum_choose_1 * choose_vat_1)//(100 + choose_vat_1)
    sum_netto = sum_choose_1 - vat_kwoty_brutto

    return sum_netto, vat_kwoty_brutto

if __name__ == "__main__": # odpala poniższy kod

    take_brutto_or_netto = str(input('Sposób obliczania (brutto/netto, netto/brutto): ')) # podajemy brutto or netto

    sposob_obliczania = take_brutto_or_netto

    while True:
        sum_choose = input(f'Podaj kwotę {sposob_obliczania}:').strip() #podajemy kwotę netto/brutto
        if "." in sum_choose:
            sum_choose = float(sum_choose)
            break
        if sum_choose.isdigit(): # czy wszystkie znaki stringa są cyfraami
            sum_choose = int(sum_choose)
            break
        else:
            print('Podaj cyferki!')
            continue

    choose_vat = int(input('Podaj procent VAT: ')) # podajemy procent obliczania

    if take_brutto_or_netto == "netto":
        n = summary_netto(sum_choose, choose_vat)
        vat_brutto = n[1]
        kwota_netto = n[0]
        print(f"\nVAT od kwoty brutto: {vat_brutto} zł")
        print(f"Sum netto z {choose_vat}%:", kwota_netto, "zł")

    if take_brutto_or_netto == "brutto":
        b = summary_brutto(sum_choose, choose_vat)
        print(f"Sum brutto z {choose_vat}%:", b)
