import enum

class EngineState(enum.Enum):
    Created   = 'created'
    Running   = 'running'
    Destroyed = 'destroyed'

    @staticmethod
    def is_allowed_state_transition(from_, to_) -> bool:
        if from_ == EngineState.Created:
            if to_ == EngineState.Created:
                return False
        elif from_ == EngineState.Running:
            if to_ != EngineState.Destroyed:
                return False
        return True
