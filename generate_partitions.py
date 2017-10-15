import sys
import igraph
import csv


def main(data_path, graph_path):
    # read in MCD metadata
    (data, idx_inv) = init_data(data_path)

    # read in adjacency list
    g = init_graph(graph_path, idx_inv)

    # find possible partitions
    parts = get_partitions(g)

    # filter on population parity
    parity_parts = filter(
        lambda x: population_parity(x, 0.25, data, idx_inv),
        parts
    )

    # list of partitions ready for output
    out = [
        [1 if i in p1 else 2 for i in range(g.vcount())]
        for (p1, p2) in parity_parts
    ]

    print "Number of partitions: %d" % len(out)
    for each in out:
        print each


def init_data(fname):
    all_lines = []
    with open(fname, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        all_lines = [line for line in csvreader]

    # remove header
    lines = all_lines[1:]

    # build up an index that maps the line number to the MCD ID
    d = {}
    idx_inv = {}
    for (i, line) in enumerate(lines):
        idx_inv[i] = line[3]
        d[line[3]] = {
                       "idx": i,
                       "POP": int(line[9]),
        }

    return (d, idx_inv)


def init_graph(fname, idx_inv):
    all_lines = []
    with open(fname, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        all_lines = [line for line in csvreader]

    # remove header
    lines = all_lines[1:]

    g = igraph.Graph()

    # idx_inv should contain all of the MCD ID's as keys
    for i in sorted(idx_inv.keys()):
        g.add_vertex(idx_inv[i])

    for line in lines:
        g.add_edge(line[0], line[2])

    return g


# find potential partitionings of the graph. uses networkx's
# "all_st_cuts" to find all possible cuts betwen two nodes.
def get_partitions(g):
    # all_st_cuts only works with directed graphs
    dir = g.as_directed()
    cuts = dir.all_st_cuts(0, dir.vcount() - 1)
    return [tuple(cut.partition) for cut in cuts]


# return True or False depending on whether a particular partitioning
# scheme satisfies the population parity requirement (i.e. the
# districts should be within (max_dev) % of each other's population
def population_parity(partition, max_dev, data, idx_inv):
    (p1, p2) = partition
    s1 = float(sum([data[idx_inv[i]]["POP"] for i in p1]))
    s2 = float(sum([data[idx_inv[i]]["POP"] for i in p2]))
    if min(s1, s2) > 0:
        return abs(s1-s2)/min(s1, s2) <= max_dev
    else:
        return False


if __name__ == "__main__":
    error_msg = "Usage: %s [map_metadata_path] [map_adjacency_path]"
    assert len(sys.argv) == 3, error_msg % sys.argv[0]
    main(*sys.argv[1:])
