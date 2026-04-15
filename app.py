import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random

# --- CONFIGURATION ---
st.set_page_config(page_title="Jungnickel Chapter 3 Study Guide", layout="wide")

# --- DATA: LESSONS & QUIZZES ---
study_data = {
    "3.1 Optimal Paths": {
        "explanation": """
        **For the everyday person:** Imagine you're using a GPS. It doesn't just show a map; it calculates the "best" route. 
        In graph theory, roads are 'edges' and intersections are 'vertices'. This section is about finding the path with the smallest total 'weight' (distance, time, or cost).
        
        **Interactive Tip:** Try changing the weights in a graph to see how the "best" path changes!
        """,
        "questions": [
            {"q": "What is the most common real-world application of shortest paths?", "options": ["Social Media", "Traffic or data communication networks", "Sorting lists", "Quantum physics"], "a": "Traffic or data communication networks", "r": "The text mentions motorways, railroads, and airline routes."},
            {"q": "How can you find a longest path using a shortest path algorithm?", "options": ["Double the weights", "Substitute weight w with -w", "Remove all cycles", "It is impossible"], "a": "Substitute weight w with -w", "r": "Flipping the sign turns a maximum problem into a minimum problem."},
            {"q": "What is an 'Optimal Path'?", "options": ["The longest path", "The path with the minimum total weight", "Any path between two points", "A path with no edges"], "a": "The path with the minimum total weight", "r": "Optimality refers to minimizing the sum of weights."},
            {"q": "What is 'weight' usually representing?", "options": ["Color", "Physical mass", "Cost, time, or distance", "The number of vertices"], "a": "Cost, time, or distance", "r": "These are the standard metrics for edge evaluation."},
            {"q": "A directed graph is often called a:", "options": ["Multigraph", "Digraph", "Loop", "Cycle"], "a": "Digraph", "r": "Digraph is shorthand for Directed Graph."}
        ]
    },
    "3.2 Metric Spaces": {
        "explanation": """
        **For the everyday person:** A 'Metric Space' is a world where distance makes sense. It follows the **Triangle Inequality**: 
        The direct path from A to B is always shorter than (or equal to) going from A to C then C to B. No "magic" detours allowed!
        """,
        "questions": [
            {"q": "What is the Triangle Inequality?", "options": ["a+b < c", "d(x,y) ≤ d(x,z) + d(z,y)", "d(x,y) = 0", "All angles are 60 degrees"], "a": "d(x,y) ≤ d(x,z) + d(z,y)", "r": "It means the direct distance is the shortest."},
            {"q": "If d(x,y) = 0, what must be true in a metric space?", "options": ["x = y", "x is far from y", "The graph is empty", "Weights are negative"], "a": "x = y", "r": "Distances between distinct points must be positive."},
            {"q": "The distance function d is also called a:", "options": ["Metric", "Vertex", "Weight", "Algorithm"], "a": "Metric", "r": "A metric is the mathematical function defining distance."},
            {"q": "Symmetry in a metric space means:", "options": ["d(x,y) = d(y,x)", "d(x,y) = 0", "The graph is a circle", "All weights are 1"], "a": "d(x,y) = d(y,x)", "r": "The distance from A to B is the same as B to A."},
            {"q": "Which of these is NOT a requirement for a metric space?", "options": ["Positivity", "Symmetry", "Triangle Inequality", "All weights must be even"], "a": "All weights must be even", "r": "Parity of numbers is not a metric requirement."}
        ]
    },
    "3.3 BFS": {
        "explanation": """
        **For the everyday person:** Breadth-First Search (BFS) is like a ripple in a pond. You visit all neighbors 1 step away, then 2 steps away, etc.
        **Best used when:** Every road is the exact same length (e.g., all weights = 1).
        """,
        "questions": [
            {"q": "What is the complexity of BFS?", "options": ["O(|V|)", "O(|E|)", "O(|V|^2)", "O(n!)"], "a": "O(|E|)", "r": "BFS visits each edge once."},
            {"q": "What data structure is used for BFS?", "options": ["Stack", "Queue", "Tree", "Array"], "a": "Queue", "r": "A FIFO queue ensures we visit closer vertices first."},
            {"q": "BFS finds the shortest path if:", "options": ["Weights are random", "All weights are 1", "There are no edges", "The graph is a tree"], "a": "All weights are 1", "r": "It counts the minimum number of edges."},
            {"q": "A vertex that cannot be reached has distance:", "options": ["0", "-1", "Infinity", "100"], "a": "Infinity", "r": "If the ripple never reaches it, the distance is undefined/infinite."},
            {"q": "BFS can be used to find:", "options": ["Connected components", "Maximum flow", "Negative cycles", "Vertex color"], "a": "Connected components", "r": "It explores everything reachable from a start node."}
        ]
    },
    "3.4 Bellman's Equations": {
        "explanation": "**For the everyday person:** This is a logic rule: 'The best way to get to your house is the best way to get to your street, plus the walk to your door.' We solve this for every point to find the global best.",
        "questions": [
            {"q": "Bellman's equations are used for:", "options": ["Sorting", "Shortest paths", "Coloring", "Printing"], "a": "Shortest paths", "r": "They define the dynamic programming approach to paths."},
            {"q": "These equations have a unique solution if:", "options": ["There are no negative cycles", "The graph is a cycle", "Weights are 0", "All vertices are even"], "a": "There are no negative cycles", "r": "Negative cycles allow for infinitely decreasing paths."},
            {"q": "The equation is: u_j = min(u_i + w_ij). What is u_i?", "options": ["The start", "Distance to i", "The edge weight", "The end"], "a": "Distance to i", "r": "It builds the path from previous optimal distances."},
            {"q": "This approach is the basis for:", "options": ["Dynamic programming", "Random guessing", "Sorting", "Hardware design"], "a": "Dynamic programming", "r": "Bellman is the father of dynamic programming."},
            {"q": "In a network with n vertices, we iterate at most:", "options": ["n times", "n-1 times", "2 times", "Infinity"], "a": "n-1 times", "r": "A path can have at most n-1 edges without repeating a vertex."}
        ]
    },
    "3.5 Acyclic Digraphs": {
        "explanation": "**For the everyday person:** This is a one-way map with no loops. Since you can't go in circles, finding the shortest path is super easy—you just follow the 'flow' from start to finish.",
        "questions": [
            {"q": "An 'Acyclic' graph has no:", "options": ["Edges", "Vertices", "Cycles", "Weights"], "a": "Cycles", "r": "Acyclic means 'no cycles'."},
            {"q": "To solve this quickly, we use:", "options": ["Random search", "Topological sorting", "Brute force", "BFS"], "a": "Topological sorting", "r": "Ordering vertices linearly simplifies path calculation."},
            {"q": "Shortest paths in acyclic graphs are:", "options": ["Harder to find", "Faster to find", "Impossible", "Always 0"], "a": "Faster to find", "r": "The lack of cycles removes complexity."},
            {"q": "If a graph is acyclic, its complexity is:", "options": ["O(|E|)", "O(n!)", "O(|V|^3)", "O(1)"], "a": "O(|E|)", "r": "We process each edge exactly once."},
            {"q": "Can we find the longest path in an acyclic graph?", "options": ["Yes", "No", "Only if weights are 1", "Only if it is a tree"], "a": "Yes", "r": "Acyclic structure makes both min and max paths easy to find."}
        ]
    },
    "3.6 Dijkstra's Algorithm": {
        "explanation": "**For the everyday person:** The most famous algorithm! It's like a 'greedy' explorer who always goes to the nearest unvisited town and updates his map based on what he finds there.",
        "questions": [
            {"q": "Dijkstra fails if there are:", "options": ["Positive weights", "Negative weights", "Too many edges", "No cycles"], "a": "Negative weights", "r": "Negative weights break the 'greedy' assumption."},
            {"q": "The complexity using a simple array is:", "options": ["O(|V|)", "O(|V|^2)", "O(|E|)", "O(log n)"], "a": "O(|V|^2)", "r": "Scanning the distance array takes O(|V|) each time."},
            {"q": "Dijkstra's is a _________ algorithm.", "options": ["Greedy", "Random", "Recursive", "Brute-force"], "a": "Greedy", "r": "It makes the best local choice at each step."},
            {"q": "What is updated in each step?", "options": ["The start node", "The distance estimates to neighbors", "The number of nodes", "The graph structure"], "a": "The distance estimates to neighbors", "r": "This is called 'relaxing' an edge."},
            {"q": "Dijkstra's is used for:", "options": ["Single-source shortest paths", "All-pairs shortest paths", "Sorting", "Finding cycles"], "a": "Single-source shortest paths", "r": "It starts from one 'root' node."}
        ]
    },
    "3.7 An Application": {
        "explanation": "**For the everyday person:** This section shows how graphs plan train trips. We don't just count the ride time; we also add 'wait time' at stations when you change lines.",
        "questions": [
            {"q": "Why split a station into two vertices?", "options": ["For looks", "To model transfer/waiting time", "To make the graph bigger", "It's a mistake"], "a": "To model transfer/waiting time", "r": "The edge between 'in' and 'out' represents the delay."},
            {"q": "What is a 'Time-expanded' graph?", "options": ["A graph with clock faces", "A graph where vertices include time info", "A very old graph", "A fast graph"], "a": "A graph where vertices include time info", "r": "It helps solve scheduling problems."},
            {"q": "Transport networks are usually:", "options": ["Directed", "Undirected", "Empty", "Random"], "a": "Directed", "r": "Buses and trains move in specific directions."},
            {"q": "A 'transfer edge' connects:", "options": ["Two different cities", "Two different lines at one station", "The start and end", "Nothing"], "a": "Two different lines at one station", "r": "It represents switching from one mode to another."},
            {"q": "Objective of transport optimization is usually:", "options": ["Earliest arrival", "Maximum transfers", "Longest ride", "More vertices"], "a": "Earliest arrival", "r": "Passengers want to reach their destination as fast as possible."}
        ]
    },
    "3.8 Floyd-Warshall": {
        "explanation": "**For the everyday person:** Dijkstra finds the way from ONE point to everywhere. Floyd-Warshall finds the path between EVERY possible pair of points at the same time.",
        "questions": [
            {"q": "Floyd-Warshall is used for:", "options": ["Single source", "All-pairs shortest paths", "One edge only", "Deleting nodes"], "a": "All-pairs shortest paths", "r": "It computes a matrix of all distances."},
            {"q": "What is the complexity?", "options": ["O(|V|)", "O(|V|^2)", "O(|V|^3)", "O(|E|)"], "a": "O(|V|^3)", "r": "It uses three nested loops over the vertices."},
            {"q": "Does it allow negative weights?", "options": ["Yes", "No", "Only if it's a tree", "Only for 2 nodes"], "a": "Yes", "r": "It handles negative weights, but not negative cycles."},
            {"q": "The algorithm works by considering:", "options": ["One edge at a time", "Intermediate vertices", "Only the start", "The color of nodes"], "a": "Intermediate vertices", "r": "It checks if vertex 'k' provides a shortcut between 'i' and 'j'."},
            {"q": "The output is usually a:", "options": ["List", "Queue", "Matrix", "Stack"], "a": "Matrix", "r": "A V x V matrix stores all path lengths."}
        ]
    },
    "3.9 Negative Cycles": {
        "explanation": "**For the everyday person:** A negative cycle is a 'magic loop' where every time you go around, your distance gets smaller. You'd stay in it forever! Most algorithms break if this happens.",
        "questions": [
            {"q": "What happens if a graph has a negative cycle?", "options": ["Path is 0", "Path is infinite", "Shortest path is undefined", "Dijkstra works fine"], "a": "Shortest path is undefined", "r": "You can always get a 'shorter' path by looping again."},
            {"q": "Which algorithm can detect negative cycles?", "options": ["BFS", "Bellman-Ford", "Dijkstra", "Greedy search"], "a": "Bellman-Ford", "r": "If distances keep changing after n-1 rounds, a cycle exists."},
            {"q": "A negative cycle has a total weight that is:", "options": ["> 0", "= 0", "< 0", "Even"], "a": "< 0", "r": "The sum of edge weights in the loop is negative."},
            {"q": "Negative cycles are common in:", "options": ["Road maps", "Currency arbitrage", "Family trees", "Social media"], "a": "Currency arbitrage", "r": "Trading money to end up with more than you started."},
            {"q": "If d(v) decreases in the nth iteration, we found a:", "options": ["Path", "Bridge", "Negative cycle", "Sink"], "a": "Negative cycle", "r": "In a standard graph, paths stabilize by iteration n-1."}
        ]
    },
    "3.10 Path Algebras": {
        "explanation": "**For the everyday person:** This is 'Graph Algebra'. It helps solve factory problems, like figuring out exactly how many bolts, wheels, and frames you need to build 100 cars.",
        "questions": [
            {"q": "What is a 'Gozinto graph'?", "options": ["A map of Italy", "A graph showing assembly parts", "A type of tree", "A social network"], "a": "A graph showing assembly parts", "r": "It shows which parts go into which modules."},
            {"q": "Path algebras generalize:", "options": ["Shortest path problems", "Sorting", "Image pixels", "Web browsers"], "a": "Shortest path problems", "r": "They provide a unified framework for many graph problems."},
            {"q": "In assembly, 'weight' might represent:", "options": ["Quantity of parts", "Color", "Price", "Weight in kg"], "a": "Quantity of parts", "r": "How many units of i are needed for j."},
            {"q": "The Gozinto graph must be:", "options": ["Cyclic", "Acyclic", "Red", "Empty"], "a": "Acyclic", "r": "You can't have a part be a component of itself."},
            {"q": "What mathematical structure is used here?", "options": ["Semiring", "Circle", "Square", "Prime number"], "a": "Semiring", "r": "Path algebras are built on algebraic semirings."}
        ]
    }
}

# --- APP LAYOUT ---
st.sidebar.title("📚 Jungnickel Chapter 3")
selection = st.sidebar.radio("Navigate Sections", list(study_data.keys()))

# --- CONTENT ---
data = study_data[selection]
st.title(selection)
st.markdown(data["explanation"])

# --- INTERACTIVE VISUALIZER ---
st.divider()
st.subheader("Interactive Graph Explorer")
col1, col2 = st.columns([2, 1])

with col2:
    node_count = st.slider("Number of Vertices", 3, 8, 5)
    generate = st.button("Generate New Random Graph")

# Logic to generate and find shortest path
G = nx.gnp_random_graph(node_count, 0.4, directed=True, seed=42 if not generate else random.randint(1, 100))
# CORRECTED: Using random.randint instead of nx.integer_tuple
for (u, v) in G.edges():
    G.edges[u,v]['weight'] = random.randint(1, 20)

with col1:
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=700, arrowsize=20)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    st.pyplot(fig)
    
    # Show calculation for user
    try:
        path = nx.shortest_path(G, source=0, target=node_count-1, weight='weight')
        length = nx.shortest_path_length(G, source=0, target=node_count-1, weight='weight')
        st.success(f"Shortest path from Node 0 to Node {node_count-1}: **{' → '.join(map(str, path))}** (Total Weight: {length})")
    except:
        st.warning(f"No path exists between Node 0 and Node {node_count-1}")

# --- QUIZ ---
st.divider()
st.subheader(f"Quiz: {selection}")

if f"score_{selection}" not in st.session_state:
    st.session_state[f"score_{selection}"] = 0

for i, q in enumerate(data["questions"]):
    st.write(f"**Q{i+1}: {q['q']}**")
    ans = st.radio("Choose one:", q["options"], key=f"ans_{selection}_{i}")
    if st.button(f"Check Q{i+1}", key=f"btn_{selection}_{i}"):
        if ans == q["a"]:
            st.success(f"Correct! {q['r']}")
        else:
            st.error(f"Wrong. {q['r']}")
