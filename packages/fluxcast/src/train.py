"""Training entry point for FluxCast."""


def train(config_path: str) -> None:
    print(f"loading config from {config_path}")


if __name__ == "__main__":
    train("configs/default.yaml")
