import pkg_resources
from services.data_source_api import DataSourceAPI
from services.visualizer_api import Visualizer
from typing import Type, List

def get_visualizer_plugins() -> List[Visualizer]:
    return [plugin.load() for plugin in pkg_resources.iter_entry_points(group='orbyx_visualizer_plugin')]

def get_data_source_plugins() -> List[DataSourceAPI]:
    return [plugin.load() for plugin in pkg_resources.iter_entry_points(group='orbyx_data_source_plugin')]

def get_visualizer_plugin_by_name(name: str) -> Visualizer:
    return next((plugin() for plugin in get_visualizer_plugins() if issubclass(plugin, Visualizer) and plugin().get_name() == name), None)

def get_data_source_plugin_by_name(name: str) -> DataSourceAPI:
    return next((plugin() for plugin in get_data_source_plugins() if issubclass(plugin, DataSourceAPI) and plugin().get_name() == name), None)

def get_plugin_by_name(group: str, name: str, base_type: Type) -> Type:
    return next((plugin() for plugin in pkg_resources.iter_entry_points(group=group) if issubclass(plugin, base_type) and plugin().get_name() == name), None)
