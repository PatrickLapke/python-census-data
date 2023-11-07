import simd_age
import unittest


class TestCensusData(unittest.TestCase):
    def test_regions(self):
        data = simd_age.CensusData("DC1117SC.csv")
        data.load()
        self.assertIsNotNone(data.regions())
        self.assertIn("Scotland", data.regions())
    
    def test_total_population(self):
        data = simd_age.CensusData("DC1117SC.csv")
        data.load()
        self.assertEqual(data.total_population("Abbey", 1), 198)
        self.assertEqual(data.total_population("West Mainland", 0), 44)


if __name__ == "__main__":
    unittest.main()
    
    







