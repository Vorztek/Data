from selenium import webdriver
import os
import time


def erasefile():
    path = r"C:\Users\SK6138\OneDrive - ENGIE\Dashboard\Sources de données_maison\Stockage"
    for filename in os.listdir(path):
        os.remove(path + "/" + filename)


def downloads():
    # Configuration
    # Changer le répertoire de destination du DL :
    prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory": r"C:\Users\SK6138\OneDrive - ENGIE\Dashboard\Sources de "
                                           r"données_maison\Stockage",
             "directory_upgrade": True}

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", prefs)
    #options.add_argument('--headless')

    driver = webdriver.Chrome(
        r"C:\Users\SK6138\OneDrive - ENGIE\Dashboard\Sources de données_maison\chromedriver_win32\chromedriver.exe",
        options=options)
    # Lancer Chrome

    driver.get("https://engiegbs.service-now.com")

    # iframe = driver.find_element_by_xpath("iframe[id='gsft_main']")$
    # driver.switch_to.frame()

    time.sleep(2)

    # driver.find_element_by_name( "username" ).send_keys( "SK6138" )
    # driver.find_element_by_name( "password" ).send_keys( "" )
    time.sleep(3)
    # driver.find_element_by_id( "okta-signin-submit" ).click()
    time.sleep(5)
    # driver.find_element_by_xpath(
    #    "/html/body/div[2]/div[2]/main/div[2]/div/div/form[1]/div[2]/input" ).click()  # Envoie la notif push sur le
    # téléphone

    time.sleep(7)

    driver.get("https://engiegbs.service-now.com")

    time.sleep(10)
    # Téléchargement des fichiers

    # Rapport Feedback
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=5e4ca2311be66c90f2fffc07cb4bcbd0")

    # Knowledge : Contenu
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=8036343b1b366c509c75102c9b4bcb6d")

    # KB_use (la globale), 7 jours | fichier : KB_use
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=69cd514adb32e8507261e03cd396195a")

    # KB_use Ce mois ci | fichier : Kb_use (1)
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=f9c31b2c1b072c9094f4b9918b4bcb02")

    # KB_use janvier | fichier : kb_use 2
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=733d569c1b07ac909c75102c9b4bcb1a")

    # KB_use 6 mois | fichier : kb_use 3
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=e1e9a3631bfaa8509c75102c9b4bcb2e")

    # KB_use 7 jours | fichier : kb_use 4
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=69cd514adb32e8507261e03cd396195a")

    # KB_use Ratio Desk/Hors Desk 7 jours | fichier kb_use 5
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=6a8b55c6dbfea8507261e03cd3961997")

    # KB_use Lemoisdernier | fichier kb_use 6
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=6bebf082db8fe8508415db15f3961923")

    # KB_use Today | fichier kb_use 7
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=f21de993db47a8108415db15f3961973")

    # KB_use Lemoisdernier Desk | fichier kb_use 8
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=d35cbd53db0ba8108415db15f3961993")

    # KB_use Consultation Février | fichier kb_use 9
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=593ea3ecdb176010c2e463cad3961914")

    # Incident 30 jours | fichier : Incident
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=2a773c741bc7ec9094f4b9918b4bcb1f")

    # Incident Le mois dernier | fichier : Incident 1
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=5d71019cdb5fac50c2e463cad396197a")

    # AI | KB_INCIDENT RELIE2 | Le mois dernier | fichier Incident2
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=953ab5111ba3681094f4b9918b4bcb9c#")

    # AI | KB_INCIDENT RELIE | 6 mois | fichier Incident3
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?&CSV&jvar_report_id=4f87d39a1b2fe85094f4b9918b4bcbfc")
    time.sleep(10)
    # AI | KB_INCIDENT| 6 mois | fichier Incident 4
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=d9f0eeae1ba3ec5094f4b9918b4bcb9b#")

    # AI | KB_INCIDENT RELIE| Ce mois-ci | fichier Incident 5
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=42a6a8111b332c508b3fbbb88b4bcbd8")

    # AI | KB_USE DESK| Ce mois ci | fichier KB use 10
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=cb0a289d1b732c508b3fbbb88b4bcbe6")

    # AI | Knowledge base | Last month | fichier kb_knowledge 1
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=658abd401b8430109c75102c9b4bcbc6")

    # AI | Knowledge base | Ce mois_ci | fichier kb_knowledge 2
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=07b09b31db332410c2e463cad396199b")

    # AI | KB_use | Yesterday | fichier KB_use 11 
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=450811ce1bf47c1052defd509b4bcb85")

    # AI | KB_use Desk | Yesterday | fichier KB_use 12 
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=854dd1421b787c1052defd509b4bcb74")

    # AI | Incident | Yesterday | fichier Incident 6
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=18de51c21b787c1052defd509b4bcbc1")

    # AI | KB_use | Last week | fichier KB_use 13
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=bea5e9ee1bb0f410759641939b4bcb8e")

    # AI | kb_knowledge | Last week | fichier knowledge_use 3
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=a8e744fe1bbc7810759641939b4bcb46")

    # AI | Incident relié | Last week | fichier Incident 7
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=5623b14f1bb07450759641939b4bcb13")

    # AI | Incident | Last week | fichier Incident 8
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=5993f9431bf07450759641939b4bcb33")

    # AI | KFT | Last week | fichier KFT
    driver.get(
        "https://engiegbs.service-now.com/sys_report_template.do?CSV&jvar_report_id=286bb9ef1bf8f01052defd509b4bcb02")



    # Fin des rapports :
    time.sleep(10)
    # Quitter Chrome
    driver.quit()


erasefile()
downloads()
