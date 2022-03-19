# zadanie: zrobić konwerter VAT brutto na netto/netto na brutto

# 1. Komputer ma prosić o wybór procentu podatku
# 2. Komputer ma prosić o konwertację brutto na netto lub odwrotnie
# 3. Komputer ma zapytać o kwotę brutto lub netto

# Pierwszy krok: napisać funkcję dla wyboru brutto > netto czy brutto < netto
# def summary_brutto(take_brutto):
#     sum_choose = int(input())
#     take_brutto_or_netto = str(input())
#     if take_brutto_or_netto == take_brutto:
#             take_brutto = sum_choose * (23 / 100)
#             return print("Sum brutto", take_brutto)

sum_choose = int(input()) #podajemy kwotę netto/brutto
take_brutto_or_netto = str(input()) # podajemy brutto or netto
choose_vat = int(input()) # podajemy procent obliczania

if choose_vat == 23:
    def summary_brutto():
        if take_brutto_or_netto == "brutto" or "BRUTTO":
                take_brutto = sum_choose * (choose_vat / 100)
            # print("Sum brutto", take_brutto)
        return take_brutto
    wynik = summary_brutto()
    print("Sum brutto", wynik)
elif choose_vat == 0:
    def summary_brutto():
        if take_brutto_or_netto == "brutto":
                take_brutto = sum_choose * (choose_vat / 100)
            # print("Sum brutto", take_brutto)
        return take_brutto
    wynik = summary_brutto()
    print("Sum brutto", wynik)
elif choose_vat == 5:
    def summary_brutto():
        if take_brutto_or_netto == "brutto":
                take_brutto = sum_choose * (choose_vat / 100)
        return take_brutto
    wynik = summary_brutto()
    print("Sum brutto", wynik)
elif choose_vat == 8:
    def summary_brutto():
        if take_brutto_or_netto == "brutto":
                take_brutto = sum_choose * (choose_vat / 100)
            # print("Sum brutto", take_brutto)
        return take_brutto
    wynik = summary_brutto()
    print("Sum brutto", wynik)
else:
    print('Negative. Please give another procent VAT')
