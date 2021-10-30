#!/usr/bin/env python
"""Visualizer for collected data.
"""

import matplotlib.pyplot as plt
import networkx as nx


def show_network_graph(tags: dict):
    # TODO: Color vertices and edges, Fix Label positions, Label edges.
    vertices = {}
    edges = {}

    # Collect all potential vertices
    for n in ["place", "location", "spatial_entity", "nonmotion_event", "path"]:
        try:
            for entity in tags[n]:
                vertices[entity["id"]] = {"label": entity["text"], "type": entity}
        except KeyError as e:
            pass

    # Collect all potential edges
    for n in ["qslink", "olink"]:
        try:
            for e in tags[n]:
                edges[e["id"]] = {"fromid": e["fromid"], "toid": e["toid"], "label": e["reltype"]}
        except KeyError as e:
            pass

    # Merge vertices
    try:
        for l in tags["metalink"]:
            if l["reltype"] == "COREFERENCE":
                # Reference all edges to new point
                for e in edges.keys():
                    if edges[e]["fromid"] == l["fromid"]:
                        edges[e]["fromid"] = l["toid"]
                    elif edges[e]["toid"] == l["fromid"]:
                        edges[e]["toid"] = l["toid"]
                # Adjust vertex
                # vertices[l["toid"]]["label"] += ", " + vertices[l["fromid"]]["label"]
    except KeyError as e:
        pass

    # Create Graph and ad edges that are in vertices
    g = nx.Graph()
    # Filter out edges containing stuff we don't want, e.g. motion tags
    g.add_edges_from([(edges[x]["fromid"], edges[x]["toid"], {"weight": 0.25}) for x in edges.keys() if
                      edges[x]["fromid"] in vertices.keys() and edges[x]["toid"] in vertices.keys()])

    pos = nx.spring_layout(g)  # positions for all nodes

    # nodes
    options = {"edgecolors": "tab:gray", "node_size": 50, "alpha": 0.9}
    nx.draw_networkx_nodes(g, pos, node_color="tab:red", **options)
    # edges
    nx.draw_networkx_edges(g, pos, width=1.0, alpha=0.5)
    # labels
    labels = {x: vertices[x]["label"] for x in g.nodes}
    nx.draw_networkx_labels(g, pos, labels, font_size=4, font_color="black")

    plt.tight_layout()
    plt.axis("off")
    plt.savefig("test.png", dpi=300)


def main():
    """Quick usage example.
    """
    print("stats.py\n" + __doc__)


if __name__ == "__main__":
    main()
