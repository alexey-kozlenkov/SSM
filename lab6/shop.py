__author__ = 'Alexey'
from collections import namedtuple, deque
from random import uniform, randint
import lab6.analyze as analyze

purchase_process_time = 3

cash_queue = deque()
current_client_process_time = 0
purchases = {}
free_clients = {}

shopboard_type = namedtuple('shopboard', ['name', 'probability', 'base_time', 'range_time', 'next_shopboard'])
fourth_shopboard = shopboard_type('fourth', 0.90, 50, 15, None)
third_shopboard = shopboard_type('third', 0.70, 100, 25, fourth_shopboard)
second_shopboard = shopboard_type('second', 0.85, 160, 30, third_shopboard)
first_shopboard = shopboard_type('first', 0.65, 180, 60, second_shopboard)

shopboard_lock = {first_shopboard: {}, second_shopboard: {}, third_shopboard: {}, fourth_shopboard: {}}


def process_new_client(client):
    free_clients[client] = first_shopboard


def do_work():
    process_free_clients()
    process_shopboards_queues()
    clean_queues()
    process_cash_desk_queue()


def process_free_clients():
    for client, shopboard in free_clients.items():
        process_client(client, shopboard)
    free_clients.clear()


def process_client(client, shopboard):
    if shopboard:
        result = push_to_shopboard(client, shopboard)
        if not result:
            process_client(client, shopboard.next_shopboard)
    elif client in purchases:
        analyze.update_statistics(current_client_process_time, cash_queue, purchases, purchases[client],
                                  purchase_process_time)
        cash_queue.append(client)


def push_to_shopboard(client, shopboard):
    base = uniform(0, 1)
    if base <= shopboard.probability:
        stay_time = shopboard.base_time + randint(-shopboard.base_time, shopboard.base_time)
        shopboard_lock[shopboard][client] = stay_time
        purchases[client] = purchases.setdefault(client, 0) + 1
        return True
    return None


def process_shopboards_queues():
    for shopboard, queue in shopboard_lock.items():
        for client in queue:
            queue[client] -= 1


def process_cash_desk_queue():
    global current_client_process_time

    if cash_queue or current_client_process_time:
        analyze.cash_desk_work_time += 1
        if not current_client_process_time:
            current_client_process_time = purchases[cash_queue.popleft()] * purchase_process_time
        current_client_process_time -= 1


def clean_queues():
    for shopboard, queue in shopboard_lock.items():
        finished_clients = filter(lambda x: queue[x] == 0, list(queue))
        for client in finished_clients:
            del queue[client]
            process_client(client, shopboard.next_shopboard)
