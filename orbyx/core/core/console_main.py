from typing import List, Union

import pkg_resources
from services.visualizer_api import Visualizer


def console_menu(*args, **kwargs):
    plugini: List[Union[Visualizer]] = \
        kwargs.get("visualizer", [])
    if not plugini:
        print("Nije prepoznati nijedan plugin!")
        return
    else:
        plugini[0].visualize("DA LIII")



def load_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins


def main():
    try:
        visualizer = load_plugins("orbyx_visualizer")
    except Exception as e:
            print("Error: {}".format(e))
            return
    try:
        console_menu(visualizer=visualizer)

    except Exception as e:
        print("Error: {}".format(e))
        return


if __name__ == '__main__':
    main()