import pkg_resources
from services.core_api import CoreAPI


def load_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins

class IspisCore(CoreAPI):

    def _proba(self, proba):
        print(proba)
        visualizer = load_plugins("generate_template")
        return visualizer[0].visualize("xx")