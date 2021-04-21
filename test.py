import unittest,time,requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
class Spark(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
    def test_home_page(self):
        def link(element1):
            href1=element1.get_attribute('href')
            res1=requests.get(href1)
            if(res1.status_code==200):
                c=str(res1.status_code)
                print(href1+"-----"+c)
                
        def homelink(element,val,n):
            href=element.get_attribute('href')
            time.sleep(1)            
            res=requests.get(href)
            if(res.status_code==200):
                b=str(res.status_code)
                print(href+"-----"+b)
                

        driver=self.driver

        driver.maximize_window()
        #Checking if title is correct
        self.assertEqual("The Sparks Foundation | Home",driver.title)
        element=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/a")
        #Checking if element is correct
        self.assertEqual("KNOW MORE",element.text)
        #Checking whether links navigates to next page
        homelink(element,350,3)
        element1=driver.find_element_by_xpath("//*[@id='home']/div/div[1]/h1/a")
        link(element1)
        element3=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a")
        homelink(element3,800,5)
        element4=driver.find_element_by_xpath("//*[@id='home']/div/div[1]/h1/a")
        link(element4)
        #logo displays or not
        logo=driver.find_element_by_xpath("//*[@id='home']/div/div[1]/h1/a/img")
        print("Logo displayed -----"+str(logo.is_displayed()))
        #navbar displays or not
        nav=driver.find_element_by_xpath("//*[@id='home']/div/div[2]/nav")
        print("Navbar displayed -----"+str(nav.is_displayed()))
        #Slider displays or not
        slider=driver.find_element_by_xpath("//*[@id='home']/div/div[2]/div/section")
        print("Slider displayed -----"+str(slider.is_displayed()))

        print("\n Home Page tested Succesfully")
    def test_aboutus(self):
        driver=self.driver
        driver.maximize_window()

        abt=driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[1]/a")
        guiding_pri=driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[1]/ul/li[2]/a")
        #Actionchains is used to perform the actions stored in the queue.
        #When you call perform(), the events are fired in the order they are queued up.
        action=ActionChains(driver)
        action.move_to_element(abt).click().move_to_element(guiding_pri).click()
        action.perform()
        time.sleep(3)
        print("\n About us Tested Successfully")
    def test_findus(self):
        driver=self.driver
        driver.maximize_window()

        join=driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[5]/a")
        why_join=driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[5]/ul/li[1]/a")
        action=ActionChains(driver)
        action.move_to_element(join).click().move_to_element(why_join).click()
        action.perform()
        name=driver.find_element_by_name("Name")
        contact = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]"
        )
        
        sub=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]")
        time.sleep(1)
        name.send_keys("hello")
        time.sleep(1    )
        contact.send_keys("abcd200@gmail.com")
        time.sleep(1)
        time.sleep(1)
        action1=ActionChains(driver)
        role=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/select")
        opt=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/select/option[3]")
        

        action1.move_to_element(role).click().move_to_element(opt).click()
        sub.click()
       
        time.sleep(2)
        print("\n Find us Tested Successfully")


    def test_policy_page(self):
        driver=self.driver
        driver.maximize_window()
        pol=driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[2]/a")
        pol1=driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[2]/ul/li[2]/a")

        action=ActionChains(driver)
        action.move_to_element(pol).click().move_to_element(pol1).click().perform()
        time.sleep(5)
        text=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/h2")
        self.assertEqual("Code Of Ethics And Conduct",text.text)
        text1=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[1]/div/div/h4")
        self.assertEqual("TSF Board members and employees are expected to:",text1.text)

        print("\n Policy Page Tested Successfully")

    def test_contact_us(self):
        driver=self.driver
        driver.maximize_window()
        contac=driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[6]/a')
        contac.click()
        title=driver.find_element_by_xpath('/html/body/div[2]/div/h3')
        self.assertEquals('Get In Touch',title.text)
        link=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/p/span/a')
        href1=link.get_attribute('href')

        res=requests.get(href1)
        if(res.status_code==200):

            c=str(res.status_code)
            print(href1+"-----"+c)
        link.click()
        time.sleep(2)
        print("\n Contact us page successfully tested")   
        
    def test_programs(self):
        driver=self.driver
        driver.maximize_window()
        prog=driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[3]/a')
        prog1=driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[3]/ul/li[2]/a')
        href1=prog1.get_attribute('href')

        res=requests.get(href1)
        if(res.status_code==200):

            c=str(res.status_code)
            print(href1+"-----"+c)
        action=ActionChains(driver)
        action.move_to_element(prog).click().move_to_element(prog1).click().perform()
        time.sleep(5)
        text=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[1]/div[1]/div/h4")
        self.assertEqual("Rabindranath Tagore",text.text)
        

        print("\n Student Mentorship Program Page Tested Successfully")
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()