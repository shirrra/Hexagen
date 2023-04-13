# Created by maor

from utils.reading_tasks import read_task
from src.hexagen import HexagonsGame, Tile, Shape, Line, Circle, Triangle

task_index = 113
gold_boards = list(read_task(task_index)['gold_boards'])

HexagonsGame.start()

# description:
# task index: 113, image: P01C03T09, collection round: 1, category: conditional iteration, group: train
# agreement scores: [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

'''
1. fill in the 7th column with purple.
'''
line1 = Line(start_tile=Tile(7,1), direction='down')
line1.draw('purple')

'''
2. Fill every other spot in the 8th column with blue starting at the top.
'''

'''
3. Make a diagonal line going down from each blue spot.
'''

HexagonsGame.plot(gold_boards=gold_boards, multiple=0)
