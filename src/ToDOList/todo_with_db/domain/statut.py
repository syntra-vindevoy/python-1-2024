from enum import Enum


class Status(Enum):
    NEW = 'NEW'
    IDLE = 'IDLE'
    DOING = 'DOING'
    DONE = 'DONE'
