from dataclasses import dataclass
from typing import Callable

_REGISTRY: dict[str, "BlockSpec"] = {}

@dataclass
class BlockSpec:
    name: str
    func: Callable
    description: str = ""

def block(name: str, description: str = ""):
    def decorator(func):
        _REGISTRY[name] = BlockSpec(name=name, func=func, description=description)
        return func
    return decorator

def get_block(name: str) -> BlockSpec:
    return _REGISTRY[name]

def list_blocks() -> list["BlockSpec"]:
    return list(_REGISTRY.values())