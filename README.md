# Selenium Form Automation Script

## Overview
This project is a Python-based script that automates the process of filling out and submitting a form on a given webpage using the **Selenium WebDriver**. The script programmatically interacts with the form by identifying specific elements via their IDs, class names, and attributes, and sends data for testing purposes.

---

## Features
- **Automated form navigation:** Opens a web page in a Chrome browser.
- **Field interaction:** Inputs values into form fields such as email, subject, and message.
- **Form submission:** Simulates a click on the "Submit" button.
- **Validation:** Ensures key elements are present on the page to verify functionality.

---

## Technologies
- Python 3.x
- Selenium WebDriver

---

## Setup Instructions

### Prerequisites
1. Install [Python 3.x](https://www.python.org/) on your machine.
2. Install the required Python libraries:
   ```bash
   pip install selenium
   ```
3. Download and install the [ChromeDriver](https://chromedriver.chromium.org/) that matches your Chrome browser version:
   - Add the downloaded ChromeDriver to your system's PATH or specify its full path in the script if required.

### Files
- **`automation_script.py`:** The main Python script containing the Selenium automation logic.

---

## How to Run
1. Clone this repository or download the script file.
2. Navigate to the directory where the script is located.
3. Run the script using the command:
   ```bash
   python automation_script.py
   ```
4. The script will:
   - Open a browser and navigate to the specified URL.
   - Fill in the form fields with pre-defined testing data.
   - Submit the form and close the browser after a short delay.

---

## Configuration
Modify the constant **`BASE_URL`** in `automation_script.py` if you want the script to target a different webpage:
```python
BASE_URL = 'https://example.com/your-form-url'
```

You can also change the test data (email, subject, and message) by modifying the following code block in `fill_form_fields` function:
```python
email_field.send_keys('h@gmai.com')
subject_field.send_keys('Testing')
message_field.send_keys('Hi there, this is a test message')
```

---

## Notes
- **Headless Browsing:** For running the script in headless mode (without opening the browser window), you can modify the WebDriver options in the `open_browser_and_navigate` function.
- **Delays:** The script includes a `time.sleep(10)` delay for demonstration purposes. You can adjust it based on your requirements.

---

## Author
**Hossein Kargar**

---

## License
This project is licensed under the MIT License. Feel free to modify and use it for your own purposes.
