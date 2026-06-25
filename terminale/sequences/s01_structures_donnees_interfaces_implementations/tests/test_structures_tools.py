import importlib.util
import pathlib
import sys
import unittest

MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / "python" / "structures_tools.py"

spec = importlib.util.spec_from_file_location("structures_tools", MODULE_PATH)
structures_tools = importlib.util.module_from_spec(spec)
sys.modules["structures_tools"] = structures_tools
spec.loader.exec_module(structures_tools)  # type: ignore[attr-defined]


class TestStructuresTools(unittest.TestCase):
    def test_stack_lifo(self):
        stack = structures_tools.Stack[int]()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

    def test_queue_fifo(self):
        queue = structures_tools.Queue[str]()
        queue.enqueue("A")
        queue.enqueue("B")
        self.assertEqual(queue.dequeue(), "A")
        self.assertEqual(queue.dequeue(), "B")
        self.assertTrue(queue.is_empty())

    def test_graph_representations(self):
        graph = structures_tools.adjacency_list_from_edges([("A", "B"), ("A", "C")])
        self.assertEqual(graph["A"], ["B", "C"])
        nodes = ["A", "B", "C"]
        matrix = structures_tools.adjacency_matrix(graph, nodes)
        self.assertEqual(matrix, [[0, 1, 1], [1, 0, 0], [1, 0, 0]])
        self.assertEqual(structures_tools.graph_from_matrix(matrix, nodes), graph)

    def test_bfs_path(self):
        graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
        self.assertEqual(structures_tools.bfs_path(graph, "A", "D"), ["A", "B", "D"])
        self.assertEqual(structures_tools.bfs_path(graph, "D", "A"), [])


if __name__ == "__main__":
    unittest.main()
