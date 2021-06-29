import enum
import logging

class EngineState(enum.Enum):
    Created   = 'created'
    Running   = 'running'
    Destroyed = 'destroyed'

    @staticmethod
    def is_allowed_state_transition(from_, to_) -> bool:
        if from_ == EngineState.Created:
            if to_ != (EngineState.Running or EngineState.Destroyed):
                logging.log(level = logging.ERROR, msg = f'Cannot change state from {from_} to {to_}')
                return False
        elif from_ == EngineState.Running:
            if to_ != EngineState.Destroyed:
                logging.log(level = logging.ERROR, msg = f'Cannot change state from {from_} to {to_}')
                return False
        return True
