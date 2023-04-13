# Created by maor

from utils.reading_tasks import read_task
from src.hexagen import HexagonsGame, Tile, Shape, Line, Circle, Triangle

task_index = 549
gold_boards = list(read_task(task_index)['gold_boards'])

HexagonsGame.start()

# description:
# task index: 549, image: P01C04T20, collection round: 0, category: conditions, group: train
# agreement scores: [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 0.72, 0.72], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 0.92, 0.92], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

'''
1. Start from the top left corner of the board and move over one column to the
right. Fill in the top tile in this column purple.
'''
HexagonsGame.record_step(step_name='1')

tile = Tile(column=2, row=1)
tile.draw('purple')

'''
2. Make the next 2 tiles down purple also
'''
line = Line(start_tile=tile, length=2, include_start_tile=False, direction='down')
line.draw('purple')

'''
3. Fill in the tile that is to the right and slightly down from the bottom purple
tile, making it purple as well.
'''
tile = line.end_tile.neighbor(direction='down_right')
tile.draw('purple')

'''
4. Make the tile 1 column to the right and slightly up purple too
'''
tile = tile.neighbor(direction='up_right')
tile.draw('purple')

'''
5. Now fill in the 2 tiles directly above this one with purple.
'''
line = Line(start_tile=tile.neighbor(direction='up'), length=2, direction='up')
line.draw('purple')

'''
6. Then go over to the left one column and fill the top tile purple
'''
tile = line.end_tile.neighbor(direction='up_left')
tile.draw('purple')

'''
7. The shape should have 2 blank tiles in the middle - color these green.
'''
shape1 = HexagonsGame.get_record(step_names=['1'])
shape1.neighbors(criterion='inside').draw('green')

'''
8. Leave one column to the right of this shape blank and recreate the purple shape
with orange tiles.
'''
shape2 = shape1.copy_paste(shift_direction='right', spacing=1)
shape2.draw('orange')

'''
9. Fill the 2 blank tiles inside the shape with green on the top and blue on the
bottom
'''
blank_tiles = shape2.neighbors(criterion='inside')
blank_tiles.extreme(direction='up').draw('green')
blank_tiles.extreme(direction='down').draw('blue')

'''
10. Leave another column to the right blank and recreate the frame of the shape in
orange again.
'''
shape3 = shape2.copy_paste(shift_direction='right', spacing=1)
shape3.draw('orange')

'''
11. The top blank tile inside the frame should be blue and the tile below it should
be green.
'''
blank_tiles = shape3.neighbors(criterion='inside')
blank_tiles.extreme(direction='up').draw('blue')
blank_tiles.extreme(direction='down').draw('green')

'''
12. Leave one more column to the right blank. Create the frame of the shape again in
purple.
'''
shape4 = shape3.copy_paste(shift_direction='right', spacing=1)
shape4.draw('purple')

'''
13. Fill in the inside tiles with blue.
'''
blank_tiles = shape4.neighbors(criterion='inside')
blank_tiles.draw('blue')

'''
14. Move to the bottom left corner of the board and go one column over to the right
and one tile up. Make this tile orange.
'''

tile = Tile(column=2,row=-2)
tile.draw('orange')

'''
15. Recreate the frame of the same shape as above in orange using this newest orange
tile as the bottom left-most tile.
'''
shape5 = shape1.copy_paste(shift_direction='down', spacing=2)
shape5.draw('orange')

'''
16. Fill in the top blank tile inside the shape with green and the bottom inside
tile with blue.
'''
blank_tiles = shape5.neighbors(criterion='inside')
blank_tiles.extreme(direction='up').draw('green')
blank_tiles.extreme(direction='down').draw('blue')

'''
17. Recreate the frame of the shape 3 more times in purple, leaving one column to
the right of each shape blank so each new shape is in line with the shape above
it.
'''
shape6 = shape5.copy_paste(shift_direction='right', spacing=1)
shape6.draw('purple')

shape7 = shape6.copy_paste(shift_direction='right', spacing=1)
shape7.draw('purple')

shape8 = shape7.copy_paste(shift_direction='right', spacing=1)
shape8.draw('purple')

'''
18. Fill in the first new purple shape's inside tiles with green.
'''
shape6.neighbors(criterion='inside').draw('green')

'''
19. Fill in the next shape's blank tiles blue.
'''
shape7.neighbors(criterion='inside').draw('blue')

'''
20. Color in the last shape's blank tiles with green.
'''
shape8.neighbors(criterion='inside').draw('green')

HexagonsGame.plot(gold_boards=gold_boards, multiple=0)
