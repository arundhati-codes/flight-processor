import unittest
import time
from src.flight_data_processor import FlightDataProcessor

class TestFlightDataProcessor(unittest.TestCase):
    """Unit tests for the FlightDataProcessor class."""

    def setUp(self):
        """Set up a new FlightDataProcessor instance and sample flight data before each test."""
        self.processor = FlightDataProcessor()
        self.test_flight_data = [
            {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "duration_minutes": 675, "status": "ON_TIME"},
            {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00", "duration_minutes": 300, "status": "DELAYED"},
            {"flight_number": "AZ003", "departure_time": "2025-02-22 12:00", "arrival_time": "2025-02-22 18:00", "duration_minutes": 360, "status": "ON_TIME"}
        ]

    def test_add_flight(self):
        """Test that flights are added correctly."""
        for flight in self.test_flight_data:
            self.processor.add_flight(flight)
        self.assertEqual(len(self.processor.flights), 3)

    def test_add_duplicate_flight(self):
        """Test that duplicate flights are not allowed."""
        self.processor.add_flight(self.test_flight_data[0])
        self.processor.add_flight(self.test_flight_data[0])
        self.assertEqual(len(self.processor.flights), 1)

    def test_remove_flight(self):
        """Test that flights are removed correctly by flight number."""
        self.processor.add_flight(self.test_flight_data[0])
        self.processor.remove_flight("AZ001")
        self.assertEqual(len(self.processor.flights), 0)

    def test_flights_by_status(self):
        """Test filtering flights by status."""
        for flight in self.test_flight_data:
            self.processor.add_flight(flight)
        delayed_flights = self.processor.flights_by_status("DELAYED")
        self.assertEqual(len(delayed_flights), 1)
        self.assertEqual(delayed_flights[0]['flight_number'], "AZ002")

    def test_get_longest_flight(self):
        """Test finding the longest flight based on duration."""
        for flight in self.test_flight_data:
            self.processor.add_flight(flight)
        longest_flight = self.processor.get_longest_flight()
        self.assertEqual(longest_flight['flight_number'], "AZ001")

    def test_update_flight_status(self):
        """Test updating the flight status."""
        self.processor.add_flight(self.test_flight_data[0])
        self.processor.update_flight_status("AZ001", "CANCELLED")
        updated_flight = self.processor.flights_by_status("CANCELLED")
        self.assertEqual(len(updated_flight), 1)
        self.assertEqual(updated_flight[0]['flight_number'], "AZ001")

    def test_get_longest_flight_same_duration(self):
        """Test finding the longest flight when multiple flights have the same duration."""
        self.processor.add_flight({"flight_number": "AZ004", "duration_minutes": 500, "status": "ON_TIME"})
        self.processor.add_flight({"flight_number": "AZ005", "duration_minutes": 500, "status": "ON_TIME"})
        longest_flight = self.processor.get_longest_flight()
        self.assertIn(longest_flight['flight_number'], ["AZ004", "AZ005"])

    def test_get_longest_flight_empty_list(self):
        """Test handling an empty flight list when retrieving the longest flight."""
        longest_flight = self.processor.get_longest_flight()
        self.assertIsNone(longest_flight)

    def test_remove_non_existent_flight(self):
        """Test removing a non-existent flight should not cause errors."""
        self.processor.remove_flight("INVALID001")
        self.assertEqual(len(self.processor.flights), 0)

    def test_large_dataset_performance(self):
        """Test performance when adding a large number of flights."""
        large_flight_data = [{"flight_number": f"FL{str(i).zfill(5)}", "duration_minutes": i, "status": "ON_TIME"} for i in range(10000)]
        
        start_time = time.time()
        for flight in large_flight_data:
            self.processor.add_flight(flight)
        end_time = time.time()
        
        self.assertEqual(len(self.processor.flights), 10000)
        self.assertLess(end_time - start_time, 3)  # Should complete within 3 seconds

    def test_flights_by_status_large_dataset(self):
        """Test performance when filtering a large dataset by status."""
        for i in range(10000):
            status = "DELAYED" if i % 2 == 0 else "ON_TIME"
            self.processor.add_flight({"flight_number": f"FL{str(i).zfill(5)}", "duration_minutes": i, "status": status})
        
        start_time = time.time()
        delayed_flights = self.processor.flights_by_status("DELAYED")
        end_time = time.time()
        
        self.assertEqual(len(delayed_flights), 5000)
        self.assertLess(end_time - start_time, 1.5)  # Should complete within 1.5 seconds

if __name__ == "__main__":
    unittest.main()
