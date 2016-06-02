__author__ = 'Alexey'


average_purchases = 0
cash_desk_work_time = 0
cash_desk_visitors = 0
cash_desk_wait_time = 0
cash_desk_real_waiters = 0
cash_desk_queue_size = 0
cash_desk_queue_max_size = 0


def update_statistics(current_wait_time, queue, purchases, current_client_purchases, purchase_process_time):
    global cash_desk_visitors, cash_desk_wait_time, cash_desk_real_waiters, cash_desk_queue_size, cash_desk_queue_max_size, average_purchases

    cash_desk_visitors += 1
    average_purchases += current_client_purchases
    cash_desk_wait_time += current_wait_time + sum(purchases[client] * purchase_process_time for client in queue)


    if current_wait_time or queue:
        cash_desk_real_waiters += 1

    cash_desk_queue_size += len(queue)
    cash_desk_queue_max_size = max(cash_desk_queue_max_size, len(queue))


def print_report(total_clients, total_time):
    print('Total clients: {:.3f}'.format(total_clients))
    print('Total buyers: {:.3f}'.format(cash_desk_visitors))
    print('Total waiters: {:.3f}'.format(cash_desk_real_waiters))
    print('Cash desk work time: {:.3f} ({:.3f})'.format(cash_desk_work_time, cash_desk_work_time / total_time))
    print('Cash desk average process time: {:.3f}'.format(cash_desk_work_time / cash_desk_visitors))
    print('Customer average purchases size: {:.3f}'.format(average_purchases / cash_desk_visitors))
    print('Cash desk average wait time: {:.3f}'.format(cash_desk_wait_time / cash_desk_visitors))
    print('Cash desk average wait time for real waiters: {:.3f}'
          .format(float('inf') if not cash_desk_real_waiters else cash_desk_wait_time / cash_desk_real_waiters))
    print('Cash desk average queue size: {:.3f}'
          .format(float('inf') if not cash_desk_real_waiters else cash_desk_queue_size / cash_desk_real_waiters))
    print('Cash desk max queue size: {:.3f}'.format(cash_desk_queue_max_size))
