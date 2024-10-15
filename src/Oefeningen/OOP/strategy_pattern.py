import random
from typing import Callable
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

guid = uuid.uuid1()


class Ticket:
    def __init__(self, ticket_number: uuid.UUID, description, date_created:datetime, priority:int=5, ):
        self.ticket_number = ticket_number
        self.description = description
        self.priority = priority
        self.date_created = date_created

    def __repr__(self):
        return f"Ticket({self.ticket_number}, {self.description}, {self.date_created}, {self.priority})"

    def __str__(self):
        return f"Ticket({self.ticket_number}, {self.description}, {self.date_created}, {self.priority}))"

# Strategy solution with high level functions
class StrategyPattern(ABC):
    @abstractmethod
    def create_ordering(self, list_ticket:List[Ticket]) -> List[Ticket]:
        pass

class FifoStrategyPattern(StrategyPattern):
    def create_ordering(self, list_ticket:List[Ticket]) -> List[Ticket]:
        return list_ticket.copy()

class LifoStrategyPattern(StrategyPattern):
    def create_ordering(self, list_ticket:List[Ticket]) -> List[Ticket]:
        list_copy= list_ticket.copy()
        list_copy.reverse()
        return list_copy

class PrioStrategyPattern(StrategyPattern):
    def create_ordering(self, list_ticket:List[Ticket]) -> List[Ticket]:
        list_copy= sorted(list_ticket, key=lambda ticket: ticket.priority, reverse=False)
        return list_copy

class RandomStrategyPattern(StrategyPattern):
    def create_ordering(self, list_ticket:List[Ticket]) -> List[Ticket]:
        list_copy= list_ticket.copy()
        random.shuffle(list_copy)
        return list_copy

# Strategy solution with callable
def fifo_strategy(list_ticket:List[Ticket]) -> List[Ticket]:
    return list_ticket.copy()


def lifo_strategy(list_ticket:List[Ticket]) -> List[Ticket]:
    list_copy= list_ticket.copy()
    list_copy.reverse()
    return list_copy


def prio_strategy(list_ticket:List[Ticket]) -> List[Ticket]:
    list_copy= sorted(list_ticket, key=lambda ticket: ticket.priority, reverse=False)
    return list_copy


def random_strategy(list_ticket:List[Ticket]) -> List[Ticket]:
    list_copy= list_ticket.copy()
    random.shuffle(list_copy)
    return list_copy




class TicketStore:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def proces_tickets(self, proces_strategy:StrategyPattern):
        if len(self.tickets)==0:
            return
        ticket_list = proces_strategy.create_ordering(self.tickets)
        return ticket_list

    def proces_tickets_func(self,func):
        if len(self.tickets) == 0:
            return
        ticket_list = func(self.tickets)
        return ticket_list



class TicketGenerator:

    @staticmethod
    def generate_tickets(description:str,prio:int)->Ticket:
        return Ticket(ticket_number=uuid.uuid1(),description=description,priority=prio,date_created=datetime.now())


def print_pretty(list_tickets:List[Ticket],title):
    print(title)
    print("----------")
    for ticket in list_tickets:
        print(f"ticket.description : {ticket.description}")
        print(f"ticket.date_created : {ticket.date_created}")
        print(f"ticket.priority: {ticket.priority}")
        print(f"ticket.ticket_number: {ticket.ticket_number}\n")


if __name__ == '__main__':
    ticket_store = TicketStore()
    for t in range(1,10):
        ticket_store.add_ticket(TicketGenerator.generate_tickets(description=f"test{t}",prio=random.randint(1,10)))

    #using Abstract class strategy pattern
    print_pretty(ticket_store.proces_tickets(RandomStrategyPattern()),"Random")

    print_pretty(ticket_store.proces_tickets(LifoStrategyPattern()),"Lifo")

    print_pretty(ticket_store.proces_tickets(FifoStrategyPattern()),"Fifo")

    print_pretty(ticket_store.proces_tickets(PrioStrategyPattern()),"Priority")


    #High level functions strategy pattern
    print_pretty(ticket_store.proces_tickets_func(random_strategy), "Random")

    print_pretty(ticket_store.proces_tickets_func(lifo_strategy), "Lifo")

    print_pretty(ticket_store.proces_tickets_func(fifo_strategy), "Fifo")

    print_pretty(ticket_store.proces_tickets_func(prio_strategy), "Priority")