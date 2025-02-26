# Flight Data Processor

## Overview

This project implements a `FlightDataProcessor` class that processes flight data. It supports adding, removing, filtering flights by status, and identifying the longest flight.

## Unit Tests

The **`tests/test_flight_data_processor.py`** file contains unit tests to verify the correctness of the `FlightDataProcessor` class.

### Test Cases

| **Test Case**                     | **Description**                                                       |
| --------------------------------- | --------------------------------------------------------------------- |
| `test_add_flight`                 | Ensures that a new flight is added correctly and prevents duplicates. |
| `test_remove_flight`              | Verifies that a flight can be removed by its flight number.           |
| `test_flights_by_status`          | Checks if filtering flights by status works correctly.                |
| `test_get_longest_flight`         | Finds the flight with the longest duration.                           |
| `test_update_flight_status`       | Ensures that a flight’s status can be updated properly.               |
| `test_invalid_flight_removal`     | Ensures no errors occur when trying to remove a non-existent flight.  |
| `test_handling_empty_flight_list` | Tests behavior when operating on an empty flight list.                |

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
python3 -m unittest discover -s tests
```
