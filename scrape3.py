#     CHK INFO
# import builtwith
# w = builtwith.parse('https://authoraditiagarwal.com')
# print(w)

#     CHECK INFO
# import whois
# print(whois.whois('aiktc.ac.in'))
# from selenium import webdriver
# driver = webdriver.Chrome('/home/aiktc/Desktop/WEB SCRAPPING/day3/chromedriver')
# search_query='AIKTC'
# driver.get('https://www.youtube.com/results?search_query='+search_query)

#     TO CHECK WHETHER IT IS WORKING OR NOT
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# browser = webdriver.Chrome('/home/aiktc/Desktop/WEB SCRAPPING/day3/chromedriver')
# browser.get("http://www.google.com")
# try:
#     assert "Google" in browser.title
#     print('Assert Success')
# except Exception as e:
#     print('Assertion Failed')
# browser.close()

#     FOR FACEBOOK
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome('/home/aiktc/Desktop/WEB SCRAPPING/day3/chromedriver')
# browser.get("https://www.facebook.com/campaign/landing.php?campaign_id=1653993517&extra_1=s%7Cc%7C318504236042%7Ce%7Cfacebook%20%27%7C&placement=&creative=318504236042&keyword=facebook%20%27&partner_id=googlesem&extra_2=campaignid%3D1653993517%26adgroupid%3D63066387003%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D1t1%26target%3D%26targetid%3Dkwd-360705453827%26loc_physical_ms%3D9040246%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMIpdjzqfGG5QIVV4myCh1zbwwuEAAYASAAEgJP1vD_BwE")
# log = browser.find_element_by_id("u_0_b")
# log.click()
# username = browser.find_element_by_id("email")
# password = browser.find_element_by_id("pass")
# login = browser.find_element_by_id("u_0_c")
# username.send_keys("myemail")
# password.send_keys("mypassword")
# login.click()

#     GMAIL FAILED
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome('/home/aiktc/Desktop/WEB SCRAPPING/day3/chromedriver')
# browser.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
# usernamec = browser.find_element_by_id("identifierId")
# usernamec.click()
# username = browser.find_element_by_id("rFrNMe KSczvd uyaebd vHVGub zKHdkd sdJrJc Tyc9J")
# next = browser.find_element_by_class_name("RveJvd snByac")
# username.send_keys("myemail")
# next.click()

#     FOR TWITTER FAILED
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# browser = webdriver.Chrome('/home/aiktc/Desktop/WEB SCRAPPING/day3/chromedriver')
# browser.get("https://twitter.com/login/en")
# username = browser.find_element_by_name("session[username_or_email]")
# password = browser.find_element_by_name("session[password]")

# # login = browser.find_element_by_name("submit EdgeButton EdgeButton--primary EdgeButtom--medium")
# username.send_keys('myemail')
# password.send_keys('mypassword')
# # login.click()

