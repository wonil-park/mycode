#!/usr/bin/env python3

import tracemalloc

print('Let\'s take a look at memory management')

tracemalloc.start(5)

time1 = tracemalloc.take_snapshot()

from apod import get_result
from api_key import key

res = get_result(f'https://api.nasa.gov/planetary/apod?api_key={key}&date=2020-01-02')

time2 = tracemalloc.take_snapshot()

hist = time2.compare_to(time1, 'lineno')
for line in hist[:10]:
    print(line)

memory_eater = time2.compare_to(time1, 'traceback')
print('=============================================')
print(memory_eater[0].traceback.format())