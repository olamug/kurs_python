print("Ile pełnych tygodni zajmie zdobycie nowej umiejętności w zależności od tego ile czasu jesteś w stanie poświęcić w tygodniu.")
hours_per_week = input("Ile godzin jesteś w stanie poświęcić na naukę w tygodniu? ")
hours_total = 75
weeks = hours_total // int(hours_per_week)
print("Całość zajmie Ci", weeks, "pełnych tygodni.")