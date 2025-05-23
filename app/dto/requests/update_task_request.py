from dataclasses import dataclass
import datetime


@dataclass
class UpdateTaskRequest:
    id: int
    title: str
    resume: str
    creation_date: datetime
    is_done: bool