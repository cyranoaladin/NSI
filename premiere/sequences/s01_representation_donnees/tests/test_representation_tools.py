import importlib.util
import pathlib
import sys
import unittest

MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / "python" / "representation_tools.py"

spec = importlib.util.spec_from_file_location("representation_tools", MODULE_PATH)
representation_tools = importlib.util.module_from_spec(spec)
sys.modules["representation_tools"] = representation_tools
spec.loader.exec_module(representation_tools)  # type: ignore[attr-defined]


class TestRepresentationTools(unittest.TestCase):
    def test_base_conversions(self):
        self.assertEqual(representation_tools.to_base(42, 2), "101010")
        self.assertEqual(representation_tools.to_base(255, 16), "FF")
        self.assertEqual(representation_tools.from_base("101010", 2), 42)
        self.assertEqual(representation_tools.from_base("FF", 16), 255)

    def test_twos_complement(self):
        self.assertEqual(representation_tools.encode_twos_complement(-1, 8), "11111111")
        self.assertEqual(representation_tools.encode_twos_complement(-5, 8), "11111011")
        self.assertEqual(representation_tools.decode_twos_complement("11111011"), -5)
        self.assertEqual(representation_tools.decode_twos_complement("00000101"), 5)

    def test_truth_table_and_unicode(self):
        xor = lambda a, b: (a and not b) or (b and not a)
        table = representation_tools.truth_table_binary(xor)
        self.assertEqual(len(table), 4)
        self.assertEqual([row["result"] for row in table], [False, True, True, False])
        self.assertEqual(representation_tools.unicode_codepoints("Aé"), [65, 233])

    def test_choose_container(self):
        self.assertEqual(representation_tools.choose_container(True, False, False), "list")
        self.assertEqual(representation_tools.choose_container(True, False, True), "tuple")
        self.assertEqual(representation_tools.choose_container(False, True, False), "dict")


if __name__ == "__main__":
    unittest.main()
