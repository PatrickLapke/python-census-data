import simd_age
import unittest


class TestSIMD_Data(unittest.TestCase):
    def test_regions(self):
        data = simd_age.SIMD_Data("SIMD_2020v2csv.csv")
        data.load()
        self.assertIsNotNone(data.regions())
        self.assertIn("Lower Deeside", data.regions())

    def test_lowest_simd(self):
        data = simd_age.SIMD_Data("SIMD_2020v2csv.csv")
        data.load()
        self.assertEqual(data.lowest_simd(), "Canal")
        

if __name__ == "__main__":
    unittest.main()