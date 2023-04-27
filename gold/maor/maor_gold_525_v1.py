# Created by maor

from utils.reading_tasks import read_task
from src.hexagen import HexagonsGame, Tile, Shape, Line, Circle, Triangle

task_index = 525
gold_boards = list(read_task(task_index)['gold_boards'])

HexagonsGame.start()

# description:
# task index: 525, image: P01C04T04, collection round: 0, category: conditions, group: train
# agreement scores: [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 0.95, 0.95], [1.0, 1.0, 1.0], [1.0, 0.95, 0.95], [1.0, 1.0, 1.0], [1.0, 0.99, 0.99], [1.0, 0.95, 0.95], [1.0, 0.96, 0.96], [1.0, 1.0, 1.0], [1.0, 0.96, 0.96], [1.0, 1.0, 1.0], [1.0, 0.97, 0.97], [1.0, 1.0, 1.0], [1.0, 0.97, 0.97], [1.0, 1.0, 1.0], [1.0, 0.97, 0.97], [1.0, 1.0, 1.0], [1.0, 0.97, 0.97], [1.0, 1.0, 1.0], [1.0, 0.97, 0.97], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

'''
1. Paint the leftmost tile at the top orange
'''
tile = Tile(column=1,row=1)
tile.draw('orange')

'''
2. Paint the next four tiles directly below it purple.
'''
line = Line(start_tile=tile, length=4, direction='down', include_start_tile=False)
line.draw('purple')

'''
3. Move to the next column, and paint the tile at the bottom green.
'''
tile = Tile(column=2,row=-1)
tile.draw('green')

'''
4. Paint the next four tiles directly above it blue.
'''
line = Line(start_tile=tile, length=4, direction='up', include_start_tile=False)
line.draw('blue')

'''
5. Move to the next column, and paint the tile at the top green.
'''
tile = Tile(column=3,row=1)
tile.draw('green')

'''
6. Paint the next four tiles directly below it blue.
'''
line = Line(start_tile=tile, length=4, direction='down', include_start_tile=False)
line.draw('blue')

'''
7. Move to the next column, and paint the tile at the bottom orange.
'''
tile = Tile(column=4,row=-1)
tile.draw('orange')

'''
8. Paint the next four tiles directly above it purple.
'''
line = Line(start_tile=tile, length=4, direction='up', include_start_tile=False)
line.draw('purple')

'''
9. Move to the next column, and paint the tile at the top green.
'''
tile = Tile(column=5,row=1)
tile.draw('green')

'''
10. Paint the next four tiles directly below it blue.
'''
line = Line(start_tile=tile, length=4, direction='down', include_start_tile=False)
line.draw('blue')

'''
11. Move to the next column, and paint the tile at the bottom green.
'''
tile = Tile(column=6,row=-1)
tile.draw('green')

'''
12. Paint the next four tiles directly above it blue.
'''
line = Line(start_tile=tile, length=4, direction='up', include_start_tile=False)
line.draw('blue')

'''
13. Move to the next column, and paint the tile at the top green.
'''
tile = Tile(column=7,row=1)
tile.draw('green')

'''
14. Paint the next four tiles directly below it blue.
'''
line = Line(start_tile=tile, length=4, direction='down', include_start_tile=False)
line.draw('blue')

'''
15. Move to the next column, and paint the tile at the bottom green.
'''
tile = Tile(column=8,row=-1)
tile.draw('green')

'''
16. Paint the next four tiles directly above it blue.
'''
line = Line(start_tile=tile, length=4, direction='up', include_start_tile=False)
line.draw('blue')

'''
17. Move to the next column, and paint the tile at the top orange.
'''
tile = Tile(column=9,row=1)
tile.draw('orange')

'''
18. Paint the next four tiles directly below it purple.
'''
line = Line(start_tile=tile, length=4, direction='down', include_start_tile=False)
line.draw('purple')

'''
19. Move to the next column, and paint the tile at the bottom orange.
'''
tile = Tile(column=10,row=-1)
tile.draw('orange')

'''
20. Paint the next four tiles directly above it purple.
'''
line = Line(start_tile=tile, length=4, direction='up', include_start_tile=False)
line.draw('purple')

'''
21. Move to the next column, and paint the tile at the top green.
'''
tile = Tile(column=11,row=1)
tile.draw('green')

'''
22. Paint the next four tiles directly below it blue.
'''
line = Line(start_tile=tile, length=4, direction='down', include_start_tile=False)
line.draw('blue')

'''
23. Move to the next column, and paint the tile at the bottom orange.
'''
tile = Tile(column=12,row=-1)
tile.draw('orange')

'''
24. Paint the next four tiles directly above it purple.
'''
line = Line(start_tile=tile, length=4, direction='up', include_start_tile=False)
line.draw('purple')

'''
25. Move to the next column, and paint the tile at the top orange.
'''
tile = Tile(column=13,row=1)
tile.draw('orange')

'''
26. Paint the next four tiles directly below it purple.
'''
line = Line(start_tile=tile, length=4, direction='down', include_start_tile=False)
line.draw('purple')

'''
27. Move to the next column, and paint the tile at the bottom orange.
'''
tile = Tile(column=14,row=-1)
tile.draw('orange')

'''
28. Paint the next four tiles directly above it purple.
'''
line = Line(start_tile=tile, length=4, direction='up', include_start_tile=False)
line.draw('purple')

'''
29. Move to the next column, and paint the tile at the top orange.
'''
tile = Tile(column=15,row=1)
tile.draw('orange')

'''
30. Paint the next four tiles directly below it purple.
'''
line = Line(start_tile=tile, length=4, direction='down', include_start_tile=False)
line.draw('purple')

'''
31. Move to the next column, and paint the tile at the bottom green.
'''
tile = Tile(column=16,row=-1)
tile.draw('green')

'''
32. Paint the next four tiles directly above it blue.
'''
line = Line(start_tile=tile, length=4, direction='up', include_start_tile=False)
line.draw('blue')

'''
33. Move to the next column, and paint the tile at the top orange.
'''
tile = Tile(column=17,row=1)
tile.draw('orange')

'''
34. Paint the next four tiles directly below it purple.
'''
line = Line(start_tile=tile, length=4, direction='down', include_start_tile=False)
line.draw('purple')

'''
35. Move to the final column, and paint the tile at the bottom green.
'''
tile = Tile(column=18,row=-1)
tile.draw('green')

'''
36. Paint the next four tiles directly above it blue.
'''
line = Line(start_tile=tile, length=4, direction='up', include_start_tile=False)
line.draw('blue')

HexagonsGame.plot(gold_boards=gold_boards, multiple=0)
