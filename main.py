import time
from selenium import webdriver
import pickle
from Product import Product
import json

'''
worten
'''
product_name_class_worten = "w-product__title"
product_price_main_class_worten = "w-product-price__main"
product_price_dec_class_worten = "w-product-price__dec"
product_price_current_class_worten = "w-currentPrice"

'''
fnac
'''
product_name_class_fnac = "js-Search-hashLink"
product_price_current_class_fnac = "floatl"


# -------------------------- WORTEN --------------------------
def get_all_products_by_string_worten(search_string):
    products_result = []
    options = webdriver.ChromeOptions()
    options.add_argument("--window-position=-32000,-32000")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path=r"D:\Programs\chromedriver_win32\chromedriver.exe", chrome_options=options)
    #options.add_argument("--window-position=-32000,-32000")
    driver.get(build_search_string_worten(search_string))

    time.sleep(2)
    driver.find_elements_by_class_name("w-button-primary")[0].click()
    time.sleep(5)

    products_name = driver.find_elements_by_class_name(product_name_class_worten)
    products_price_main = driver.find_elements_by_class_name(product_price_main_class_worten)
    products_price_dec = driver.find_elements_by_class_name(product_price_dec_class_worten)
    products_price_current = driver.find_elements_by_class_name(product_price_current_class_worten)

    for i in range(len(products_name)):
        if search_string.upper() in products_name[i].text.upper():
            price_main = products_price_current[i].find_elements_by_tag_name("span")[0].find_elements_by_class_name(product_price_main_class_worten)[0].text
            price_dec = products_price_current[i].find_elements_by_tag_name("span")[0].find_elements_by_class_name(product_price_dec_class_worten)[0].text
            products_result.append(Product(products_name[i].text, float(price_main + "." + price_dec), "Worten"))

    for product in products_result:
        product.printProductInfo()

    driver.close()
    driver.quit()

    return products_result

# -------------------------- FNAC --------------------------
def get_all_products_by_string_fnac(search_string):
    products_result = []
    options = webdriver.ChromeOptions()
    options.add_argument("--window-position=-32000,-32000")

    driver = webdriver.Chrome(executable_path=r"D:\Programs\chromedriver_win32\chromedriver.exe")
    driver.get(build_search_string_fnac(search_string))

    time.sleep(2)

    products_name = driver.find_elements_by_class_name(product_name_class_fnac)
    products_price_current = driver.find_elements_by_class_name(product_price_current_class_fnac)

    for i in range(len(products_name)):
        if search_string.upper() in products_name[i].text.upper():
            price = products_price_current[i].find_elements_by_class_name("userPrice")[0].text
            price_as_float = price.replace(" ", "").replace(",", ".").replace("€", "")
            products_result.append(Product(products_name[i].text, float(price_as_float), "Fnac"))

    for product in products_result:
        product.printProductInfo()

    driver.close()
    driver.quit()

    return products_result


def build_search_string_worten(search_string):
    base_string = "https://www.worten.pt/search?query="
    search_string_array = search_string.split()

    for i in range(len(search_string_array)):
        if i == 0:
            base_string = base_string + search_string_array[i]
        else:
            base_string = base_string + "+" + search_string_array[i]

    return base_string


def build_search_string_fnac(search_string):
    base_string = "https://www.fnac.pt/SearchResult/ResultList.aspx?SCat=0%211&Search="
    search_string_array = search_string.split()

    for i in range(len(search_string_array)):
        if i == 0:
            base_string = base_string + search_string_array[i]
        else:
            base_string = base_string + "+" + search_string_array[i]

    return base_string + "&sft=1&sa=0"


def product_list_to_json(filename, list):
    return json.dumps(list, default=vars)

if __name__=='__main__':
    print("Price Comparison started!")
    print("------------------------")
    #get_all_products_by_string_worten("iphone 12")
    get_all_products_by_string_fnac("iphone 12")
