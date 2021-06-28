#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 15:27
# @Description: The main method of the application: here all the objects are instantiated and then the engine is started
#
#################################################
from cube3d.data_model import Cube
from cube3d.screen import Window
from cube3d.event import EventHandler
from cube3d.engine import GameEngine, Clock, EngineGuard
from cube3d.board import GameBoard

def run():

    # ALLOCATE RESOURCES
    player = Cube()

    # CREATE GAME BOARD
    board = GameBoard(player = player)

    # CREATE WINDOW
    window = Window('- game screen -')

    # CREATE THE CLOCK
    clock = Clock(fps = 30)

    # CREATE THE GUARD
    guard = EngineGuard()

    # CREATE EVENT HANDLER
    handler = EventHandler(guard = guard, board = board)

    # CREATE GAME ENGINE
    engine = GameEngine(clock = clock, window = window, guard = guard, handler = handler)
    guard.set_engine(engine)

    # START
    engine.start()
