from prettytable import PrettyTable
import prettytable
Table = PrettyTable()
Table.add_column("name",["pikachu","squirtle","charmander"])
Table.add_column("type",["Electric","water","fire"])
Table.align = "r"
print(Table)


