"""FluxCast model."""


class FluxCastModel:
    def __init__(self, hidden=64):
        self.hidden = hidden

    def forward(self, batch):
        raise NotImplementedError
