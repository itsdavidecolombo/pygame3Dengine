#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 15:27
# @Description: The main method of the application: here all the objects are instantiated and then the engine is started
#
#################################################
from cube3d.data_model import Cube
from cube3d.ui import Window
from cube3d.event import EventHandler
from cube3d.engine import GameEngine, Clock, EngineGuard
from cube3d.board import GameBoard
from cube3d.logger import Logger


def run():

    try:
        # DEFINE THE LOGGER
        logger = Logger()

        # ALLOCATE RESOURCES
        player = Cube()

        # CREATE GAME BOARD
        board = GameBoard(player = player, logger = logger)

        # CREATE WINDOW
        window = Window(title = '- game ui -', logger = logger)

        # CREATE THE CLOCK
        clock = Clock(fps = 20, logger = logger)

        # CREATE EVENT HANDLER
        handler = EventHandler(board = board, logger = logger)

        # CREATE GAME ENGINE
        engine = GameEngine(clock = clock, window = window, handler = handler, logger = logger)

        # CREATE THE GUARD
        guard = EngineGuard(engine = engine, logger = logger)
        logger.set_guard(guard = guard)

        # START
        guard.safe_start()
    except ValueError as ex:
        print(ex.__str__())
