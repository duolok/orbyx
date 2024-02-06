
data_tree_init = {};
data_tree_nodes = {}

var tree = () => {
    $.ajax(
        {
            method: "GET",
            url: "http://localhost:8000/orbyx/json",
            success: function(data){
                console.log("success");
                console.log(data);
                generate_json(data);
            },
            error: function(){
                console.error("something bad happened");
            }
        }
    );
}

tree();

function generate_json(data){
    nodes = data.nodes;
    edges = data.edges;

    nodes.forEach((node) => {
        node = JSON.parse(node);

        var hasChildren = [];
        if(node.children > 0){
            hasChildren = true;
        }

        if(data_tree_init[node["id"]] == undefined) {

            data_tree_init[node["id"].toString()] = {
                'id': node["id"],
                'text' : node["name"],
                'children' : false
            }
        }

        if(data_tree_nodes[node["id"]] == undefined) {

            data_tree_nodes[node["id"].toString()] = [];
        }

        edges.forEach((edge) => {
            edge = JSON.parse(edge);

            if(node["id"] == edge["source"]["id"]){
                // data_dict_init[node["id"]]["children"].push({
                //     'id': edge["target"]["id"],
                //     'text': edge["target"]["name"],
                //     'children': []
                // });
                data_tree_nodes[node["id"]].push(edge["target"]);
            }
        })
    })

    console.log(data_tree_init);
    console.log(data_tree_nodes);

    generate_tree();
}

function generate_tree() {

    var data = [];

    for (const [key, value] of Object.entries(data_tree_init)) {
        data.push(value);
    }

    $('#tree-canvas').jstree({
        'core' : {
            "check_callback": true,
            "data" : data
        },
        "types" : {
          "default" : {
            "icon" : "fa fa-user fa-2xl"
          }
        },
        "plugins": [
          "contextmenu", "types", "wholerow"
        ]
    }).on('create_node.jstree', function(e, data) {
        console.log('saved');
    });

    $('#tree-canvas').on('select_node.jstree', function (e, data) {
        var selectedNode = data.node

        console.log("CHILDREN: ");
        console.log(selectedNode.children.length);

        if(selectedNode.children <= 0){
                data_tree_nodes[selectedNode.id].forEach((child) => {
                console.log(child);
                var newNodeData = {
                    text: child.name,
                    parent: selectedNode.id
                };

                $('#tree-canvas').jstree('create_node', selectedNode.id, newNodeData, "last", function(new_node) {
                    console.log("New node created:", new_node.id);
                });
            });
        }


    });
}