from pages.tensor import TensorPage

def test_new_tab_tenzor_exist(browser, original_window):
    tensor_page = TensorPage(browser)
    tensor_page.switch_to_new_tab(original_window)
    assert tensor_page.is_tensor_url_opened()

def test_block_tensor_exist(browser):
    tensor_page = TensorPage(browser)
    assert tensor_page.block_is_displayed

def test_tensor_more_detailed_clicked(browser):
    tensor_page = TensorPage(browser)
    tensor_page.detailed_click()

def test_tensor_block_working_exist(browser):
    tensor_page = TensorPage(browser)
    assert tensor_page.url_about
    assert tensor_page.working_is_displayed

def test_tensor_img_width_height(browser, original_window):
    tensor_page = TensorPage(browser)
    tensor_page.wait_for_container()
    images = tensor_page.get_images

    for img in images:
        width = img.get_attribute('width')
        height = img.get_attribute('height')

        assert width == '270', f"Width of image is {width}, expected 270"
        assert height == '192', f"Height of image is {height}, expected 192"

    browser.close()
    browser.switch_to.window(original_window)