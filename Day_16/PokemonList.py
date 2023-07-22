from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("Description", ["Electric Pokemon", "Water Pokemon", "Fire Pokemon"])

table.align = "l"

print(table)