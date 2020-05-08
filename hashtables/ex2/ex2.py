#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_dict = {}
    route = []

    for t in tickets:
        ticket_dict[t.source] = t.destination

    cur_ticket = ticket_dict['NONE']

    while cur_ticket != 'NONE':
        route.append(cur_ticket)
        cur_ticket = ticket_dict[cur_ticket]

    route.append(cur_ticket)

    return route
