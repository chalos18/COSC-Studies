"""
Mobile agents (self driving taxis) scattered across a flat rectangular grid environment.
There are a number of call points (customers) waiting to be served.
The objective: navigate an agent to the customer that is closes in time (takes the least time to reach)

1. Navigate only one agent to only one customer (only the closest pair)
2. Search module is available on the quiz server so can import safely
3. All import statements for solution must be provided
4. I can have all 3 questions answered in one file and submit it for all 3 questions. DO NOT print anything. Use main() instead.
5. Answer the questions in order.
6. If it passes all tests, it might still be wrong, causing following questions to fail so test lots.
"""

# Question 1. RoutingGraph class

import heapq
import itertools
import math
from COSC367.graph_search import Arc, Frontier, Graph, generic_search, print_actions


class RoutingGraph(Graph):
    """
    The map is always rectangular. Positions are (row, col) starting at 0,0
    The map has a wall represenented by characters '+' or '-' or '|'. Corners are +,
    the first and last rows and first and last columns are always - and |.
    Obstacles are X
    Fuel station is F. If an agent is in F and fuel is less than 9 then take the action "Fuel up" ->
    this fills the tank to its max of 9.
        The fuel up action should appear after any other directional actions in the sequence of arcs
    Portal is P. There can be 0 or more. If an agent in in P, it has the option of teleporting
    to any other portal.
    Moving between portals is like a train or ferry.
        In the sequence of arcs, the teleport option should appear after any other directional move action
        The action costs 10 units of time
        The action label of the arc must be "Teleport to (row,col)" -> destination portal
        If multiple outgoing arcs of this type are free then they should appear in ascending order of the row/column number
        of the target portals
    There may be zero or more agents ont he map (located by S or digits 0 to 9)
        - S means solar, need no fuel
        - digits have fuel tanks, 9 is full tank. Digit means how much fuel is initially available for the agent
        - zero or more customer on the map -> potential destinations marked by G.
        - An agent is never initially on a potential destination (call points)

    Costs:
        The action of fueling up costs 15 units of time (always)
        All single horizontal/vertical moves take 5 units of time
        All single diagonal moves take 7 units of time
        Time is the cost of an action and the objective is to minimise it
        The agent can consume all of its fuel to get to the call point
    """
    def __init__(self, map_string):
        self.map = map_string.strip()
        self.map_str = map_string
        self.map_graph = []

        self.explored = []
        self.start_nodes = []
        self.goal_nodes = []
        self.portal_nodes = []

        self.filter_map(self.map_str)

    def filter_map(self, map_str):
        filter_map = (map_str.strip()).split("\n")

        for element in filter_map:
            self.map_graph.append(list(element.strip()))

        for i in range(len(self.map_graph)):
            for j in range(len(self.map_graph[i])):
                r, c = i, j
                if self.map_graph[r][c] == "S":
                    self.start_nodes.append((r, c, math.inf))
                elif self.map_graph[r][c].isdigit():
                    self.start_nodes.append((r, c, int(self.map_graph[r][c])))
                elif self.map_graph[r][c] == "G":
                    self.goal_nodes.append((r, c))
                elif self.map_graph[r][c] == "P":
                    self.portal_nodes.append((r, c))

    def is_goal(self, node):
        """Returns true if the given node is a call point, denoted by G, false otherwise."""
        node_r, node_c, _ = node
        self.explored.append((node_r, node_c))

        # Checks if the node's location is part of the list of goal nodes
        return (node_r, node_c) in self.goal_nodes

    def starting_nodes(self):
        """Returns a sequence of starting nodes. Often there is only one
        starting node but even then the function returns a sequence
        with one element. It can be implemented as an iterator if
        needed."""
        return self.start_nodes

    def outgoing_arcs(self, tail_node):
        directions = [
            ("N", -1, 0),
            ("NE", -1, 1),
            ("E", 0, 1),
            ("SE", 1, 1),
            ("S", 1, 0),
            ("SW", 1, -1),
            ("W", 0, -1),
            ("NW", -1, -1),
        ]
        horizontal_vertical = {"N", "E", "S", "W"}

        node_r, node_c, node_fuel = tail_node
        available_actions = []
        for action, dr, dc in directions:
            new_r, new_c = node_r + dr, node_c + dc

            # Check obstacle/wall
            if self.map_graph[new_r][new_c] in ["X", "|", "-", "+"]:
                continue

            # Valid move
            cost = 5 if action in horizontal_vertical else 7
            new_fuel = node_fuel - 1 if node_fuel != math.inf else math.inf

            available_actions.append(
                Arc(
                    tail=tail_node,
                    head=(new_r, new_c, new_fuel),
                    action=action,
                    cost=cost,
                )
            )

        # Fuel up action (if on fuel station and fuel less than 9)
        if self.map_graph[node_r][node_c] == "F" and node_fuel < 9:
            available_actions.append(
                Arc(
                    tail=tail_node,
                    head=(node_r, node_c, 9),
                    action="Fuel up",
                    cost=15,
                )
            )

        # Teleport actions if on portal
        if self.map_graph[node_r][node_c] == "P":
            for portal_r, portal_c in sorted(self.portal_nodes):
                if (portal_r, portal_c) != (node_r, node_c):
                    available_actions.append(
                        Arc(
                            tail=tail_node,
                            head=(portal_r, portal_c, node_fuel),
                            action=f"Teleport to {(portal_r, portal_c)}",
                            cost=10,
                        )
                    )

        return available_actions

    def estimated_cost_to_goal(self, node):
        """
        Return the admissible heuristic estimate for the cost to the closest goal.
        Movement is in 8 directions, with costs:
            - 5 for N, S, E, W
            - 7 for NE, NW, SE, SW
        """
        max_estimate = float("inf")

        for goal in self.goal_nodes:
            dx = abs(goal[0] - node[0])
            dy = abs(goal[1] - node[1])

            # Optimal strategy: use diagonal moves when possible, then straight moves
            # Manhattan distance and the Chebyshev distance
            diagonal_steps = min(dx, dy)
            straight_steps = abs(dx - dy)

            estimate = diagonal_steps * 7 + straight_steps * 5

            # For multiple goals, we want the minimum cost to ANY goal
            # if estimate < max_estimate:
            if estimate > max_estimate:
                max_estimate = estimate

        return max_estimate if max_estimate != float("inf") else 0


class AStarFrontier(Frontier):
    """
    Performing A* search on graphs will be done to find the lowest cost
    i.e shortest time solution if one exists from one of the agents to the goal node.
    """

    def __init__(self, map_graph):
        """The constructor takes a map_graph and initializes the
        container to an empty heap. We also store a set of visited nodes
        and their lowest cost seen so far.
        """
        self.map = map_graph
        self.container = []
        # Store a dictionary to keep track of the minimum cost to reach a node
        self.min_cost_to_node = {}
        self.visited = set()  # Using a set for faster lookups
        self.direction_order = {
            "N": 0,
            "NE": 1,
            "E": 2,
            "SE": 3,
            "S": 4,
            "SW": 5,
            "W": 6,
            "NW": 7,
        }

    def add(self, path):
        """
        Adds a new path to the frontier, only if it's a better path to the node.
        """
        head = path[-1].head
        total_cost = sum(arc.cost for arc in path)

        # Pruning check: Don't add if we've already found a cheaper path
        # if head in self.min_cost_to_node and total_cost >= self.min_cost_to_node[head]:
        #     return

        # self.min_cost_to_node[head] = total_cost

        last_node_estimate = self.map.estimated_cost_to_goal(head)

        # The priority is the total cost (g) plus the heuristic estimate (h)
        priority = total_cost + last_node_estimate

        # Determine direction for tie-breaking
        if len(path) > 1:
            first_move = path[1].action
        else:
            first_move = None
        direction_index = self.direction_order.get(first_move, 99)

        # Push the path to the heap
        heapq.heappush(self.container, (priority, direction_index, path))

    def __iter__(self):
        return self

    def __next__(self):
        """
        Selects, removes, and returns a path on the frontier.
        This method will handle the pruning of already processed nodes.
        """
        while self.container:
            _, _, path = heapq.heappop(self.container)
            head = path[-1].head

            # Pruning check: Only return paths to nodes that haven't been visited yet
            if head not in self.visited:
                self.visited.add(head)
                return path

        raise StopIteration


def print_map(map_graph, frontier, solution):
    # Make a mutable copy of the map
    path_map = [list(row) for row in map_graph.map_graph]

    # Mark solution path
    if solution:
        for selected_path in solution:
            r, c = selected_path.head[0], selected_path.head[1]
            if path_map[r][c] not in ["S", "G"]:
                path_map[r][c] = "*"

    for available_path in frontier.visited:
        r, c = available_path[0], available_path[1]
        if path_map[r][c] not in ["S", "G", "*"]:
            path_map[r][c] = "."

    for map_line in path_map:
        map_line = "".join(map_line)
        print(map_line)


def main():
    "--------------------------------------------------------------------------------------"
    """Question 3"""

    # map_str = """\
    # +----------------+
    # |                |
    # |                |
    # |                |
    # |                |
    # |                |
    # |                |
    # |        S       |
    # |                |
    # |                |
    # |     G          |
    # |                |
    # |                |
    # |                |
    # +----------------+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_map(map_graph, frontier, solution)

    # map_str = """\
    # +----------------+
    # |                |
    # |                |
    # |                |
    # |                |
    # |                |
    # |                |
    # |        S       |
    # |                |
    # |                |
    # |     G          |
    # |                |
    # |                |
    # |                |
    # +----------------+
    # """

    # map_graph = RoutingGraph(map_str)
    # # changing the heuristic so the search behaves like LCFS
    # map_graph.estimated_cost_to_goal = lambda node: 0

    # frontier = AStarFrontier(map_graph)

    # solution = next(generic_search(map_graph, frontier), None)
    # print_map(map_graph, frontier, solution)

    map_str = """\
    +-------------+
    | G         G |
    |      S      |
    | G         G |
    +-------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    # map_str = """\
    # +-------+
    # |     XG|
    # |X XXX  |
    # |  S    |
    # +-------+
    # """
    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_map(map_graph, frontier, solution)

    # map_str = """\
    # +--+
    # |GS|
    # +--+
    # """
    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_map(map_graph, frontier, solution)

    # map_str = """\
    # +----+
    # |    |
    # | SX |
    # | X G|
    # +----+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_map(map_graph, frontier, solution)

    # map_str = """\
    # +---------------+
    # |    G          |
    # |XXXXXXXXXXXX   |
    # |           X   |
    # |  XXXXXX   X   |
    # |  X S  X   X   |
    # |  X        X   |
    # |  XXXXXXXXXX   |
    # |               |
    # +---------------+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_map(map_graph, frontier, solution)

    # map_str = """\
    # +---------+
    # |         |
    # |    G    |
    # |         |
    # +---------+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_map(map_graph, frontier, solution)
    "--------------------------------------------------------------------------------------"
    """Question 2"""

    # map_str = """\
    # +-------+
    # |   G   |
    # |       |
    # |   S   |
    # +-------+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_actions(solution)

    # map_str = """\
    # +-------+
    # |  GG   |
    # |S    G |
    # |  S    |
    # +-------+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_actions(solution)

    # map_str = """\
    # +-------+
    # |     XG|
    # |X XXX  |
    # | S     |
    # +-------+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_actions(solution)

    # map_str = """\
    # +-------+
    # |  F  X |
    # |X XXXXG|
    # | 3     |
    # +-------+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_actions(solution)

    # map_str = """\
    # +--+
    # |GS|
    # +--+
    # """
    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_actions(solution)

    # map_str = """\
    # +---+
    # |GF2|
    # +---+
    # """
    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_actions(solution)

    # map_str = """\
    # +----+
    # | S  |
    # | SX |
    # |GX G|
    # +----+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_actions(solution)

    # map_str = """\
    # +------------+
    # |    P       |
    # | 5          |
    # |XXXXXXXXX   |
    # |  P G       |
    # +------------+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_actions(solution)

    # map_str = """\
    # +---------+
    # |         |
    # |    G    |
    # |         |
    # +---------+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_actions(solution)

    # map_str = """\
    # +------------+
    # |    P       |
    # | 7          |
    # |XXXXXXXXX   |
    # |P F X  G    |
    # +------------+
    # """

    # map_graph = RoutingGraph(map_str)
    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_actions(solution)

    "--------------------------------------------------------------------------------------"

    """Question 1"""

    # map_str = """\
    # +-------+
    # | G   G |
    # |   S   |
    # | G   G |
    # +-------+
    # """

    # map_graph = RoutingGraph(map_str)
    # print("Starting nodes:", sorted(map_graph.starting_nodes()))
    # print("Outgoing arcs (available actions) at starting states:")
    # for s in sorted(map_graph.starting_nodes()):
    #     print(s)
    #     for arc in map_graph.outgoing_arcs(s):
    #         print("  " + str(arc))

    # frontier = AStarFrontier(map_graph)
    # solution = next(generic_search(map_graph, frontier), None)
    # print_actions(solution)

    # map_str = """\
    # +-------+
    # |  9  XG|
    # |X XXX P|
    # | S  0FG|
    # |XX P XX|
    # +-------+
    # """

    # graph = RoutingGraph(map_str)

    # print("Starting nodes:", sorted(graph.starting_nodes()))
    # print("Outgoing arcs (available actions) at starting states:")
    # for s in sorted(graph.starting_nodes()):
    #     print(s)
    #     for arc in graph.outgoing_arcs(s):
    #         print("  " + str(arc))

    # node = (1, 1, 5)
    # print("\nIs {} goal?".format(node), graph.is_goal(node)) # False
    # print("Outgoing arcs (available actions) at {}:".format(node))
    # for arc in graph.outgoing_arcs(node):
    #     print("  " + str(arc))

    # node = (1, 7, 2)
    # print("\nIs {} goal?".format(node), graph.is_goal(node))  # True
    # print("Outgoing arcs (available actions) at {}:".format(node))
    # for arc in graph.outgoing_arcs(node):
    #     print("  " + str(arc))

    # node = (3, 7, 0)
    # print("\nIs {} goal?".format(node), graph.is_goal(node))  # True

    # node = (3, 7, math.inf)
    # print("\nIs {} goal?".format(node), graph.is_goal(node))  # True

    # node = (3, 6, 5)
    # print("\nIs {} goal?".format(node), graph.is_goal(node))  # False
    # print("Outgoing arcs (available actions) at {}:".format(node))
    # for arc in graph.outgoing_arcs(node):
    #     print("  " + str(arc))

    # node = (3, 6, 9)
    # print("\nIs {} goal?".format(node), graph.is_goal(node))
    # print("Outgoing arcs (available actions) at {}:".format(node))
    # for arc in graph.outgoing_arcs(node):
    #     print("  " + str(arc))

    # node = (2, 7, 4)  # at a location with a portal
    # print("\nOutgoing arcs (available actions) at {}:".format(node))
    # for arc in graph.outgoing_arcs(node):
    #     print("  " + str(arc))

    "--------------------------------------------------------------------------------------"

    # map_str = """\
    # +--+
    # |GS|
    # +--+
    # """

    # graph = RoutingGraph(map_str)

    # print("Starting nodes:", sorted(graph.starting_nodes()))
    # print("Outgoing arcs (available actions) at the start:")
    # for start in graph.starting_nodes():
    #     for arc in graph.outgoing_arcs(start):
    #         print("  " + str(arc))

    # node = (1, 1, 1)
    # print("\nIs {} goal?".format(node), graph.is_goal(node))
    # print("Outgoing arcs (available actions) at {}:".format(node))
    # for arc in graph.outgoing_arcs(node):
    #     print("  " + str(arc))

    "---------------------------------------------------------------------------------------"

    # map_str = """\
    # +------+
    # |S    S|
    # |  GXXX|
    # |S     |
    # +------+
    # """

    # graph = RoutingGraph(map_str)
    # print("Starting nodes:", sorted(graph.starting_nodes()))


if __name__ == "__main__":
    main()
