# Partial k-tree Generator

This script generates a partial k-tree with a specified number of vertices and perturbations (edge additions and removals). It uses NetworkX to generate and manipulate the graph, and outputs the graph in a simple format that can be saved to a file.

## Prerequisites

Before running the script, make sure you have Python and the necessary packages installed:

- **Python 3.x** (preferably 3.6 or higher)
- **NetworkX**: Install it via `pip install networkx`

## Script Overview

This script generates a partial k-tree, which is a graph where every subset of `k+1` vertices forms a clique. The user can also perturb the graph by adding or removing edges with a specified probability. The resulting graph is saved in a `.txt` format that lists the edges.

## Usage

To run the script, use the following command in your terminal:

```bash
python generate_k_tree.py -n NUM_VERTICES -w WIDTH -o OUTPUT_FILE [-s SEED] [-r REMOVE_PROBABILITY] [-a ADD_PROBABILITY]
```

### Parameters

- `-n, --numvertices`: **Required**  
  The number of vertices in the generated graph (must be at least `k+1`).
  
- `-w, --width`: **Required**  
  The width `k` of the k-tree before perturbation. This determines the size of the cliques.

- `-o, --output`: **Required**  
  The output file where the graph will be saved. The format will be a plain text file containing the list of edges.

- `-s, --seed`: **Optional**  
  Random seed for reproducibility of results. If not provided, the script uses the default seed (`0`).

- `-r, --remove`: **Optional**  
  Probability of removing an edge from the graph. A float value between `0.0` and `1.0` (default: `0.0`).

- `-a, --add`: **Optional**  
  Probability of adding an edge to the graph. A float value between `0.0` and `1.0` (default: `0.0`).

## Example

### Example 1: Basic usage with default values

```bash
python generate_k_tree.py -n 10 -w 3 -o graph_output.txt
```

This generates a k-tree with 10 vertices and a width of 3, and saves it to `graph_output.txt`.

### Example 2: Adding and removing edges with a seed

```bash
python generate_k_tree.py -n 15 -w 4 -o perturbed_graph.txt -s 42 -r 0.2 -a 0.3
```

This generates a k-tree with 15 vertices, a width of 4, a random seed of `42`, a 20% chance of removing edges, and a 30% chance of adding edges. The graph will be saved to `perturbed_graph.txt`.

## Output Format

The script outputs a simple text file where the first line contains the number of vertices and edges, followed by each edge in the format:

```
NUM_VERTICES NUM_EDGES
u v
u v
...
```

### Example output:
```
10 25
0 1
0 2
1 2
1 3
...
```

## Notes

- The number of vertices (`n`) must be at least `k+1` because a k-tree requires at least `k+1` vertices to form a clique.
- The script assumes that the graph is undirected. If you need to work with directed graphs or weighted graphs, further modifications are required.
- The probabilities for adding and removing edges are floats between 0.0 and 1.0. A value of `0.0` means no edges will be added or removed, and `1.0` means all possible edges will be added or removed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

