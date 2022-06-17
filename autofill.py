from selenium import webdriver

class Oasisbot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:/Users/sohzi/Downloads/chromedriver.exe")

    def OasisSite(self):
        self.driver.get("https://login.smu.edu.sg/adfs/ls/?wa=wsignin1.0&wtrealm=urn%3asharepoint%3asporprd&wctx=https%3a%2f%2foasis.smu.edu.sg%2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252F")
    
    def OasisLogin(self):

        self.driver.find_element_by_id("userNameInput").send_keys("zihao.soh.2021@economics.smu.edu.sg")

        self.driver.find_element_by_id("passwordInput").send_keys("StarWars69!")

        self.driver.find_element_by_id("submitButton").click()

if __name__ == "__main__":
    Oasisbot = Oasisbot()
    Oasisbot.OasisSite()
    Oasisbot.OasisLogin()

