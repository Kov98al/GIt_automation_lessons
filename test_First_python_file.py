from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest


class TestAmazon:
    search_words = ('Amazon', 'Google', 'YouTube', 'Deepl')
    driver = None
    
    #driver = ''  # Ініціалізуємо змінну в __init__ 
    def setup_method(self):
        # Цей метод викликається перед кожним тестом
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.google.com")
    
    @pytest.mark.parametrize("params_words", search_words)
    def test_amazon_search(self, params_words):
        
        search = self.driver.find_element(By.ID, 'L2AGLb')
        search.send_keys(Keys.ENTER)

        
        search_line = self.driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

        search_line.send_keys(params_words, Keys.ENTER)
        self.driver.implicitly_wait(5)
        
        sicle_word = 'Deepl'
        
        if params_words == sicle_word:
            open_Deepl_site = self.driver.find_element(By.XPATH, '//h3[@class="LC20lb MBeuO DKV0Md"]').click()
            actual_deepl_text = 'Menu'
            self.driver.implicitly_wait(5)
            expected_deepl_text = self.driver.find_element(By.XPATH, '//button[@data-testid="menu-site-btn"]').text
            print (f'{expected_deepl_text}', ' <---------  Text in Deepl')
            assert expected_deepl_text == actual_deepl_text, f'Test passed!  Actual text -> {actual_deepl_text} == expected -> {expected_deepl_text}'
        else:
            actual_text = f'{params_words}'
            expected_text = self.driver.find_element(By.CSS_SELECTOR, 'div.PZPZlf.ssJ7i.B5dxMb[data-attrid="title"]').text

            assert expected_text == actual_text, f'Test passed!  Actual text -> {actual_text} == expected -> {expected_text}'
    
    
    def teardown_method(self):
        # Цей метод викликається після кожного тесту
        self.driver.quit()