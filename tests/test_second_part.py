from pages.sbis import SbisPage

def test_page_contacts_exist(browser):
    sbis_page = SbisPage(browser)
    sbis_page.contacts_page_exist()
    assert sbis_page.contains_title_is_displayed

def test_region_exist(browser):
    sbis_page = SbisPage(browser)
    assert sbis_page.region_is_displayed
    assert sbis_page.contacts_list_is_displayed

def test_region_click(browser):
    sbis_page = SbisPage(browser)
    sbis_page.region_click()

def test_region_panel_exist(browser):
    sbis_page = SbisPage(browser)
    assert sbis_page.region_panel_is_displayed
    assert sbis_page.region_panel_header_is_displayed
    assert sbis_page.render_is_displayed

def test_region_panel_click(browser):
    sbis_page = SbisPage(browser)
    sbis_page.region_panel_click()

def test_region_new_exist(browser):
    sbis_page = SbisPage(browser)
    assert sbis_page.region_new_is_displayed

def test_contacts_list_new_exist(browser):
    sbis_page = SbisPage(browser)
    assert sbis_page.contacts_list_new_is_displayed