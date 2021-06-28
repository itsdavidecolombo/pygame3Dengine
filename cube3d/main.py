#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 15:27
# @Description: The main method of the application: here all the objects are instantiated and then the engine is started
#
#################################################
from cube3d.screen import Window
from cube3d.engine import GameEngine, EventHandler, Clock
from cube3d.data_model import Cube
from cube3d.board import GameBoard

def run():

    # ALLOCATE RESOURCES
    player = Cube()

    # CREATE WINDOW
    window = Window('- game screen -')

    # CREATE THE CLOCK
    clock = Clock(fps = 30)

    # CREATE GAME ENGINE
    engine = GameEngine()
    engine.set_clock(clock)
    engine.set_window(window)

    # CREATE GAME BOARD
    board = GameBoard(engine)
    board.set_player(player)

    # CREATE EVENT HANDLER
    handler = EventHandler(guard = engine.guard, board = board)
    engine.set_event_handler(handler)

    # START
    engine.start()
