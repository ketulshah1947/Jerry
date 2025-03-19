# Running Python Tests from Terminal

This guide explains how to run Python tests using the terminal for this project.

## Prerequisites

Before running the tests, make sure you have the following installed:

- Python 3.x (You can check if Python is installed by running `python3 --version` or `python3 --version` in the terminal)

## Steps to Run Tests

1. **Download and extract the zip file**:
   Download this assessment submission and extract to a location. 
2. **Open the Terminal**:
   Open a terminal window on your system. This can be Command Prompt (Windows), Terminal (macOS/Linux), or any other terminal you prefer. 
   Navigate to the directory where you downloaded and extracted this project.
   Use the `cd` (change directory) command to move into the project directory.
   For example:
   ```bash
   cd /path/to/your/project

3. **Run the Tests**:
   Once you're in the project directory, use the following command to run your Python tests:
   ```bash
   python -m unittest tests/IntensitySegmentsTests.py
   ```
   or 
   ```bash
   python3 -m unittest tests/IntensitySegmentsTests.py
   ```

## Troubleshooting
* **Python Not Found**:
   If Python is not recognized, make sure it is properly installed and added to your system’s PATH.
* **Module Not Found**: 
   If you see an error like ModuleNotFoundError, ensure that the Python module paths are correctly set up and that you are running the command from the correct directory.

For any further issues or assistance, feel free to contact me at ketulshah1947@gmail.com.
