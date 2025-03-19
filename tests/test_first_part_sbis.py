from pages.sbis import SbisPage

def test_contacts_menu_exist(browser):
    sbis_page = SbisPage(browser)
    assert sbis_page.menu_is_displayed

def test_contacts_menu_clicked(browser):
    sbis_page = SbisPage(browser)
    sbis_page.menu_click()
    sbis_page.menu_link_click()

def test_logo_tensor_exist(browser):
    sbis_page = SbisPage(browser)
    sbis_page.logo_tensor_is_displayed

def test_logo_tensor_clicked(browser):
    sbis_page = SbisPage(browser)
    sbis_page.logo_tensor_click()