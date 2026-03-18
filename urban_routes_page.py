from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
import helpers  # Esto permite llamar a helpers.retrieve_phone_code()
import time

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Paso 1: Direcciones
    def set_route(self, from_address, to_address):
        self.wait.until(EC.visibility_of_element_located(locators.FROM_FIELD)).send_keys(from_address)
        self.driver.find_element(*locators.TO_FIELD).send_keys(to_address)

    # Paso 2: Seleccionar Tarifa Comfort
    def click_smart_button(self):
        # Esperamos a que el botón "Pedir un taxi" sea clicK
        self.wait.until(EC.element_to_be_clickable(locators.SMART_BUTTON)).click()

    def select_comfort_tariff(self):
        # Ahora sí seleccionamos la tarjeta de tarifa Comfort
        self.wait.until(EC.element_to_be_clickable(locators.COMFORT_TARIFF_CARD)).click()

# Paso 3: Rellenar el número de teléfono
    def set_phone(self, phone_number):
        # 1. Clic para abrir el modal
        self.wait.until(EC.element_to_be_clickable(locators.PHONE_BUTTON)).click()
        # 2. Esperar a que el input aparezca y escribir el número
        self.wait.until(EC.visibility_of_element_located(locators.PHONE_INPUT)).send_keys(phone_number)
        # 3. Clic en el botón "Siguiente"
        self.driver.find_element(*locators.NEXT_BUTTON_PHONE).click()
        # Recuperamos el código usando la función de tu hoja helpers.py
        sms_code = helpers.retrieve_phone_code(self.driver)

        # Escribimos el código en el campo de SMS (asegúrate de tener este locator)
        self.wait.until(EC.visibility_of_element_located(locators.SMS_CODE_INPUT)).send_keys(sms_code)

        # Clic en el botón para confirmar el código
        self.driver.find_element(*locators.CONFIRM_PHONE_BUTTON).click()

    def add_card(self, card_number, card_code):
        payment_method = self.wait.until(EC.element_to_be_clickable(locators.PAYMENT_METHOD_BUTTON))
        payment_method.click()

# 2. Clic en 'Agregar tarjeta' (Asegúrate que el modal anterior ya cerró)
        self.wait.until(EC.element_to_be_clickable(locators.ADD_CARD_BUTTON)).click()
        # Abrir el modal de pago
 # PASO 1: Escribir SOLO el número y presionar TAB
        self.driver.implicitly_wait(2)
        card_field = self.wait.until(EC.visibility_of_element_located(locators.CARD_NUMBER_INPUT))
        card_field.send_keys(card_number)
        card_field.send_keys(Keys.TAB)  # Esto mueve el foco al siguiente campo

        # PASO 2: Escribir SOLO el CVV
        code_field = self.wait.until(EC.element_to_be_clickable(locators.CARD_CODE_INPUT))
        code_field.send_keys(card_code)
        code_field.send_keys(Keys.TAB)  # Solo una vez
        time.sleep(2)
    # ... después de card_field.send_keys(Keys.TAB) ...

    # 1. Clic en el botón para confirmar/enlazar la tarjeta (EL PASO QUE FALTABA)
        self.wait.until(EC.element_to_be_clickable(locators.LINK_CARD_BUTTON)).click()

    def is_card_selected(self):
        selector = self.wait.until(
            EC.presence_of_element_located(locators.PAYMENT_SELECTOR)
        )
        return "active" in selector.get_attribute("class") \
            or "selected" in selector.get_attribute("class")

    #paso 5: creAr comentario para conductor
    def set_comment(self, comment):
        self.driver.find_element(*locators.COMMENT_FIELD).send_keys(comment)
        self.wait.until(EC.invisibility_of_element_located(locators.ADD_CARD_BUTTON))
        comment_field = self.wait.until(EC.visibility_of_element_located(locators.COMMENT_FIELD))
        comment_field.send_keys()
# paso 7:
    def click_order_taxi_button(self):
        self.driver.find_element(*locators.FINAL_ORDER_BUTTON).click()

    def get_from(self):
        return self.wait.until(EC.visibility_of_element_located(locators.FROM_FIELD)).get_attribute('value')

    def get_to(self):
        # Localiza el campo 'Hasta' y extrae el texto que se escribió
        return self.driver.find_element(*locators.TO_FIELD).get_attribute('value')

    def is_comfort_selected(self):
        # Usamos wait para dar tiempo a que la clase 'active' aparezca
        return self.wait.until(EC.presence_of_element_located(locators.COMFORT_ACTIVE_STATE)).is_displayed()

    def get_phone_button_text(self):
        # Extrae el número de teléfono que aparece en el botón principal
        return self.driver.find_element(*locators.PHONE_BUTTON).text

    def select_mantas(self):
        # Pausa de 3 segundos para que todos los modales se cierren y la página respire
        time.sleep(3)

        # 1. Intentar activar la manta
        self.driver.find_element(*locators.BLANKET_SWITCH)
        blanket_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locators.BLANKET_SWITCH))
        # 2. Ejecutamos el script
        self.driver.execute_script("arguments[0].click();",blanket_btn)

    def get_blanket_status(self):
         # Retorna True si está seleccionado (azul), False si no.
        return self.driver.find_element(*locators.BLANKET_SWITCH).is_selected()

    def add_ice_cream(self):    # Otra pequeña pausa antes de los helados
        time.sleep(1)
        # 2. Los dos helados
        plus_btn = self.wait.until(EC.element_to_be_clickable(locators.ICE_CREAM_PLUS_BUTTON))
        plus_btn.click()
        time.sleep(0.5)  # Pausa mínima entre clics para que el sistema registre el primero
        plus_btn.click()

    def get_ice_cream_count(self):
        # Buscamos el elemento, obtenemos el texto ("2") y lo convertimos a número
        count = self.driver.find_element(*locators.ICE_CREAM_VALUE).text
        return int(count)
    def is_card_added(self):
        return self.wait.until(EC.visibility_of_element_located(locators.ADDED_CARD)).text
    def close_payment_panel(self):
        close_btn = self.wait.until(
            EC.element_to_be_clickable(locators.CLOSE_PAYMENT_MODAL_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            close_btn
        )

    def get_comment_value(self):
        # Lee el texto que quedó escrito en el campo de comentario
        return self.driver.find_element(*locators.COMMENT_FIELD).get_attribute('value')

    def is_blanket_on(self):
        # Verifica si el interruptor de la manta está seleccionado (marcado)
        # Algunos elementos usan 'checked' o un cambio en la clase CSS
        return self.driver.find_element(*locators.BLANKET_SWITCH).is_selected()

    def is_search_modal_visible(self):
        # Confirma que el modal de "Buscando conductor" apareció tras pedir el taxi
        # Esto indica que el flujo completo fue exitoso
        return self.wait.until(EC.visibility_of_element_located(locators.FINAL_ORDER_BUTTON)).is_displayed()

    def wait_for_driver_assignment(self):
        # Esperamos hasta 45 segundos a que el título cambie a "El conductor llegará..."
        return WebDriverWait(self.driver,60).until(
            EC.visibility_of_element_located(locators.DRIVER_ARRIVAL_TITLE)
        )

    def get_driver_info_text(self):
        element = self.wait_for_driver_assignment()
        return element.text

    def quit_driver(self):
        self.driver.quit()