from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from time import sleep
from random import uniform, randint

class SkinReaper():
    """Skin collector for minecraftskins.com"""
    def __init__(self):
        """Initialize Firefox webdriver. 
        geckodriver.exe in the same directory and firefox installed and in path required!"""
        print("Initializing webdriver...")
        options = FirefoxOptions()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", True)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/png")

        self.__dr = Firefox(options=options)
        self.__base = "https://www.minecraftskins.com"
        self.__preview = False
        print("Done")

    def dumpLinks(self, filename, data):
        """Save array to file"""
        print(f"Dumping data to {filename}...")
        f = open(filename, "w")
        for link in data:
            f.writelines(link + "\n")
        f.close()
        print("Done")

    def harvestLinks(self, amount=1, max_wait_time=0.0):
        """Visit main website with todays featured skins and get links."""
        if(amount > 10):
            self.kill()
            raise Exception('Too much elements requested!')
        result = list()
        for i in range(1, amount+1):
            print(f"Capturing page {i}...")
            self.__dr.delete_all_cookies()
            sleep(uniform(0.0, max_wait_time))
            self.__dr.get(self.__base + f"/{i}/")
            skins = self.__dr.find_elements(By.CLASS_NAME, 'js-skin-title')
            for skin in skins:
                result.append(skin.get_attribute('href'))

        return result
    
    def collectSouls(self, data, amount=1, max_wait_time=0.0):
        """Visit every link from array get download links and skins."""
        if(amount > len(data)):
            self.kill()
            raise Exception('Not enough data!')

        resultLinks = list()

        print("Link targeted hunting started...")
        for link in range(amount):
            self.__dr.delete_all_cookies()
            sleep(uniform(0.0, max_wait_time))
            self.__dr.get(data[link])
            targetLink = self.__dr.find_element(By.CLASS_NAME, 'btn-download')
            resultLinks.append(targetLink.get_attribute('href'))

        print("Downloading skins...")
        for soul in resultLinks:
            self.__dr.delete_all_cookies()
            sleep(uniform(0.0, max_wait_time))
            self.__dr.get(soul)
        print("Download finished")

    def loadFromFile(self, filename):
        """Load array from file."""
        f = open(filename, "r")
        data = f.read()
        f.close()
        print(f"Loaded {filename}")
        return data.split("\n")

    def collectRandom(self, data, max_wait_time=0.0):
        """Download random skin from provided data."""
        print("Targeting random link...")
        self.__dr.delete_all_cookies()
        sleep(uniform(0.0, max_wait_time))
        self.__dr.get(data[randint(0, len(data)-1)])
        targetLink = self.__dr.find_element(By.CLASS_NAME, 'btn-download')
        targetLink = targetLink.get_attribute('href')
        if(self.__preview):
            skinPreview = self.__dr.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/img[1]')
            skinPreview = skinPreview.get_attribute('src')
            print("Check your skin here:")
            print(skinPreview)
        print("Download of a skin begins...")
        self.__dr.delete_all_cookies()
        sleep(uniform(0.0, max_wait_time))
        self.__dr.get(targetLink)

    def setSkinPreview(self, value=True):
        """Use it if you want to get link to preview when getting random skin."""
        self.__preview = value

    def kill(self):
        """Kill the webdriver."""
        print("Dead but dreaming...")
        self.__dr.quit()