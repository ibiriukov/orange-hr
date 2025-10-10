from playwright.sync_api import Page, expect


def get_text_of_element(element):
    return element.inner_text()

def get_value_of_element(element):
    return element.input_value()

def element_loaded(element) -> bool:
    expect(element.first).to_be_visible(timeout=8000)
    return True

def is_element_visible(locator, name) -> bool:
    try:
        visible = locator.is_visible()
        print(f"{name} visibility: {visible}")
        return visible
    except Exception as e:
        print(f"{name} visibility check failed: {e}")
        return False
