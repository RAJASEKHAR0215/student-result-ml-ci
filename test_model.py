import json
import unittest
import os

class TestStudentResultModel(unittest.TestCase):

    def test_metrics_file_exists(self):
        self.assertTrue(os.path.exists("metrics.json"))

    def test_accuracy_exists(self):
        with open("metrics.json") as file:
            metrics = json.load(file)

        self.assertIn("accuracy", metrics)

    def test_accuracy_range(self):
        with open("metrics.json") as file:
            accuracy = json.load(file)["accuracy"]

        self.assertGreaterEqual(accuracy, 0)
        self.assertLessEqual(accuracy, 1)

if __name__ == "__main__":
    unittest.main()
