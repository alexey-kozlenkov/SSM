__author__ = 'Alexey'
import uuid
import lab6.shop as shop
from random import expovariate
from math import ceil

lambd = 95
total_time = 8 * 60 * 60


def next_client_time(lambd):
    return ceil(expovariate(1 / lambd))


clients_counter = 0
next_client_arrive_time = next_client_time(lambd)

for t in range(total_time):
    if t == next_client_arrive_time:
        clients_counter += 1
        next_client_arrive_time += next_client_time(lambd)
        client_id = uuid.uuid4()
        shop.process_new_client(client_id)
    shop.do_work()

shop.analyze.print_report(clients_counter, total_time)
