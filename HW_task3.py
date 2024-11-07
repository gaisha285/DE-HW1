import math
import unittest

def convert_time_to_cyclic(hour):
    """
    Converts a given hour (0-24) to its sine and cosine cyclic representation.
    """
    radians = (hour % 24) * 2 * math.pi / 24  # Convert hour to radians
    sine_component = math.sin(radians)
    cosine_component = math.cos(radians)
    return sine_component, cosine_component

def calculate_cyclic_time_difference(hour1, hour2):
    """
    Calculates the cyclic difference between two times represented in hours (0-24).
    """
    sine1, cosine1 = convert_time_to_cyclic(hour1)
    sine2, cosine2 = convert_time_to_cyclic(hour2)
    # Calculate Euclidean distance between the points on the unit circle
    return math.sqrt((sine2 - sine1) ** 2 + (cosine2 - cosine1) ** 2)

# Unit Test
class TestCyclicTimeRepresentation(unittest.TestCase):

    def test_convert_time_to_cyclic(self):
        """Test that cyclic transformation returns values within -1 and 1."""
        for hour in range(0, 24):
            sine, cosine = convert_time_to_cyclic(hour)
            self.assertTrue(-1 <= sine <= 1)
            self.assertTrue(-1 <= cosine <= 1)

    def test_same_time_difference(self):
        """Test that the difference between the same times is zero."""
        self.assertAlmostEqual(calculate_cyclic_time_difference(5, 5), 0, places=5)
        self.assertAlmostEqual(calculate_cyclic_time_difference(0, 0), 0, places=5)

    def test_midnight_cross_difference(self):
        """Test for times across midnight (e.g., 23:00 and 01:00) to verify small differences."""
        # Expect a small difference because they are only 2 hours apart
        diff = calculate_cyclic_time_difference(23, 1)
        expected_diff = calculate_cyclic_time_difference(0, 2)  # Should match a 2-hour difference
        self.assertAlmostEqual(diff, expected_diff, places=5)

    def test_12_hour_opposite(self):
        """Test that times 12 hours apart have the maximum cyclic difference."""
        diff = calculate_cyclic_time_difference(0, 12)
        # The maximum distance between two points on the unit circle is 2 (diameter)
        self.assertAlmostEqual(diff, 2, places=5)

    def test_arbitrary_hour_differences(self):
        """Test several hour differences to confirm cyclic nature."""
        self.assertAlmostEqual(calculate_cyclic_time_difference(3, 9), calculate_cyclic_time_difference(15, 21), places=5)
        self.assertAlmostEqual(calculate_cyclic_time_difference(6, 18), calculate_cyclic_time_difference(0, 12), places=5)

# Run the tests
if __name__ == "__main__":
    unittest.main()
