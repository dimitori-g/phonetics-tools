from rich.tree import Tree
from rich import print

tree = Tree(':family: [yellow]Phonetic family: 𡿧[/yellow]')

level_1 = tree.add('[blue]𡿧(zai)[/blue]')

level_2_1 = level_1.add('[green]災(zai)[/green]')
level_2_2 = level_1.add('[green]甾(zai,zi)[/green]')

level_2_1.add('𨉒(?)')
level_2_1.add('𨓌(?)')
level_2_1.add('𭴠(?)')

level_2_2.add('㿳(zi)')
level_2_2.add('䅔(zi)')
level_2_2.add('䎩(zi)')
level_2_2.add('䐉(zi)')
level_2_2.add('䣎(zi)')
level_2_2.add('崰(zi)')
level_2_2.add('椔(zi)')
level_2_2.add('[green]淄(zi)[/green]').add('𬩆(?)')
level_2_2.add('湽(zi)')
level_2_2.add('𡸟(zi)')
level_2_2.add('𥚉(zi)')
level_2_2.add('𩜊(zi)')
level_2_2.add('緇缁(zi)')
level_2_2.add('輜輺辎(zi)')
level_2_2.add('錙鍿锱(zi)')
level_2_2.add('鯔鲻(zi)')
level_2_2.add('鶅(zi)')
print(tree)
