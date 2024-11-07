import unittest
import numpy as np

# Function definitions
def generate_random_data(mean, variance, num_samples):
    """Generates random threat scores within the mean ± variance, constrained to [0, 90]."""
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_aggregated_threat(department_data):
    """Calculates a weighted average of threat scores for all departments based on importance."""
    total_weighted_score = sum(dept['importance'] * np.mean(dept['scores']) for dept in department_data)
    total_importance = sum(dept['importance'] for dept in department_data)
    return total_weighted_score / total_importance

# Unit test and functional test suite
class TestCybersecurityThreatCalculation(unittest.TestCase):

    ### Unit Tests ###

    def test_generate_random_data(self):
        """Test that generate_random_data produces values within the correct range."""
        mean = 30
        variance = 10
        num_samples = 100
        scores = generate_random_data(mean, variance, num_samples)
        self.assertEqual(len(scores), num_samples)  # Ensure correct number of samples
        self.assertTrue(np.all(scores >= 0))  # Ensure all scores are at least 0
        self.assertTrue(np.all(scores <= 90))  # Ensure all scores are at most 90

    def test_calculate_aggregated_threat(self):
        """Test that calculate_aggregated_threat accurately computes the weighted average."""
        department_data = [
            {"name": "DeptA", "scores": np.array([10, 20, 30]), "importance": 3},
            {"name": "DeptB", "scores": np.array([40, 50, 60]), "importance": 2}
        ]
        expected_score = (3 * 20 + 2 * 50) / (3 + 2)
        self.assertAlmostEqual(calculate_aggregated_threat(department_data), expected_score)

    ### Functional Tests ###

    def test_balanced_scenario(self):
        """Case 1: Balanced scenario with similar scores and importance tags across departments."""
        department_data = [
            {"name": "Engineering", "scores": generate_random_data(30, 5, 50), "importance": 3},
            {"name": "Marketing", "scores": generate_random_data(32, 5, 50), "importance": 3},
            {"name": "Finance", "scores": generate_random_data(31, 5, 50), "importance": 3},
            {"name": "HR", "scores": generate_random_data(29, 5, 50), "importance": 3},
            {"name": "Science", "scores": generate_random_data(30, 5, 50), "importance": 3}
        ]
        score = calculate_aggregated_threat(department_data)
        self.assertTrue(0 <= score <= 90)

    def test_high_importance_department(self):
        """Case 2: High importance for a critical department like Finance."""
        department_data = [
            {"name": "Engineering", "scores": generate_random_data(30, 5, 50), "importance": 2},
            {"name": "Marketing", "scores": generate_random_data(30, 5, 50), "importance": 2},
            {"name": "Finance", "scores": generate_random_data(70, 10, 50), "importance": 5},
            {"name": "HR", "scores": generate_random_data(30, 5, 50), "importance": 2},
            {"name": "Science", "scores": generate_random_data(30, 5, 50), "importance": 2}
        ]
        score = calculate_aggregated_threat(department_data)
        self.assertTrue(0 <= score <= 90)

    def test_high_threat_in_one_department(self):
        """Case 3: One department with a significantly high threat score."""
        department_data = [
            {"name": "Engineering", "scores": generate_random_data(30, 5, 50), "importance": 3},
            {"name": "Marketing", "scores": generate_random_data(30, 5, 50), "importance": 3},
            {"name": "Finance", "scores": generate_random_data(85, 2, 50), "importance": 3},
            {"name": "HR", "scores": generate_random_data(30, 5, 50), "importance": 3},
            {"name": "Science", "scores": generate_random_data(30, 5, 50), "importance": 3}
        ]
        score = calculate_aggregated_threat(department_data)
        self.assertTrue(0 <= score <= 90)

    def test_diverse_department_sizes(self):
        """Case 4: Departments with varied user sizes."""
        department_data = [
            {"name": "Engineering", "scores": generate_random_data(30, 5, 200), "importance": 3},
            {"name": "Marketing", "scores": generate_random_data(30, 5, 20), "importance": 3},
            {"name": "Finance", "scores": generate_random_data(30, 5, 100), "importance": 3},
            {"name": "HR", "scores": generate_random_data(30, 5, 10), "importance": 3},
            {"name": "Science", "scores": generate_random_data(30, 5, 150), "importance": 3}
        ]
        score = calculate_aggregated_threat(department_data)
        self.assertTrue(0 <= score <= 90)

    def test_low_importance_high_threat_department(self):
        """Case 5: High threat in low-importance departments."""
        department_data = [
            {"name": "Engineering", "scores": generate_random_data(30, 5, 50), "importance": 5},
            {"name": "Marketing", "scores": generate_random_data(80, 5, 50), "importance": 1},
            {"name": "Finance", "scores": generate_random_data(30, 5, 50), "importance": 5},
            {"name": "HR", "scores": generate_random_data(80, 5, 50), "importance": 1},
            {"name": "Science", "scores": generate_random_data(30, 5, 50), "importance": 5}
        ]
        score = calculate_aggregated_threat(department_data)
        self.assertTrue(0 <= score <= 90)

    def test_outlier_scores(self):
        """Case 6: Departments with outlier scores."""
        department_data = [
            {"name": "Engineering", "scores": generate_random_data(5, 5, 50), "importance": 3},
            {"name": "Marketing", "scores": generate_random_data(85, 5, 50), "importance": 3},
            {"name": "Finance", "scores": generate_random_data(45, 20, 50), "importance": 3},
            {"name": "HR", "scores": generate_random_data(10, 30, 50), "importance": 3},
            {"name": "Science", "scores": generate_random_data(60, 15, 50), "importance": 3}
        ]
        score = calculate_aggregated_threat(department_data)
        self.assertTrue(0 <= score <= 90)

# Run the test suite
if __name__ == '__main__':
    unittest.main()

