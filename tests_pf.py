#python3 -m pytest -v --driver Chrome --driver-path C:/chromedriver.exe  tests_pf.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import val_email
from settings import val_pass
from settings import b_url

@pytest.fixture(autouse=True)
def test_petfriends():
    pytest.driver = webdriver.Chrome('C:\chromedriver.exe')
    pytest.driver.get(b_url)
    pytest.driver.maximize_window()
    pytest.driver.implicitly_wait(10)

    yield

    pytest.driver.quit()


def test_my_pets():
    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element(By.ID, "email").send_keys(val_email)

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "pass")))
    pytest.driver.find_element(By.ID, "pass").send_keys(val_pass)

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()


def test_all_pets():
    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element(By.ID, "email").send_keys(val_email)

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "pass")))
    pytest.driver.find_element(By.ID, "pass").send_keys(val_pass)

    element = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'tr')))
    pets = len(pytest.driver.find_elements(By.TAG_NAME, 'tr'))

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, '(html/body/div[1]/div[1]/div[1])')))
    pets_counter = pytest.driver.find_element(By.XPATH, '(html/body/div[1]/div[1]/div[1])')
    pets_counter = pets_counter.get_attribute('innerText')

    assert str((pets) - 1) in pets_counter


def test_photo_of_pets():
    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element(By.ID, "email").send_keys(val_email)

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "pass")))
    pytest.driver.find_element(By.ID, "pass").send_keys(val_pass)

    element = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'th>img')))
    photo = pytest.driver.find_elements(By.CSS_SELECTOR, 'th>img')

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'tr')))
    pets = len(pytest.driver.find_elements(By.TAG_NAME, 'tr'))
    photo_counter = 0

    for x in range(len(photo)):
        if photo[x].get_attribute('src') != "":
            photo_counter += 1
        else:
            photo_counter += 0
    assert photo_counter >= (pets-1)//2


def test_pet_contain():
    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element(By.ID, "email").send_keys(val_email)

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "pass")))
    pytest.driver.find_element(By.ID, "pass").send_keys(val_pass)

    element = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td[1]")))
    names = pytest.driver.find_elements(By.XPATH, "//tbody/tr/td[1]")

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td[2]")))
    breed = pytest.driver.find_elements(By.XPATH, "//tbody/tr/td[2]")

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td[3]")))
    age = pytest.driver.find_elements(By.XPATH, "//tbody/tr/td[3]")

    for i in range(len(names)):
        assert names[i].text != ''
        assert breed[i].text != ''
        assert age[i].text != ''


def test_dif_name_of_pets():
    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element(By.ID, "email").send_keys(val_email)

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "pass")))
    pytest.driver.find_element(By.ID, "pass").send_keys(val_pass)

    element = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td[1]")))
    names = pytest.driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
    the_same = 0
    dub_names = []

    for x in range(len(names)):
        dub_names.append(names[x].text)

    print(dub_names)
    for x in dub_names:
        if the_same == 2:
            break
        the_same = 0
        for y in dub_names:
            if x == y:
                the_same += 1
            if the_same == 2:
                break
    assert the_same == 1

def test_dif_pets():
    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element(By.ID, "email").send_keys(val_email)

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "pass")))
    pytest.driver.find_element(By.ID, "pass").send_keys(val_pass)

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td[1]")))
    names = pytest.driver.find_elements(By.XPATH, "//tbody/tr/td[1]")

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td[2]")))
    breed = pytest.driver.find_elements(By.XPATH, "//tbody/tr/td[2]")

    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td[3]")))
    age = pytest.driver.find_elements(By.XPATH, "//tbody/tr/td[3]")

    same_name = 0
    same_breed = 0
    same_age = 0
    dub_name = []
    dub_breed = []
    dub_age = []

    for x in range(len(names)):
        dub_name.append(names[x].text)

    for x in dub_name:
        if same_name == 2:
            break
        same_name = 0
        for y in dub_name:
            if x == y:
                same_name += 1
            if same_name == 2:
                break


    for x in range(len(breed)):
        dub_breed.append(breed[x].text)

    for x in dub_breed:
        if same_breed == 2:
            break
        same_breed = 0
        for y in dub_breed:
            if x == y:
                same_breed += 1
            if same_breed == 2:
                break


    for x in range(len(age)):
        dub_age.append(age[x].text)

    for x in dub_age:
        if same_age == 2:
            break
        same_age = 0
        for y in dub_age:
            if x == y:
                same_age += 1
            if same_age == 2:
                break

    total_same = same_name + same_breed + same_age

    assert total_same != 6