#!/usr/bin/env python3

import gc
import tracemalloc

print('Let\'s take a look at memory management')
print('Showing how many objects are created during execution')
objs_before = gc.get_objects()
print(f'# of objs before I run a challenge: {len(objs_before)}')

from apod import get_result
from api_key import key

res = get_result(f'https://api.nasa.gov/planetary/apod?api_key={key}&date=2020-01-02')
objs_after = gc.get_objects()
print(f'# of objs after I run a challenge: {len(objs_after)}')
for obj in objs_after[:10]:
    print(repr(obj)[:500])
