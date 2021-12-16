from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\pablo.marrero\\Workspaces\\chromedriver.exe")
#driver = webdriver.Chrome() esto es cuando has metido el chromedriver al mismo nivel que el script
driver.get("https://www3.animeflv.net/")

seleccion_serie = driver.find_element(By.CSS_SELECTOR, "a[href*='anime/one-piece-tv']")
seleccion_serie.click()

driver.quit()
#assert ultimo_episodio == 1003