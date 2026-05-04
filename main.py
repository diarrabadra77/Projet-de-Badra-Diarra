#from this import d
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fake_useragent import UserAgent
import time

options = Options()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option(
    'prefs', {'profile.managed_default_content_settings.media_stream': 2}
)
options.add_argument('--start-maximized')
options.add_argument('--disable-infobars')
#options.add_argument('--disable-extensions')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1200')
options.add_argument('--start-fullscreen')
options.add_argument('--mute-audio')
options.add_extension('./ublock.crx')
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--disable-notifications')
options.add_argument(
    '--disable-features=PreloadMediaEngagementData,MediaEngagementBypassAutoplayPolicies'
)
options.add_argument('--autoplay-policy=user-required')
ua = UserAgent()
user_agent = ua.random
options.add_argument(f"user-agent={user_agent}")

monpilote = webdriver.Chrome(options=options)
print('Chrome démarré')

monpilote.get('https://www.umontpellier.fr/')


monbouton = WebDriverWait(monpilote, timeout=10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="tarteaucitronPersonalize2"]')))
time.sleep(1)
monbouton.click()



diplôme = 'Master CCA'

mazone = WebDriverWait(monpilote, timeout=3).until(expected_conditions.presence_of_element_located((By.XPATH,'/html/body/main/div[2]/section/div/form/div/input')))
mazone.send_keys(diplôme)
mazone.send_keys(Keys.ENTER)


#//*[@id="content"]/div/div/div/div[*]/article/div[2]/h3/a
# //*[@id="content"]/div/div/div/div[3]/article/div[2]/h3/a
# //*[@id="content"]/div/div/div/div[4]/article/div[2]/h3/a
# //*[@id="searchResults"]/li[17]/div/div/div[1]/h4/a

listZoneTitre = WebDriverWait(monpilote, timeout=3).until(expected_conditions.presence_of_all_elements_located ((By.XPATH, '//*[@id="content"]/div/div/div/div[*]/article/div[2]/h3/a')))

time.sleep(1)



a = []
a.append( ['titre'] )
for x in listZoneTitre:
    titre = x.text
    print(titre)
    if titre != "" :  
        r = [titre]
        a.append( r )

print(a)

listZoneDate = WebDriverWait(monpilote, timeout=3).until(expected_conditions.presence_of_all_elements_located ((By.XPATH, '//*[@id="content"]/div/div/div/div[*]/article/div[2]/h3/a')))
b=[]
b.append( ['date'])
for x in listZoneDate:
    date= x.text
    print(date)
    if date != "" :
        r = [date]
        b.append( r )

e=[]
for i in range(len(a)):
    x=a[i][0]
    y=b[i][0]
    r=[x,y]
    e.append(r)

print(e)


import csv
fichier = open( "badraumontpellier.csv" , "w" )
écrivain = csv.writer( fichier , delimiter="," )
écrivain.writerows(e)
fichier.close()

input("pause")

input("Presser une touche pour quitter...")