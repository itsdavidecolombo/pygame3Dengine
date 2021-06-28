from cube3d.screen import Window
from cube3d.engine import GameEngine, EventHandler
from cube3d.data_model import Cube
from cube3d.board import GameBoard

def run():

    # ALLOCATE RESOURCES
    player = Cube()

    # CREATE WINDOW
    window = Window('- game screen -')

    # CREATE GAME ENGINE
    engine = GameEngine()
    engine.set_fps(30)
    engine.set_window(window)

    # CREATE GAME BOARD
    board = GameBoard(engine, player)


    # CREATE EVENT HANDLER
    handler = EventHandler(engine, board)
    engine.set_event_handler(handler)

    # START
    engine.start()
