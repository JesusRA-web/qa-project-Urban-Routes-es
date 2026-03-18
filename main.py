import data
from selenium import webdriver
from urban_routes_page import UrbanRoutesPage
class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        # Habilita logs para que helpers.py recupere el SMS
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.routes_page = UrbanRoutesPage(cls.driver)

    # PASO 1: Direcciones
    def test_urban_routes_address(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page.set_route(data.address_from, data.address_to)
        # Verificación: ¿Se escribieron bien las direcciones?
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_urban_routes_tarifa_confort(self):
    # 2. Seleccionar tarifa Comfort
       self.routes_page.click_smart_button()
       self.routes_page.select_comfort_tariff()
       assert self.routes_page.is_comfort_selected() is True

    def test_urban_routes_phone(self):
    # 3. Rellenar número de teléfono
       self.routes_page.set_phone(data.phone_number)
       assert self.routes_page.get_phone_button_text() == data.phone_number

    def test_urban_routes_add_card(self):
    # 4. Agregar tarjeta
       self.routes_page.add_card(data.card_number, data.card_code)
       self.routes_page.close_payment_panel()
       assert self.routes_page.is_card_added()=="Tarjeta"

    def test_urban_routes_comment(self):
    # 5. Comentario para el conduct
       self.routes_page.set_comment(data.message_for_driver)
       assert self.routes_page.get_comment_value() == data.message_for_driver

    def test_urban_routes_mantas(self):
    # 6. Adicionar mantas
       self.routes_page.select_mantas()
       assert self.routes_page.get_blanket_status() is True

    def test_urban_routes_ice_crea(self):
    # 7.adicionar 2 helados
       self.routes_page.add_ice_cream()
       assert self.routes_page.get_ice_cream_count() == 2

    def test_urban_routes_order_taxi(self):
    # 8. Pedir taxi
       self.routes_page.click_order_taxi_button()
       assert self.routes_page.is_search_modal_visible() is True
    # 9. Esperar a que aparezca la información del conductor
       self.routes_page.wait_for_driver_assignment()

    # El Assert: Verificamos que el texto del encabezado contiene lo esperado
       final_text = self.routes_page.get_driver_info_text()

       assert "conductor" in final_text.lower()

    def test_quit_driver(self):
        self.driver.close()
