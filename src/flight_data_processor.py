from typing import List, Dict, Optional


class FlightDataProcessor:
    """
    A class to manage flight data, including adding, removing, filtering, and updating flights.
    """

    def __init__(self) -> None:
        """
        Initializes an empty list to store flight data.
        """
        self.flights: List[Dict] = []

    def add_flight(self, data: Dict) -> None:
        """
        Adds a new flight to the list, ensuring no duplicate flight numbers.

        :param data: A dictionary containing flight details.
        """
        if not self._is_existing_flight(data['flight_number']):
            self.flights.append(data)

    def remove_flight(self, flight_number: str) -> None:
        """
        Removes a flight from the list based on the flight number.

        :param flight_number: The flight number to remove.
        """
        self.flights = [flight for flight in self.flights if flight['flight_number'] != flight_number]

    def flights_by_status(self, status: str) -> List[Dict]:
        """
        Returns all flights with a given status.

        :param status: The status to filter flights by (e.g., "ON_TIME", "DELAYED", "CANCELLED").
        :return: A list of flight dictionaries matching the given status.
        """
        return [flight for flight in self.flights if flight['status'] == status]

    def get_longest_flight(self) -> Optional[Dict]:
        """
        Returns the flight with the longest duration in minutes.

        :return: The dictionary of the longest flight, or None if there are no flights.
        """
        if not self.flights:
            return None
        return max(self.flights, key=lambda flight: flight['duration_minutes'])

    def update_flight_status(self, flight_number: str, new_status: str) -> None:
        """
        Updates the status of a specific flight.

        :param flight_number: The flight number to update.
        :param new_status: The new status to set for the flight.
        """
        for flight in self.flights:
            if flight['flight_number'] == flight_number:
                flight['status'] = new_status

    def _is_existing_flight(self, flight_number: str) -> bool:
        """
        Checks if a flight with the given flight number already exists.

        :param flight_number: The flight number to check.
        :return: True if the flight exists, False otherwise.
        """
        return any(flight['flight_number'] == flight_number for flight in self.flights)


# Example usage
if __name__ == "__main__":
    # Sample flight data
    flight_data = [
        {
            "flight_number": "AZ001",
            "departure_time": "2025-02-19 15:30",
            "arrival_time": "2025-02-20 03:45",
            "duration_minutes": 675,
            "status": "ON_TIME"
        },
        {
            "flight_number": "AZ002",
            "departure_time": "2025-02-21 11:00",
            "arrival_time": "2025-02-21 16:00",
            "duration_minutes": 300,
            "status": "DELAYED"
        },
    ]

    # Create a FlightDataProcessor instance
    processor = FlightDataProcessor()

    # Add flights to the processor
    for flight in flight_data:
        processor.add_flight(flight)

    # Print the longest flight
    print("Longest flight:", processor.get_longest_flight())

    # Update flight status
    processor.update_flight_status("AZ002", "ON_TIME")
    print("Updated flights:", processor.flights_by_status("ON_TIME"))

    # Remove flight
    processor.remove_flight("AZ001")