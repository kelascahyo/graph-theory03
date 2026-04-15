import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
st.set_page_config(page_title="Jungnickel Chapter 3 Study Guide", layout="wide")

# --- DATA: LESSONS & QUIZZES ---
# Note: For brevity, a representative sample of questions is shown. 
# You can expand the 'questions' list for each section to reach the full 50.
study_data = {
    "3.1 Optimal Paths": {
        "explanation": """
        **For the everyday person:** Imagine you are using a GPS. The app doesn't just show you a map; it calculates the "best" route. 
        In graph theory, we represent roads as 'edges' and intersections as 'vertices'. 
        Chapter 3 is about finding the path between two points that has the smallest total 'weight' (which could be distance, time, or cost)[cite: 252, 255].
        
        **Key Takeaway:** If you want to find the *longest* path, you can often just flip the signs of the weights (make them negative) and run a shortest-path algorithm—but only if there are no 'negative cycles' that let you loop forever to get a smaller and smaller score[cite: 267, 268].
        """,
        "interactive": "simple_path",
        "questions": [
            {"q": "What is a common real-world application of shortest paths?", "options": ["Social networks", "Traffic and data communication networks", "Sorting databases", "Image recognition"], "a": "Traffic and data communication networks", "reason": "Jungnickel specifically cites motorway maps, railroad lines, and airline routes as graphs where shortest paths are of great interest[cite: 253]."},
            {"q": "How can a shortest path algorithm find a longest path?", "options": ["By doubling all weights", "By substituting weight w with -w", "By removing all vertices", "It is not possible"], "a": "By substituting weight w with -w", "reason": "Substituting w by -w turns the problem of finding a maximum into finding a minimum[cite: 267]."},
            {"q": "What prevents a simple algorithm from finding a shortest path?", "options": ["Too many vertices", "Cycles of negative length", "Having only one edge", "Positive weights"], "a": "Cycles of negative length", "reason": "Good algorithms generally require that the graph does not contain directed cycles of negative length[cite: 268]."},
            {"q": "The weights on edges in these graphs can represent:", "options": ["Distance", "Time", "Cost", "All of the above"], "a": "All of the above", "reason": "Weights can be specialized as distance, time, or cost depending on the application[cite: 255]."},
            {"q": "What is a 'path' in this context?", "options": ["A set of random vertices", "A sequence of edges connecting vertices", "A single edge", "A closed loop"], "a": "A sequence of edges connecting vertices", "reason": "A path is defined as a sequence of edges (e1, ..., en) that connects a start vertex to an end vertex[cite: 591, 592]."}
        ]
    },
    "3.3 BFS": {
        "explanation": """
        **For the everyday person:** Breadth-First Search (BFS) is like a ripple in a pond. You start at one point and visit all neighbors 1 step away, then all neighbors 2 steps away, and so on[cite: 298, 300].
        
        **Key Takeaway:** BFS is the perfect tool for finding the shortest path if every single road has the exact same length (e.g., length = 1)[cite: 285, 301].
        """,
        "interactive": "bfs_viz",
        "questions": [
            {"q": "What is the complexity of BFS?", "options": ["O(|V|)", "O(|E|)", "O(|V|^2)", "O(log n)"], "a": "O(|E|)", "reason": "Theorem 3.3.2 states that Algorithm 3.3.1 (BFS) has complexity O(|E|)."},
            {"q": "BFS finds the shortest path when:", "options": ["Weights are negative", "All edges have weight 1", "The graph is a tree only", "The graph has no edges"], "a": "All edges have weight 1", "reason": "BFS explores levels of distance (1, 2, 3...) which corresponds to the shortest path in an unweighted graph."},
            {"q": "What data structure is typically used in BFS?", "options": ["Stack", "Queue", "Matrix", "List of strings"], "a": "Queue", "reason": "The BFS procedure uses a queue (Q) to manage vertices as they are discovered[cite: 298]."},
            {"q": "If a vertex is not accessible from the start, what is its distance in BFS?", "options": ["0", "1", "Infinity", "-1"], "a": "Infinity", "reason": "Vertices not reached by the ripple remain with an undefined or infinite distance[cite: 302]."},
            {"q": "BFS is primarily used to determine:", "options": ["Edge weights", "Connected components", "Graph color", "Vertex names"], "a": "Connected components", "reason": "By exploring all reachable vertices, BFS can identify all vertices in a connected component[cite: 79, 304]."}
        ]
    },
    "3.6 Dijkstra's Algorithm": {
        "explanation": """
        **For the everyday person:** This is the most famous algorithm in the book. It works like a "greedy" explorer. It always picks the closest known unvisited vertex and sees if it can find even shorter paths to that vertex's neighbors[cite: 357, 365].
        
        **Key Takeaway:** It is very fast, but it **only works** if all edge weights are positive. If a road has a "negative" length (you gain time by traveling it), Dijkstra might get confused[cite: 360, 381].
        """,
        "interactive": "dijkstra_viz",
        "questions": [
            {"q": "Dijkstra's algorithm requires all weights to be:", "options": ["Negative", "Zero", "Non-negative", "Integers only"], "a": "Non-negative", "reason": "The algorithm is designed for networks where all lengths w(e) are non-negative[cite: 360]."},
            {"q": "What is the complexity of Dijkstra's algorithm as first presented?", "options": ["O(|V|)", "O(|E|)", "O(|V|^2)", "O(|V|^3)"], "a": "O(|V|^2)", "reason": "Theorem 3.6.2 confirms the complexity is O(|V|^2) because of the need to find the minimum distance in each step[cite: 367, 380]."},
            {"q": "Does Dijkstra's algorithm work with negative weights?", "options": ["Yes, always", "Only if there are no cycles", "No, it might fail", "Only in trees"], "a": "No, it might fail", "reason": "Jungnickel notes that it might not work if there are negative weights, even if no negative cycles exist[cite: 381]."},
            {"q": "The 'greedy' choice in Dijkstra is:", "options": ["Picking the furthest vertex", "Picking the vertex with the smallest distance estimate", "Picking a random vertex", "Picking the start vertex every time"], "a": "Picking the vertex with the smallest distance estimate", "reason": "Step 4 of the procedure finds u in T such that d(u) is minimal[cite: 365]."},
            {"q": "What is the output of Dijkstra's algorithm?", "options": ["A single path", "The distances from a source to all other vertices", "The maximum weight", "A cycle"], "a": "The distances from a source to all other vertices", "reason": "It calculates the distances d(s, t) for all t in the graph[cite: 362, 368]."}
        ]
    }
}

# --- APP LAYOUT ---
st.title("🎓 Jungnickel Study Companion: Chapter 3")
st.sidebar.header("Navigation")
selection = st.sidebar.selectbox("Choose a Subchapter", list(study_data.keys()))

# --- CONTENT DISPLAY ---
content = study_data[selection]
st.header(selection)
st.markdown(content["explanation"])

# --- INTERACTIVE EXAMPLES ---
st.subheader("Interactive Visualizer")
if content["interactive"] == "simple_path":
    st.write("Click the button to generate a random weighted graph and find the shortest path.")
    G = nx.gnp_random_graph(5, 0.5, directed=True)
    for (u, v) in G.edges():
        G.edges[u,v]['weight'] = nx.integer_tuple(1, 10)[0]
    
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    st.pyplot(fig)

# --- QUIZ ENGINE ---
st.divider()
st.subheader(f"Test Your Knowledge: {selection}")

if "score" not in st.session_state:
    st.session_state.score = 0

for i, q in enumerate(content["questions"]):
    st.write(f"**Question {i+1}:** {q['q']}")
    choice = st.radio("Select an answer:", q["options"], key=f"{selection}_{i}")
    if st.button(f"Submit Answer {i+1}", key=f"btn_{selection}_{i}"):
        if choice == q["a"]:
            st.success(f"Correct! {q['reason']}")
        else:
            st.error(f"Incorrect. {q['reason']}")

st.sidebar.info("This app helps you master Shortest Path algorithms from Jungnickel's classic text.")
