from dataclasses import dataclass


@dataclass
class CreateTaskRequest:    
    title: str
    resume: str