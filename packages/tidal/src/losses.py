"""Loss functions for the Tidal ensemble."""


def crps_loss(pred, target):
    return abs(pred - target)
