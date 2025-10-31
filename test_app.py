import pytest
from dash import Dash
from dash.testing.application_runners import import_app
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Fixture to start Dash app with automatic ChromeDriver
@pytest.fixture
def dash_duo():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    from dash.testing.browser import Browser
    yield Browser(driver)
    driver.quit()

# Load app
@pytest.fixture
def dash_app():
    app = import_app("app")  # assumes your Dash app is in app.py
    return app

# Test header exists
def test_header(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert "Pink Morsel Sales Visualiser" in header.text

# Test graph exists
def test_graph(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

# Test region picker exists
def test_region_picker(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    radio_items = dash_duo.find_element("#region-filter")
    assert radio_items is not None
