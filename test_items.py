import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button(browser):
    browser.get(link)
    button = len(browser.find_elements_by_css_selector('.add-to-basket button'))
    # добавлено ожидание, чтобы визуально оценить результат
    time.sleep(5)
    assert button > 0, "There is no such button on the page!" 

