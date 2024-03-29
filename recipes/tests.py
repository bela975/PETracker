from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless") #sera usado no actions
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

global wait
wait = WebDriverWait(driver, 10)

class petracker_tests(LiveServerTestCase):
    def test(self):
        driver.get("http://ptv123-env.eba-gb4zztkd.sa-east-1.elasticbeanstalk.com/")
        self.run_tests(driver)
    
    def register(self, driver):
        time.sleep(10)
        register = driver.find_element(By.NAME, "sign-up")
        driver.execute_script("arguments[0].click();", register)
        register_username = driver.find_element(By.NAME, "username")
        register_username.send_keys("miles morales")
        register_email = driver.find_element(By.NAME, "email")
        register_email.send_keys("spiderman@gmail.com")
        register_password = driver.find_element(By.NAME, "password")
        register_password.send_keys("gwen&miles")
        register_button = driver.find_element(By.NAME, "register")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", register_button)
        print("REGISTER TEST OK")

    def login(self, driver):
        driver.get("http://ptv123-env.eba-gb4zztkd.sa-east-1.elasticbeanstalk.com/")
        time.sleep(2)
        login_username = driver.find_element(By.NAME, "username")
        login_username.send_keys("miles morales")
        login_password = driver.find_element(By.NAME, "password")
        login_password.send_keys("gwen&miles")
        login_button = driver.find_element(By.NAME, "login")
        time.sleep(1)
        login_button.click()
        print("LOGIN TEST OK")

    def register_pet(self, driver):
        time.sleep(1)
        register_pet_button = driver.find_element(By.LINK_TEXT, "+")
        register_pet_button.click()
        register_pet_name = driver.find_element(By.NAME, "name")
        register_pet_name.send_keys("Peter Porker")
        register_pet_breed = driver.find_element(By.NAME, "breed")
        register_pet_breed.send_keys("Spider Pig")
        register_pet_age = driver.find_element(By.NAME, "age")
        register_pet_age.send_keys("3")
        register_pet_description = driver.find_element(By.NAME, "description")
        register_pet_description.send_keys("This is astounding! Am I a spider with the limitations of a pig? Or a pig with the proportionate strength and agility of a spider? I've become something greater than either spider or pig... I've become a Spider-Ham!")
        register_pet_phone = driver.find_element(By.NAME, "phone")
        register_pet_phone.send_keys("12345678910")
        register_pet_email = driver.find_element(By.NAME, "email")
        register_pet_email.send_keys("spiderman@gmail.com")
        # driver.find_element(By.NAME, "photo").send_keys("C:/Users/virna/OneDrive/Área de Trabalho/PETracker/files/spider_pig.jpg") # utilizado para teste local com link aws
        register_pet_button_create = driver.find_element(By.NAME, "create")
        time.sleep(2)
        register_pet_button_create.click()
        print("REGISTER PET TEST OK")
        

    def acessing_home(self, driver):
        time.sleep(1)
        pet_profile_button = driver.find_element(By.ID, "pet_profile")
        driver.execute_script("arguments[0].click();", pet_profile_button)
        time.sleep(1)
        print("ACESSING HOME PET TEST OK")


    def alergy(self, driver):
        alergy_input = driver.find_element(By.NAME, "title")
        alergy_input.send_keys("Tylenol")
        alergy_input_button = driver.find_element(By.NAME, "add")
        alergy_input_button.click()
        time.sleep(1)
        driver.find_element(By.ID, "ab").click()
        time.sleep(1)
        driver.find_element(By.ID, "del-al").click()
        time.sleep(1)
        print("ALERGY TEST OK")

    def background_color(self, driver):
        background_color_select = driver.find_element(By.ID, "id_background_color")
        background_color_select.click()
        Select(background_color_select).select_by_value('#978DCC')
        background_color_select_button = driver.find_element(By.NAME, "add_color")
        background_color_select_button.click()
        time.sleep(1)
        
        background_color_select = driver.find_element(By.ID, "id_background_color")
        background_color_select.click()
        Select(background_color_select).select_by_value('#FAA42B')
        background_color_select_button = driver.find_element(By.NAME, "add_color")
        background_color_select_button.click()
        time.sleep(1)
        
        background_color_select = driver.find_element(By.ID, "id_background_color")
        background_color_select.click()
        Select(background_color_select).select_by_value('#00B7D9')
        background_color_select_button = driver.find_element(By.NAME, "add_color")
        background_color_select_button.click()
        time.sleep(1)

        background_color_select = driver.find_element(By.ID, "id_background_color")
        background_color_select.click()
        Select(background_color_select).select_by_value('#4FD881')
        background_color_select_button = driver.find_element(By.NAME, "add_color")
        background_color_select_button.click()
        time.sleep(2)
        print("BACKGROUND COLOR TEST OK")


    def calendar(self, driver):
        calendar_nav_button = driver.find_element(By.ID, "calendar")
        calendar_nav_button.click()
        new_event_button = driver.find_element(By.NAME, "button_new_event")
        new_event_button.click()
        event_title = driver.find_element(By.ID, "id_title")
        event_title.send_keys("Walk to The Park With Peter Porker")
        event_description = driver.find_element(By.ID, "id_description")
        event_description.send_keys("He needs to check if any super vilain is trying to commit crimes. Thanos can be there. Who knows? He's inevitable!")
        event_start_time = driver.find_element(By.ID, "id_start_time")
        event_start_time.send_keys("13062023")
        event_start_time.send_keys(Keys.TAB)
        event_start_time.send_keys("1620")
        event_end_time = driver.find_element(By.ID, "id_end_time")
        event_end_time.send_keys("13062023")
        event_end_time.send_keys(Keys.TAB)
        event_end_time.send_keys("2007")
        event_color_select = driver.find_element(By.ID, "id_colorSelected")
        event_color_select.send_keys("orange")
        time.sleep(3)
        event_save_button = driver.find_element(By.ID, "save-event")
        event_save_button.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)
        # precisa
        back_button = driver.find_element(By.ID, "back_button")
        back_button.send_keys(Keys.RETURN)
        time.sleep(1)
        print("CALENDAR TEST OK")


    def checklist(self, driver):
        checklist_nav_button = driver.find_element(By.ID, "kanban") 
        checklist_nav_button.click()
        new_task = driver.find_element(By.ID, "task")
        new_task.send_keys("Defeat Thanos")
        new_task_responsible = driver.find_element(By.ID, "responsible")
        new_task_responsible.send_keys("Peter Porker")
        new_task_due_date = driver.find_element(By.ID, "due-date")
        new_task_due_date.send_keys(13062023)
        add_task_button = driver.find_element(By.ID, "add-task")
        add_task_button.click()
        
        move_task_r = driver.find_element(By.ID, "right-td-btn")
        move_task_r.click()
        time.sleep(1)
        
        move_task_r2 = driver.find_element(By.ID, "right-ip-btn")
        move_task_r2.click()
        time.sleep(1)
        move_task_l = driver.find_element(By.ID, "left-d-btn")
        move_task_l.click()
        time.sleep(1)
        move_task_r2 = driver.find_element(By.ID, "right-ip-btn")
        move_task_r2.click()
        time.sleep(1)
        move_task_r3 = driver.find_element(By.ID, "right-d-btn")
        move_task_r3.click()
        time.sleep(1)
        show_history = driver.find_element(By.ID, "show")
        show_history.click()
        time.sleep(1)
        hide_history = driver.find_element(By.ID, "hide")
        hide_history.click()
        time.sleep(1)
        show_history = driver.find_element(By.ID, "show")
        show_history.click()
        time.sleep(1)
        redo_task = driver.find_element(By.ID, "restore-h-btn")
        redo_task.click()
        time.sleep(1)
        delete_task = driver.find_element(By.ID, "delete-td-btn")
        delete_task.click()
        time.sleep(1)
        
        back_button = driver.find_element(By.ID, "back_button")
        back_button.click()
        time.sleep(2)
        print("CHECKLIST TEST OK")


    def medicine(self, driver):
        medicine_nav_button = driver.find_element(By.ID, "medicine")
        medicine_nav_button.click()

        plan_medicine = driver.find_element(By.ID, "id_medicine")
        plan_medicine.send_keys("Zolmitriptan")
        plan_details = driver.find_element(By.ID, "id_details")
        plan_details.send_keys("After defeating Thanos, Peter got sick. Since Porker is alergic to Tylenol, he'll take Zolmitriptan's pills for a day instead")
        plan_times_per_day = driver.find_element(By.ID, "id_time_per_day")
        plan_times_per_day.send_keys("1")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,100)")
        time.sleep(1)
        plan_add_button = driver.find_element(By.ID, "add-plan")
        driver.execute_script("arguments[0].click();", plan_add_button)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2) #precisa
        plan_accordion = driver.find_element(By.ID, "plan-button")
        plan_accordion.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,800)")
        time.sleep(1) #precisa
        plan_accordion.click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1) #precisa
        
        medicine_diary_med = driver.find_element(By.ID, "id_med")
        medicine_diary_med.send_keys("Zolmitriptan")
        medicine_diary_resp = driver.find_element(By.ID, "id_resp")
        medicine_diary_resp.send_keys("Miles")
        medicine_diary_time = driver.find_element(By.ID, "id_time")
        medicine_diary_time.send_keys("13062023")
        medicine_diary_time.send_keys(Keys.TAB)
        medicine_diary_time.send_keys("2200")
        time.sleep(2)
        medicine_diary_add_button = driver.find_element(By.ID, "add-medicine-diary")
        medicine_diary_add_button.click()
        time.sleep(1)
        # med_info = driver.find_element(By.ID, "med-det")
        med_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "med-det")))
        med_info.click()
        # driver.execute_script("arguments[0].click();", med_info)

        time.sleep(2)
        med_delete = driver.find_element(By.ID, "del-med")
        med_delete.click()
        time.sleep(2)

        driver.execute_script("window.scrollTo(0,800)")
        time.sleep(3)
        plan_accordion = driver.find_element(By.ID, "plan-button")
        plan_accordion.click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,800)")
        time.sleep(3)
        delete_plan_accordion = driver.find_element(By.ID, "del-med-plan")
        delete_plan_accordion.click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,0)")
        time.sleep(3)

        back_button = driver.find_element(By.ID, "back_button")
        back_button.click()
        time.sleep(2)
        print("MEDICINE TEST OK")

        
    def food(self, driver):
        time.sleep(2)
        food_nav_button = driver.find_element(By.ID, "food")
        food_nav_button.click()
        food_name = driver.find_element(By.ID, "id_food")
        food_name.send_keys("Ração")
        food_resp = driver.find_element(By.ID, "id_resp")
        food_resp.send_keys("Miles")
        food_time = driver.find_element(By.ID, "id_time")
        food_time.send_keys("13062023", Keys.TAB, "2200")
        time.sleep(2)
        food_add_button = driver.find_element(By.ID, "add_food")
        food_add_button.click()
        time.sleep(1)
        food_info = driver.find_element(By.ID, "food_del")
        food_info.click()
        time.sleep(2)
        med_delete = driver.find_element(By.ID, "del-food")
        med_delete.click()
        time.sleep(2)
        back_button = driver.find_element(By.ID, "back_button")
        back_button.click()
        time.sleep(2)
        print("FOOD TEST OK")

    
    def logout(self, driver):
        logout_button = driver.find_element(By.ID, "Logout")
        logout_button.click()
        time.sleep(2)
        print("LOGOUT TEST OK")

        driver.quit()

        #shift + tab volta a linha

    def run_tests(self, driver):
        self.register(driver)
        self.login(driver)
        self.register_pet(driver)
        self.acessing_home(driver)
        self.alergy(driver)
        self.background_color(driver)
        self.calendar(driver)
        self.checklist(driver)
        self.medicine(driver)
        self.food(driver)
        self.logout(driver)
        print("ALL TESTS OK")

