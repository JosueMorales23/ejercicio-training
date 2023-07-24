# install undetected-chromedriver: pip install undetected-chromedriver
import undetected_chromedriver as uc

driver = uc.Chrome(use_subprocess=True)
driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

email = 'document.getElementById("identifierId").value = "mi-correo";'
driver.execute_script(email)

siguiente = 'document.getElementsByClassName("VfPpkd-RLmnJb")[1].click();'
driver.execute_script(siguiente)

password = 'document.getElementsByClassName("whsOnd zHQkBf")[0].value = "mi-contraseña";'
driver.execute_script(password)

button = 'document.getElementsByClassName("VfPpkd-vQzf8d")[1].click();'
driver.execute_script(button)
