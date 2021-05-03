import shlex
import kivy.core.window as window
from kivy.base import EventLoop

def parse_pgn(pgn):
    pgn_dict = {}
    pgn_items = [line.rstrip('\n') for line in pgn]
    for item in pgn_items:
        if item == "":
            break
        splits = shlex.split(item)
        first_part = str(splits[0])[1:]
        second_part = str(splits[1])[:-1]
        pgn_dict[first_part] = second_part

    return pgn_dict


def reset():

    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}