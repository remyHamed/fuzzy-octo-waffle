from dataclasses import dataclass


@dataclass
class UpdateTaskRequest:
    id: int
    title: str
    resume: str
    is_done: bool