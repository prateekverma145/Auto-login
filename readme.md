# Automated Network Portal Login

This project provides an automated solution for logging into your network portal each time you start your PC. It uses Selenium to enter your credentials into the network portal form automatically, ensuring uninterrupted network access without manual intervention.

## Overview

Many organizations, such as educational institutions or corporate environments, require users to authenticate via a network portal at startup. This script automates that login process, saving time and reducing the need for manual entry.

## Features

- **Automatic Login:**  
  Automatically enters your credentials into the network portal's login form.
  
- **Headless Operation:**  
  Runs Google Chrome in headless mode so that no browser window is displayed during the process.

- **Robust Error Handling:**  
  Includes error handling for common issues (e.g., element not found or WebDriver errors) to ensure a smooth login process.

- **Background Execution:**  
  Can be converted to an executable and added to Windows startup, allowing the login process to run silently in the background.

## Use Cases

- **Automated Network Access:**  
  Ideal for environments where frequent authentication is required (e.g., university or corporate networks) to maintain continuous network connectivity.

- **Time-Saving:**  
  Eliminates the repetitive task of manually logging in, especially useful if you log in several times a day.

- **Unattended Operation:**  
  Useful for systems that need to maintain network access for background tasks or services that run on startup.

## Prerequisites

- **Python 3.x**
- **Selenium:**  
  Install using `pip install selenium`.
- **Google Chrome:**  
  The script requires Google Chrome to be installed.
- **ChromeDriver:**  
  Ensure the ChromeDriver executable is available on your system's PATH or specify its location in the script.
- **PyInstaller (Optional):**  
  For converting the script into an executable. Install using `pip install pyinstaller`.

## Setup and Usage
add the code to startup so it will automatically login to the portal on pc start:
### steps
1 press win+r and write shell:startup 
2 add new shortcut and browse to location where the dist folder is and add the .exe file


### 1. Configure the Script

Edit the script to include your network portal credentials:
```python
USR = "your_username"
PASS = "your_password"
