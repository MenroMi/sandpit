
sum_choose = int(input()) #podajemy kwotę netto/brutto
take_brutto_or_netto = str(input()) # podajemy brutto or netto
choose_vat = int(input()) # podajemy procent obliczania

def summary_brutto():

    if choose_vat == 23:
        if take_brutto_or_netto == "brutto" or "BRUTTO":
            take_brutto = sum_choose * (choose_vat / 100)
            # print("Sum brutto z procentem 23%:", take_brutto)
    elif choose_vat == 0:
        if take_brutto_or_netto == "brutto" or "BRUTTO":
            take_brutto = sum_choose * (choose_vat / 100)
            # print("Sum brutto z procentem 0%:", take_brutto)
    elif choose_vat == 5:
        if take_brutto_or_netto == "brutto" or "BRUTTO":
            take_brutto = sum_choose * (choose_vat / 100)
            # print("Sum brutto z procentem 5%:", take_brutto)
    elif choose_vat == 8:
        if take_brutto_or_netto == "brutto" or "BRUTTO":
            take_brutto = sum_choose * (choose_vat / 100)
            # print("Sum brutto z procentem 8%:", take_brutto)
    else:
        print('Negative. Please give another procent VAT')
    
    
    return print(f"Sum brutto z {choose_vat}%:", take_brutto)


def summary_netto():

    if choose_vat == 23:
        if take_brutto_or_netto == "netto" or "NETTO":
            vat_kwoty_brutto = (sum_choose * choose_vat)//(100 + choose_vat)
            sum_netto = sum_choose - vat_kwoty_brutto
            # print("Sum brutto z procentem 23%:", take_brutto)
    elif choose_vat == 0:
        if take_brutto_or_netto == "netto" or "NETTO":
            vat_kwoty_brutto = (sum_choose * choose_vat)//(100 + choose_vat)
            sum_netto = sum_choose - vat_kwoty_brutto
            # print("Sum brutto z procentem 0%:", take_brutto)
    elif choose_vat == 5:
        if take_brutto_or_netto == "netto" or "NETTO":
            vat_kwoty_brutto = (sum_choose * choose_vat)//(100 + choose_vat)
            sum_netto = sum_choose - vat_kwoty_brutto
            # print("Sum brutto z procentem 5%:", take_brutto)
    elif choose_vat == 8:
        if take_brutto_or_netto == "netto" or "NETTO":
            vat_kwoty_brutto = (sum_choose * choose_vat)//(100 + choose_vat)
            sum_netto = sum_choose - vat_kwoty_brutto
            # print("Sum brutto z procentem 8%:", take_brutto)
    else:
        print("Negative. Please give another procent VAT 0%, 5%, 8% or 23%")

    return print(f"\nVAT od kwoty brutto: {vat_kwoty_brutto} zł"), print(f"Sum netto z {choose_vat}%:", sum_netto, "zł")

