"""please note this multithreading is all done by Claude.ai, just as a fun
experiment"""

import random
from concurrent.futures import ProcessPoolExecutor

def count_sevens(rolls):
    got_seven = 0
    for _ in range(rolls):
        if random.randint(1, 6) + random.randint(1, 6) == 7:
            got_seven += 1
    return got_seven

if __name__ == '__main__':
    rolls = 10_000_0000
    workers = 16
    chunk = rolls // workers

    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(count_sevens, chunk) for _ in range(workers)]
        total_sevens = sum(f.result() for f in futures)

    print(total_sevens / rolls)