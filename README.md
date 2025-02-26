# Flight Data Processor

## Overview

This project implements a `FlightDataProcessor` class that processes flight data. It supports adding, removing, filtering flights by status, and identifying the longest flight.

## Features

- Add flights with unique flight numbers

- Remove flights by flight number

- Retrieve flights based on status (e.g., ON_TIME, DELAYED, CANCELLED)

- Find the longest flight by duration

- Update flight status

## Installation

Clone the repository:

```sh
git clone https://github.com/flight-processor/flight-data-processor.git
cd flight-data-processor
```

## Usage

```python
from src.flight_data_processor import FlightDataProcessor

# Create an instance of FlightDataProcessor
processor = FlightDataProcessor()

# Add a flight
processor.add_flight({"flight_number": "AZ001", "duration_minutes": 300, "status": "ON_TIME"})

# Remove a flight
processor.remove_flight("AZ001")

# Retrieve flights with a specific status
on_time_flights = processor.get_flights_by_status("ON_TIME")

# Get the longest flight
longest_flight = processor.get_longest_flight()
```

## Unit Tests

The **`test/test_flight_data_processor.py`** file contains unit tests to verify the correctness of the `FlightDataProcessor` class.

### Test Cases

| Test Name                               | Description                                                            |
| --------------------------------------- | ---------------------------------------------------------------------- |
| `test_add_flight`                       | Tests if flights are added correctly.                                  |
| `test_add_duplicate_flight`             | Ensures duplicate flights are not allowed.                             |
| `test_remove_flight`                    | Tests flight removal by flight number.                                 |
| `test_flights_by_status`                | Verifies filtering flights by status.                                  |
| `test_get_longest_flight`               | Ensures the longest flight is correctly identified.                    |
| `test_update_flight_status`             | Tests if flight status updates correctly.                              |
| `test_get_longest_flight_same_duration` | Verifies handling of multiple flights with the same duration.          |
| `test_get_longest_flight_empty_list`    | Ensures proper handling of an empty flight list.                       |
| `test_remove_non_existent_flight`       | Tests removal of a non-existent flight (should not cause errors).      |
| `test_large_dataset_performance`        | Checks performance when handling a large dataset (10,000 flights).     |
| `test_flights_by_status_large_dataset`  | Measures efficiency of filtering flights by status in a large dataset. |

---

## Running the Tests

### Setting Up the Virtual Environment

To run this project in an isolated environment, follow these steps:

#### **Create a virtual environment and install pytest**

```bash
python3 -m venv test_env
source venv/bin/activate
pip install pytest
```

To execute the test suite, run:

```bash
python3 -m unittest discover -s test
```
