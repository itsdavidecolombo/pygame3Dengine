from cube3d.screen.window import Window
from cube3d.engine.game_engine import GameEngine
from cube3d.engine.event_handler import EventHandler
from cube3d.data_model.cube import Cube
from cube3d.board.game_board import GameBoard

def run():

    # ALLOCATE RESOURCES
    cube = Cube()

    # CREATE WINDOW
    window = Window('- game screen -')

    # CREATE GAME ENGINE
    engine = GameEngine()
    engine.set_fps(30)
    engine.set_window(window)

    # CREATE GAME BOARD
    board = GameBoard(engine)

    # CREATE EVENT HANDLER
    handler = EventHandler(engine)
    engine.set_event_handler(handler)

    # START
    engine.start()
