# Werte
x = 0.18

# Eingabe
print("Geben Sie Ihr Bruttogehalt in Euro ein:")
eingabe = input()

# Eingabe in eine Zahl umwandeln
brutto = float(eingabe)

# Berechnung
steuer = brutto * x

print("Es ergibt sich ein Steuerbetrag von", steuer, "Euro")
