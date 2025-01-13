import argparse
import networkx as nx
import random

def main():
    parser = argparse.ArgumentParser(description="Generate a partial k-tree with a target width.")
    parser.add_argument("-n", "--numvertices", type=int, required=True, help="Number of vertices in the graph.")
    parser.add_argument("-s", "--seed", type=int, default=0, help="Random seed for reproducibility.")
    parser.add_argument("-r", "--remove", type=float, default=0.0, help="Probability of removing an edge.")
    parser.add_argument("-a", "--add", type=float, default=0.0, help="Probability of adding a new edge.")
    parser.add_argument("-w", "--width", type=int, required=True, help="Width of the k-tree generated before pertubation.")
    parser.add_argument("-o", "--output", type=str, required=True, help="Name of output file.")
    
    args = parser.parse_args()

    k=args.width
    n=args.numvertices
    p_add = args.add
    p_remove = args.remove

    if k < 1:
        raise ValueError("Width must be at least 1.")
    if n < k + 1:
        raise ValueError(f"Number of vertices must be at least {k + 1} for a k-tree.")

    random.seed(args.seed)

    k_cliques=[]

    for u in range(n):
        clique = [v for v in range(n) if v is not u]
        k_cliques.append(clique)

    for u in range(k+1, n):
        i = random.randint(0, len(k_cliques)-1)
        clique = k_cliques[i][:]
        j = random.randint(0, len(clique)-1)
        clique[j] = u
        k_cliques.append(clique)

    G = nx.empty_graph(n)

    for clique in k_cliques:
        for u in clique:
            for v in clique:
                if u < v:
                    G.add_edge(u, v)

    add=[]
    for u in G.nodes():
        for v in G.nodes():
            if u < v and not G.has_edge(u, v):
                if random.random() < p_add:
                    add.append((u, v))
    
    for u, v in list(G.edges()):
        if random.random() < p_remove:
            G.remove_edge(u, v)

    G.add_edges_from(add)

    with open(args.output, 'w') as f:
        f.write(f"{len(G.nodes())} {len(G.edges())}\n")
        for u, v in G.edges():
            f.write(f"{u} {v}\n")

if __name__ == "__main__":
    main()




    




