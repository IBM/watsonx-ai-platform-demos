import tomllib
from pathlib import Path

def load_config(section: str | None = None) -> dict:
    config = tomllib.loads((Path(__file__).parent / "config.toml").read_text())
    if section is not None:
        print(f"***Log load_config -> section: {config[section]}")
        return config[section]
    else:
        print(f"***Log load_config -> all: {config}")
        return config
