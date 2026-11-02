import random, time

INF = float("inf")

# ---- tiny testing helper (do not edit) ------------------------------------
RESULTS = {}

def check(task, name, test, pts=1):
    """Run test() and record whether it returned True. Exceptions count as a fail."""
    try:
        ok = bool(test())
        err = ""
    except Exception as e:
        ok, err = False, f"  ({type(e).__name__}: {e})"
    RESULTS.setdefault(task, []).append((name, ok, pts))
    print(("✅" if ok else "❌"), f"[{task}] {name} ({pts} pt){err}")

def summary():
    print(f"{'Task':<22}{'Points':>8}{'Max':>6}")
    total = mx = 0
    for task, rows in RESULTS.items():
        got = sum(p for _, ok, p in rows if ok)
        top = sum(p for _, _, p in rows)
        total += got; mx += top
        print(f"{task:<22}{got:>8}{top:>6}")
    print("-" * 36)
    print(f"{'AUTOMATIC TOTAL':<22}{total:>8}{mx:>6}")

# ---- graphs used in the lab (do not edit) ----------------------------------
V = ["S", "A", "B", "C", "D"]
E = [("S", "A", 6), ("S", "B", 3), ("B", "A", -2),
     ("A", "C", 3), ("B", "D", 7), ("C", "D", -1)]          # has a negative edge, no negative cycle

V_CYCLE = ["S", "A", "B"]
E_CYCLE = [("S", "A", 2), ("A", "B", 2), ("B", "S", -5)]    # cycle S->A->B->S costs -1

def random_graph(n, m, seed=0):
    """Random directed graph with some negative edges but NO negative cycle."""
    rnd = random.Random(seed)
    pot = [rnd.randint(0, 10) for _ in range(n)]
    edges = {}
    while len(edges) < m:
        u, v = rnd.sample(range(n), 2)
        edges[(u, v)] = rnd.randint(1, 9) + pot[u] - pot[v]
    return [(u, v, w) for (u, v), w in edges.items()]

print("Setup done.")

my_trace = {
    # 1: [0, 6, 3, INF, INF],
    # 2: [0, 1, 3, 9, 10],
    # 3: [0, 1, 3, 4, 8],
    # 4: [0, 1, 3, 4, 3],
}

def bellman_ford(vertices, edges, source):
    """Return (dist, prev, history). Raise ValueError on a reachable negative cycle."""
    dist = {v: INF for v in vertices}
    prev = {v: None for v in vertices}
    dist[source] = 0
    history = [dist.copy()]
    for _ in range(len(vertices) - 1):
        new = dist.copy()
        for a, b, w in edges:
            if dist[a] != INF and dist[a] + w < new[b]:
                new[b] = dist[a] + w
                prev[b] = a
        dist = new
        history.append(dist.copy())
    for a, b, w in edges:
        if dist[a] != INF and dist[a] + w < dist[b]:
            raise ValueError("negative cycle reachable from source")
    return dist, prev, history

def build_path(prv, target):
    """Return the list of vertices from the source to target."""
    if target not in prv:
        return []
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = prv[current]
    path.reverse()
    return path
def bellman_ford_early(vertices, edges, source):
    """Return (dist, prev, rounds). Stop after the first round with no change."""
    dist = {v: INF for v in vertices}
    prev = {v: None for v in vertices}
    dist[source] = 0
    rounds = 0
    for _ in range(len(vertices) - 1):
        new = dist.copy()
        changed = False
        for a, b, w in edges:
            if dist[a] != INF and dist[a] + w < new[b]:
                new[b] = dist[a] + w
                prev[b] = a
                changed = True
        dist = new
        rounds += 1
        if not changed:
            break
    for a, b, w in edges:
        if dist[a] != INF and dist[a] + w < dist[b]:
            raise ValueError("negative cycle reachable from source")
    return dist, prev, rounds
T = "Task 1"
expected_hist = [
    [0, INF, INF, INF, INF], [0, 6, 3, INF, INF], [0, 1, 3, 9, 10],
    [0, 1, 3, 4, 8], [0, 1, 3, 4, 3],
]
check(T, "my_trace matches d(1)…d(4)", lambda: [my_trace[k] for k in (1, 2, 3, 4)] == expected_hist[1:], 6)
check(T, "final distances are correct",
      lambda: bellman_ford(V, E, "S")[0] == {"S": 0, "A": 1, "B": 3, "C": 4, "D": 3}, 9)
check(T, "history rows d(0)…d(4) are correct",
      lambda: [[h[v] for v in V] for h in bellman_ford(V, E, "S")[2]] == expected_hist, 7)
check(T, "build_path(prev, 'D') == S,B,A,C,D",
      lambda: build_path(bellman_ford(V, E, "S")[1], "D") == ["S", "B", "A", "C", "D"], 6)
check(T, "build_path(prev, 'S') == ['S']",
      lambda: build_path(bellman_ford(V, E, "S")[1], "S") == ["S"], 2)

def _raises(fn):
    try:
        fn()
    except ValueError:
        return True
    return False

check(T, "negative cycle raises ValueError", lambda: _raises(lambda: bellman_ford(V_CYCLE, E_CYCLE, "S")), 6)

V6 = ["S", "A", "B", "C", "D", "E"]
E6 = [("S", "A", 1), ("A", "B", 1)]
check(T, "early exit: same distances", lambda: bellman_ford_early(V, E, "S")[0] == bellman_ford(V, E, "S")[0], 3)
check(T, "early exit: stops after 3 rounds on the chain graph", lambda: bellman_ford_early(V6, E6, "S")[2] == 3, 4)
check(T, "early exit: still detects negative cycle", lambda: _raises(lambda: bellman_ford_early(V_CYCLE, E_CYCLE, "S")), 2)