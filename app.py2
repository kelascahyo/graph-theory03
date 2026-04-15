import streamlit as st

# Set page config
st.set_page_config(page_title="Jungnickel Chapter 3 Study Guide", layout="wide")

# --- APP NAVIGATION ---
st.sidebar.title("Chapter 3 Sections")
section = st.sidebar.radio("Go to:", [
    "Introduction & 3.1", "3.2 Metric Spaces", "3.3 BFS", "3.4 Bellman's Equations", 
    "3.5 Acyclic Digraphs", "3.6 Dijkstra's Algorithm", "3.7 An Application", 
    "3.8 Floyd-Warshall", "3.9 Cycles of Negative Length", "3.10 Path Algebras"
])

# --- HELPER FUNCTION FOR QUIZZES ---
def run_quiz(questions, section_key):
    st.subheader("Section Quiz")
    score = 0
    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}: {q['question']}**")
        # Use a unique key for each radio button to prevent state issues
        user_choice = st.radio(f"Select option for Q{i+1}", q['options'], key=f"{section_key}_{i}")
        
        if st.button(f"Submit Q{i+1}", key=f"btn_{section_key}_{i}"):
            if user_choice == q['answer']:
                st.success(f"Correct! {q['reason']}")
                score += 1
            else:
                st.error(f"Incorrect. {q['reason']}")
    st.write(f"**Current Score for this section: {score}/{len(questions)}**")

# --- CONTENT SECTIONS ---

if section == "Introduction & 3.1":
    st.header("3.1 Optimal Paths")
    st.markdown("""
    **Explanation for Everyone:** Graphs are used every day in things like Google Maps or bus routes. Chapter 3 looks at how we find the "best" way to get from point A to point B[cite: 263, 264]. 
    "Best" usually means the **shortest** distance, but it could also mean the **fastest** time or the **cheapest** cost[cite: 266].
    
    **Key Concept:** To find the longest path, we can sometimes just flip the numbers (make them negative) and look for the shortest path, but this only works if there aren't any weird "negative cycles" that make the path infinitely short[cite: 278, 279].
    """)
    
    q31 = [
        {"question": "What is the most common real-world application of shortest paths mentioned?", "options": ["Social Media", "Traffic or data communication networks", "Sorting lists", "Quantum physics"], "answer": "Traffic or data communication networks", "reason": "The text explicitly mentions motorways, railroads, and airline routes as graphs[cite: 264]."},
        {"question": "How can you find a longest path using a shortest path algorithm?", "options": ["By doubling the weights", "By substituting weight w with -w", "By removing all cycles", "It is impossible"], "answer": "By substituting weight w with -w", "reason": "Flipping the sign of the weights allows a shortest path algorithm to find what was originally the longest path[cite: 278]."}
    ]
    run_quiz(q31, "s31")

elif section == "3.2 Metric Spaces":
    st.header("3.2 Metric Spaces and Valuations")
    st.markdown("""
    **Explanation for Everyone:** A "Metric Space" is just a fancy way of saying a place where distance follows specific rules, like: 
    1. The distance from A to B is the same as B to A.
    2. The shortest distance between two points is a straight line (the triangle inequality)[cite: 294, 298].
    """)
    q32 = [{"question": "What rule must distances in a metric space follow regarding three points a, b, and c?", "options": ["d(a,b) > d(a,c) + d(c,b)", "d(a,b) <= d(a,c) + d(c,b)", "d(a,b) = d(a,c)", "d(a,b) = 0"], "answer": "d(a,b) <= d(a,c) + d(c,b)", "reason": "This is the triangle inequality, essential for valid distance metrics[cite: 294]."} for _ in range(1)]
    run_quiz(q32, "s32")

elif section == "3.3 BFS":
    st.header("3.3 Breadth First Search (BFS)")
    st.markdown("""
    **Explanation for Everyone:** Imagine dropping a pebble in a pond—the ripples move outward in circles. BFS works like that. It checks all immediate neighbors first, then neighbors of neighbors, until it finds the target[cite: 309]. It's perfect for finding the shortest path when every "step" is the same length.
    """)
    q33 = [{"question": "What can BFS be used to determine in a graph?", "options": ["The heaviest edge", "Connected components", "The alphabet size", "The total number of cycles"], "answer": "Connected components", "reason": "BFS can explore all reachable vertices from a starting point to identify a component[cite: 310]."} for _ in range(1)]
    run_quiz(q33, "s33")

elif section == "3.4 Bellman's Equations":
    st.header("3.4 Bellman's Equations")
    st.markdown("""
    **Explanation for Everyone:** This is a mathematical rule that says: "The shortest path to point J is the shortest path to some neighbor I, plus the distance from I to J"[cite: 328]. If you solve these equations for every point, you get the shortest path to everywhere.
    """)
    q34 = [{"question": "Bellman's equations have a unique solution if the network contains:", "options": ["Only negative cycles", "Only positive cycles", "No edges", "Only loops"], "answer": "Only positive cycles", "reason": "If there are no negative cycles, there is a unique set of shortest distances[cite: 323]."} for _ in range(1)]
    run_quiz(q34, "s34")

elif section == "3.5 Acyclic Digraphs":
    st.header("3.5 Shortest Paths in Acyclic Digraphs")
    st.markdown("""
    **Explanation for Everyone:** An "Acyclic Digraph" is a one-way map with no loops. Because you can never go back to where you started, solving for the shortest path is extremely fast and easy—you just follow the flow from start to finish[cite: 325, 328].
    """)
    q35 = [{"question": "What is an acyclic digraph?", "options": ["A graph with only one vertex", "A directed graph with no cycles", "A graph where every vertex is even", "A graph used only for bus routes"], "answer": "A directed graph with no cycles", "reason": "The term 'acyclic' literally means without cycles[cite: 325]."} for _ in range(1)]
    run_quiz(q35, "s35")

elif section == "3.6 Dijkstra's Algorithm":
    st.header("3.6 The Algorithm of Dijkstra")
    st.markdown("""
    **Explanation for Everyone:** Dijkstra is the "Superstar" of shortest path algorithms. It always picks the closest "unvisited" spot and updates the distances to its neighbors[cite: 351, 359]. 
    **Important:** It only works if all the paths have positive lengths (no "shortcuts" that actually give you money back!)[cite: 354, 375].
    """)
    q36 = [{"question": "What is the complexity of Dijkstra's algorithm as described in Theorem 3.6.2?", "options": ["O(|V|)", "O(|V|^2)", "O(|E|)", "O(n!)"], "answer": "O(|V|^2)", "reason": "The standard implementation mentioned has a complexity of O(|V|^2)[cite: 361]."} for _ in range(1)]
    run_quiz(q36, "s36")

elif section == "3.7 An Application":
    st.header("3.7 An Application: Optimal Connections")
    st.markdown("""
    **Explanation for Everyone:** This section applies graph theory to public transport. It shows how to build a graph that includes not just the distance of the train ride, but also the **waiting time** when you change lines[cite: 441, 445].
    """)
    q37 = [{"question": "In the transport application, why are two vertices (in and out) used for each station/line pair?", "options": ["To double the distance", "To account for waiting times during changes", "To represent passengers", "It is a mistake in the book"], "answer": "To account for waiting times during changes", "reason": "The 'in' and 'out' vertices allow the algorithm to weigh the transfer time between lines[cite: 442, 445]."} for _ in range(1)]
    run_quiz(q37, "s37")

elif section == "3.8 Floyd-Warshall":
    st.header("3.8 The Algorithm of Floyd-Warshall")
    st.markdown("""
    **Explanation for Everyone:** While Dijkstra finds the distance from *one* point to everywhere else, Floyd-Warshall finds the distance between **every possible pair** of points at the same time[cite: 500]. It also helps find the "center" of a network—the most convenient place to be[cite: 465, 466].
    """)
    q38 = [{"question": "What does the Floyd-Warshall algorithm calculate?", "options": ["The shortest path from a root only", "The shortest path between all pairs of vertices", "Only negative cycles", "The number of vertices"], "answer": "The shortest path between all pairs of vertices", "reason": "It is an all-pairs shortest path algorithm[cite: 500]."} for _ in range(1)]
    run_quiz(q38, "s38")

elif section == "3.9 Cycles of Negative Length":
    st.header("3.9 Cycles of Negative Length")
    st.markdown("""
    **Explanation for Everyone:** A negative cycle is like a "infinite money glitch" in a game. If you can keep going in a circle and the distance keeps getting smaller, there is no "shortest" path because you could just keep going forever[cite: 279, 499].
    """)
    q32 = [{"question": "What happens if a network contains a negative cycle?", "options": ["Shortest paths become infinitely long", "Shortest paths are no longer well-defined", "The graph disappears", "Dijkstra's algorithm works faster"], "answer": "Shortest paths are no longer well-defined", "reason": "One could keep traversing the negative cycle to decrease the path length indefinitely[cite: 279, 500]."} for _ in range(1)]
    run_quiz(q32, "s39")

elif section == "3.10 Path Algebras":
    st.header("3.10 Path Algebras")
    st.markdown("""
    **Explanation for Everyone:** This is an advanced way of looking at graphs using algebra. It helps solve real-world assembly problems, like a "Gozinto graph," which shows exactly how many parts you need to build a finished product (e.g., 4 wheels and 1 body to make 1 car)[cite: 512, 513].
    """)
    q310 = [{"question": "What is a 'Gozinto graph' used for?", "options": ["Finding bus routes", "Modeling assembly lines and parts requirements", "Social networking", "Weather forecasting"], "answer": "Modeling assembly lines and parts requirements", "reason": "It identifies how many parts and modules are needed for a finished product[cite: 512, 513]."} for _ in range(1)]
    run_quiz(q310, "s310")
