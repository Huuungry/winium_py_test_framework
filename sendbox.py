from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui

driver = webdriver.Remote('http://134.132.239.40:9999',
               {"debugConnectToRunningApp":"true"})

def find_element(search):
    search_result = driver.find_element_by_name(search)
    return search_result

def get_xy(element1):
    xystring = element1.get_attribute("ClickablePoint")
    xylist = xystring.split(",")
    x= int(xylist[0])
    y = int(xylist[1])
    return x, y

def drag_and_drop(element, ofsetX=0, ofsetY=0):
    pyautogui.mouseDown(get_xy(element)[0], get_xy(element)[1])
    pyautogui.dragTo(get_xy(element)[0]+ofsetX, get_xy(element)[1]+ofsetY)
    pyautogui.mouseUp()

drag_and_drop(find_element("depthbrick.bri, UPGRADE"),500,300)