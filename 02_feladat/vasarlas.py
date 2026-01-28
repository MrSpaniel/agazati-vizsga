termek_ar= int(input("Adja meg a termék árát forintban:"))
euro_arfolyam=float(input("Kérem az euro árfolyamát:"))
euro_van= float(input("Mennyi euroval rendelkezel:"))

forint_to_euro = termek_ar / euro_arfolyam
print(f"A termék ára euróban {forint_to_euro}.")
if termek_ar / euro_arfolyam <= euro_van:
    print("A terméket megtudod vásárolni.")
else:
    print("Nem tudod megvásárolni")