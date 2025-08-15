from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Task:
    id: Optional[int] = field(default=None, init=False)
    title: str
    description: str
    completion: bool = False
