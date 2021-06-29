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
from cube3d.logger import Logger


def run():

    # CREATE THE GUARD
    guard = EngineGuard()

    # DEFINE THE LOGGER
    logger = Logger(guard)
    guard.set_logger(logger)

    # ALLOCATE RESOURCES
    player = Cube()

    # CREATE GAME BOARD
    board = GameBoard(player = player, logger = logger)

    # CREATE WINDOW
    window = Window(title = '- game screen -', logger = logger)

    # CREATE THE CLOCK
    clock = Clock(fps = 30, logger = logger)

    # CREATE EVENT HANDLER
    handler = EventHandler(board = board, logger = logger)

    # CREATE GAME ENGINE
    engine = GameEngine(clock = clock, window = window, handler = handler, logger = logger)
    guard.set_engine(engine)

    # START
    engine.start()
