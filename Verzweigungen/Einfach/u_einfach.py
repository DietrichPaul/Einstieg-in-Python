# Eingabe
print("Geben Sie Ihr Bruttogehalt in Euro ein:")
brutto = float(input())

# Berechnung
if brutto > 2500:
    steuer = brutto * 0.22
else:
    steuer = brutto * 0.18

# Ausgabe
print("Es ergibt sich ein Steuerbetrag von", steuer, "Euro")
