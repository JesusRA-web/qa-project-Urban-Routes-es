from selenium.webdriver.common.by import By
#  Configurar la dirección (Desde y Hasta)
FROM_FIELD = (By.ID, 'from')
TO_FIELD = (By.ID, 'to')
# selecionar boton pedir taxi
SMART_BUTTON = (By.CSS_SELECTOR, '.button.round')
# Este busca el div que contiene el texto 'Comfort' para asegurar el clic
COMFORT_TARIFF_CARD = (By.XPATH, "//div[contains(@class, 'tcard')]//div[text()='Comfort']")
# Este te sirve para verificar si se seleccionó correctamente opcion confort
COMFORT_ACTIVE_STATE = (By.CSS_SELECTOR, ".tcard.active")
# Rellenar el número de teléfono
PHONE_BUTTON = (By.CLASS_NAME, 'np-button')
PHONE_INPUT = (By.ID, 'phone')
# Usamos un XPath que busque el botón que TIENE la clase 'full' Y el texto 'Siguiente'
NEXT_BUTTON_PHONE = (By.XPATH, "//button[contains(@class, 'full') and text()='Siguiente']")
# Elementos del modal de confirmación SMS
SMS_CODE_INPUT = (By.ID, 'code') #
CONFIRM_PHONE_BUTTON = (By.XPATH, '//button[text()="Confirmar"]')
# 4. Agregar una tarjeta de crédito
PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-button')
ADD_CARD_BUTTON = (By.XPATH, "//div[text()='Agregar tarjeta']")
CARD_NUMBER_INPUT = (By.ID, 'number')
CONFIRM_CODE_INPUT = (By.XPATH, "//div[@class='number-picker']//input[@id='code']")
CARD_CODE_INPUT = (By.XPATH, "//div[@class='card-wrapper']//input[@id='code']")
LINK_CARD_BUTTON = (By.XPATH,"//button[text()='Agregar']")
CLOSE_PAYMENT_MODAL = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
PAYMENT_METHOD_VALUE = (By.XPATH,"//div[@class='pp-value-text' and text()='Tarjeta']")
CLOSE_PAYMENT_PANEL = (By.CSS_SELECTOR,"button.close-button.section-close")
ADDED_CARD = (By.XPATH, "//div[@class='pp-value-text' and text()='Tarjeta']")
ACTIVE_CARD = (By.CSS_SELECTOR, ".payment-card.active")
PAYMENT_SELECTOR = (By.CSS_SELECTOR, ".pp-selector")
# Buscamos específicamente el botón de cierre dentro de la sección de pago activa
CLOSE_PAYMENT_MODAL_BUTTON = (By.CSS_SELECTOR, ".payment-picker.open .section.active .close-button")
SAVED_CARD = (By.CSS_SELECTOR,".payment-method__card")
# comentario conductor
COMMENT_FIELD = (By.ID, 'comment')
# helado
ICE_CREAM_PLUS_BUTTON = (By.XPATH, "//div[text()='Helado']/..//div[@class='counter-plus']")
# Localizador para el número que muestra la cantidad de helados
ICE_CREAM_VALUE = (By.XPATH, "//div[text()='Helado']/..//div[@class='counter-value']")
#  para la manta,
BLANKET_SWITCH = (By.XPATH, "//div[text()='Manta y pañuelos']/..//input[@class='switch-input']")
# Este apunta al switch de manata para validar estado
BLANKET_CHECKBOX = (By.CSS_SELECTOR, '.r-sw-container input.switch-input')
#El gran botón final (El que confirma todo el viaje)
FINAL_ORDER_BUTTON = (By.CLASS_NAME, 'smart-button-main')
#busca la palabra conductor en modal final
DRIVER_ARRIVAL_TITLE = (By.XPATH, "//div[contains(@class, 'order-header-title') and contains(text(), 'conductor')]")
# busca nombre conductor modal final
DRIVER_NAME_DISPLAY = (By.XPATH, "//div[contains(@class, 'order-btn-group')]//div[contains(text(), 'driver.name')]")