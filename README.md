![image](https://github.com/duolok/orbyx/assets/42711489/df9ba8b1-0957-4a7f-b648-f27dcec7eec0)

<h1 align="center"> Orbyx </h1>

Orbyx is a Graph Visualization project written with Python and JavaScript. It's main focus is extensibility with plugins.

### Prerequisites

Before you get started with Orbyx, make sure you have the following prerequisites installed on your system:

- Git
- Python

### Installation

Clone the Orbyx repository and navigate into the directory:

```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
./run.sh
```

#### Adding more plugins

First, you need to decide which kind of plugin you want to add. If you decide to go with a Data Source plugin, you need to create a class which 
will implement DataSourceAPI (api/services/data\_source\_api). Or perhaps you could choose to write a Visualizer plugin, then you will need to create a class
which will implement Visualizer (api/services/visualizer_api)

##### DataSourceAPI 
```python3
class DataSourceAPI(ABC):
    @abstractmethod
    def get_name(self) -> str:
        """Abstract property for the name of the data source"""
        pass
 
    @abstractmethod
    def get_requirements(self) -> List:         
        """Abstract method for the name that will return list of dependencies necessary."""
        pass

    @abstractmethod
    def parse_data(self, data: Any) -> List[Dict[str, Any]]:
        """Method that will parse data and consturct a graph"""
        pass

    @abstractmethod
    def get_graph(self, parsed_data: List[Dict[str, Any]]) -> Graph:
        """Method that will send data to the plugin and recieve a graph"""
        pass
```

##### DataSourceAPI 
```python3
class Visualizer(ABC):
    @abstractmethod
    def get_name(self) -> str:
        """Abstract property for the name of the visualizer"""
        pass

    @abstractmethod
    def visualize(self, graph: Graph) -> Any:
        """Abstract method for data visualization"""
        pass
```

After that you will need to put it in a folder and add a setup.py file for it. It should contain these lines:

- 'orbyx\_tinywiki': ['template=tinywiki.engine:WikipediaDataSource'] - example if you're writting a data source plugin
- 'orbyx\_visualizer\_plugin': ['template=visualize.generate_template:BlockVisualizer'] - example if you're writting a data source plugin

Optionally, you want to add dependencies which are required for your plugin.

That's it! You're ready to enjoy Orbyx.

### Currently written plugins
- Tinywiki - Wikipedia Data Source which scrapes wikipedia until its found N number of nodes, it only works with en.wikipedia articles.
- Java Data Source - Written with _antlr_, data source which will go through your java project and make a graph from it.
- Block Visualizer - Visualizer which will make visualization for your graph with squares containing content of the graph node.
- Simple Visualizer - Visualizer which will make blob-like visualization using your graph nodes.

### Additional Views
- Tree View - Displays data in a Tree like way, similar to popular IDEs or text editors, located on left of the  web application.
- Bird View - Minimized view of the entire graph, which traces your zoom with a red rectangle.

#### Gallery
![image](https://github.com/duolok/orbyx/assets/42711489/e9b4ab65-2cc3-42a5-b833-748d31302e5e)
![image](https://github.com/duolok/orbyx/assets/42711489/8c65ffc5-d48a-4969-8fa4-6d94bd392673)
![image](https://github.com/duolok/orbyx/assets/42711489/6d1a63cf-c804-48b2-9b4d-90c8eae38a76)


