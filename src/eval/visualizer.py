#!/usr/bin/env python
"""Visualizer for collected data.
"""

import networkx as nx
import matplotlib as mpl


def show_network_graph(tags: dict):
    vertices = {}
    edges = {}
    entities = ["place", "location", "spatial_entity", "nonmotion_event", "path"]

    # Collect all potential vertices
    for n in entities:
        try:
            for entity in tags[n]:
                vertices[entity["id"]] = {"label": entity["text"], "type": n}
        except KeyError as e:
            pass

    # Collect all potential edges
    for n in ["qslink", "olink"]:
        try:
            for e in tags[n]:
                edges[e["id"]] = {"fromid": e["fromid"], "toid": e["toid"], "label": e["reltype"], "type": n}
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
    except KeyError as e:
        pass

    # Create Graph and ad edges that are in vertices
    g = nx.Graph()
    # Filter out edges containing stuff we don't want, e.g. motion tags
    edges = [(edges[x]["fromid"], edges[x]["toid"],
              {"weight": 0.18, "label": edges[x]["label"], "type": edges[x]["type"]})
             for x in edges.keys() if
             edges[x]["fromid"] in vertices.keys() and edges[x]["toid"] in vertices.keys()]
    g.add_edges_from(edges)

    pos = nx.kamada_kawai_layout(g, pos=nx.spring_layout(g, seed=5, iterations=500))  # positions for all nodes

    # nodes
    # Determine colors for nodes
    color_lookup = {k: entities.index(vertices[k]["type"]) for k in list(g.nodes)}
    low, *_, high = sorted(color_lookup.values())
    norm = mpl.colors.Normalize(vmin=low, vmax=high, clip=True)
    mapper = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.summer)

    options = {"edgecolors": "tab:gray",
               "node_size": 100,
               "alpha": 0.9,
               "node_color": [mapper.to_rgba(i) for i in color_lookup.values()]}
    nx.draw_networkx_nodes(g, pos, **options)

    # edges
    nx.draw_networkx_edges(g, pos, width=1.0, alpha=0.5, node_size=100,
                           edge_color=["r" if x[2]["type"] == "qslink" else "b" for x in edges])

    # labels
    nx.draw_networkx_labels(g, pos, {x: vertices[x]["label"] for x in g.nodes}, font_size=4, font_color="black")
    nx.draw_networkx_edge_labels(g, pos,
                                 edge_labels={(x[0], x[1]): x[2]["label"] for x in edges},
                                 font_size=4)


def main():
    """Quick usage example.
    """
    print("stats.py\n" + __doc__)


if __name__ == "__main__":
    main()

