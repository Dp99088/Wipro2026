import pytest
from selenium import webdriver
import configparser
import os
import sys
import datetime

# Add project root to sys.path so that 'pages' and 'utilities' can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Load configuration
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini'))

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help="Type of browser: chrome, firefox, edge")

@pytest.fixture(scope="class")
def driver(request):
    # Command line option takes precedence
    browser_type = request.config.getoption("--browser")
    if not browser_type:
        browser_type = config['settings']['browser'].lower()
    
    base_url = config['settings']['url']
    
    if browser_type == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless") 
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(options=options)
    elif browser_type == 'firefox':
        options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    elif browser_type == 'edge':
        options = webdriver.EdgeOptions()
        # options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Browser {browser_type} not supported")
    
    driver.maximize_window()
    driver.get(base_url)
    
    yield driver
    
    driver.quit()

@pytest.fixture(scope="function")
def step(request):
    """
    Fixture to log test steps to both terminal and HTML report.
    Usage: step("Log description")
    """
    def _step(message):
        print(f"STEP: {message}")
        if not hasattr(request.node, "test_steps"):
            request.node.test_steps = []
        request.node.test_steps.append(message)
    return _step

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])

    if report.when == 'call' or (report.when == 'setup' and report.skipped):
        # Add steps to the report
        if hasattr(item, "test_steps"):
             steps_html = "<ul>" + "".join([f"<li>{s}</li>" for s in item.test_steps]) + "</ul>"
             extras.append(pytest_html.extras.html(f"<div><b>Test Steps:</b>{steps_html}</div>"))

        driver = item.funcargs.get('driver', None)
        if driver:
            # Sanitize the test name to use as a filename
            test_name = item.name
            invalid_chars = '<>:"/\\|?*'
            for char in invalid_chars:
                test_name = test_name.replace(char, "_")
            
            timestamp = datetime.datetime.now().strftime('%H-%M-%S_%d-%m-%Y')
            screenshots_dir = os.path.join(os.path.dirname(__file__), '..', 'screenshots')
            os.makedirs(screenshots_dir, exist_ok=True)

            suffix = ""
            if report.failed:
                suffix = "_failed"
            elif report.skipped:
                # Capture skip reason
                skip_reason = "skipped"
                if hasattr(report, 'longrepr') and report.longrepr:
                    # report.longrepr can be a tuple (file, line, reason) or a string
                    if isinstance(report.longrepr, tuple):
                        skip_reason = report.longrepr[2]
                    else:
                        skip_reason = str(report.longrepr)
                
                # Sanitize skip reason
                for char in invalid_chars + ' ':
                    skip_reason = skip_reason.replace(char, "_")
                suffix = f"_skipped_{skip_reason}"

            if suffix:
                screenshot_path = os.path.join(screenshots_dir, f'{test_name}{suffix}_{timestamp}.png')
                driver.save_screenshot(screenshot_path)
                
                screenshot_base64 = driver.get_screenshot_as_base64()
                extras.append(pytest_html.extras.image(screenshot_base64))
        report.extras = extras

def pytest_configure(config):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    reports_dir = os.path.join(root_dir, 'reports')
    screenshots_dir = os.path.join(root_dir, 'screenshots')

    os.makedirs(reports_dir, exist_ok=True)
    os.makedirs(screenshots_dir, exist_ok=True)

    # Always generate new report with timestamp
    timestamp = datetime.datetime.now().strftime('%H-%M-%S_%d-%m-%Y')
    report_file = f"report_{timestamp}.html"
    report_path = os.path.join(reports_dir, report_file)

    config.option.htmlpath = report_path

def pytest_collection_modifyitems(items):
    """
    Sorts tests such that all tests for a specific parameter (user) 
    run consecutively. This allows class-scoped fixtures like 'driver'
    to persist through the entire multi-step journey.
    """
    def get_sort_key(item):
        # Sort by parameter ID (data0, data1...) then by test name (test_01, test_02...)
        data_id = ""
        if hasattr(item, 'callspec'):
            data_id = str(item.callspec.id)
        return (data_id, item.name)
    
    items.sort(key=get_sort_key)
