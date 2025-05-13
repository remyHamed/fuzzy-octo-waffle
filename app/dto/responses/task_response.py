import datetime
from dataclasses import dataclass


@dataclass
class TaskResponse:
    id: int
    title: str
    creation_date: datetime
    resume: str
    is_done: bool