from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
import csv 


options = webdriver.ChromeOptions()
try:
    try:
        global driver
        driver_path = ChromeDriverManager().install()
        driver = webdriver.Chrome(service=Service(driver_path), options=options)
    except Exception as e:
        print("Error occurred while automatically downloading ChromeDriver:", e)
        print("Using ChromeDriver from the current folder if available.")
        
        current_folder_driver_path = os.path.join(os.getcwd(), "chrome.exe")
        
        if os.path.exists(current_folder_driver_path):
            try:
                driver = webdriver.Chrome(executable_path=current_folder_driver_path, options=options)
            except Exception as e:
                print("Error occurred while using ChromeDriver from the current folder:", e)
                print("Please ensure you have a compatible chromedriver executable in your current folder.")
                driver = None
        else:
            print("No chromedriver executable found in the current folder.")
            driver = None
except:
    print('error')
# url=driver.get('https://www.amazon.in/s?k=grocery+items&ref=nb_sb_noss')
# url = driver.get("https://www.amazon.in/s?k=footwear&crid=31Q7KTKIPMAX2&sprefix=footwear%2Caps%2C275&ref=nb_sb_noss_1'")
# url=driver.get("https://www.amazon.in/s?k=fashion&crid=2I6H1NGTWB3Y0&sprefix=fashion%2Caps%2C284&ref=nb_sb_noss_1")
# url=driver.get('https://www.amazon.in/s?k=electronics&sprefix=electro%2Caps%2C304&ref=nb_sb_ss_ts-doa-p_3_7')
# sleep(2)

# url = driver.get("https://www.amazon.in/s?k=Clothing+%26+Apparel&crid=2SF1OORE1RSTU&sprefix=clothing%2Caps%2C258&ref=nb_sb_noss_2")
# url = driver.get("https://www.amazon.in/s?k=Games+%26+Toys&crid=P0PVGBJKWH39&sprefix=games+%26+toys%2Caps%2C461&ref=nb_sb_noss_1")
# url = driver.get("https://www.amazon.in/s?k=Veterinary+%26+Pet+Items&crid=17E9SCCB7VZ3N&sprefix=veterinary+%26+pet+items%2Caps%2C319&ref=nb_sb_noss")
# url = driver.get("https://www.amazon.in/s?k=Stationery&ref=nb_sb_noss")

# url = driver.get("https://www.amazon.in/s?k=Hand+%26+Power+Tools&crid=22M9G8PF27SB4&sprefix=hand+%26+power+tools%2Caps%2C407&ref=nb_sb_noss_2")
# url = driver.get('https://www.amazon.in/s?k=Tupperware&crid=2KM8G9ASYF050&sprefix=hand+%26+power+tools%2Caps%2C438&ref=nb_sb_noss_2')
# url = driver.get("https://www.amazon.in/s?k=furniture&sprefix=furni%2Caps%2C315&ref=nb_sb_ss_ts-doa-p_1_5")
url=driver.get("https://www.amazon.in/s?k=sports+equipment&sprefix=sports+eq%2Caps%2C291&ref=nb_sb_ss_ts-doa-p_1_9")

driver.maximize_window()

L=[]
wait = WebDriverWait(driver, 10)

kellogs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.rush-component')))

for watch in kellogs:
    try:
        ankar = watch.find_element(By.TAG_NAME, 'a')
        urls = ankar.get_attribute("href")
        # print(urls)
        L.append(urls)
    except Exception as e:
        # print("Error:", e)
        pass

products = []
for url in L:
    
    # try:
    #     # Find and extract the data for a single product
    #     heading = driver.find_element(By.ID, 'productTitle').text
    #     print(heading)
    #     price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[1]/td[2]').text
    #     print(price)
    #     # Collect the descriptions
    #     description_elements = driver.find_elements(By.CLASS_NAME, 'a-list-item')
    #     description = ' '.join(item.text for item in description_elements)
    #     print(description)
    #     # Extract the image URL
    #     image = driver.find_element(By.CLASS_NAME, 'imgTagWrapper')
    #     img = image.find_element(By.TAG_NAME, 'img')
    #     img_1 = img.get_attribute('src')
    #     print(img_1)
    #     # Add the product data to the products list as a dictionary
    #     products.append({"Product Name": heading, "Product Price": price, "Product Description": description, "Product Images": img_1})

    # except:
    #     pass
    
    try:
        driver.get(url)
        # Find and extract the data for a single product
        heading = driver.find_element(By.ID, 'productTitle').text
        print(heading)
        price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
        print(price)
        # Collect the descriptions
        description_elements = driver.find_elements(By.CLASS_NAME, 'a-spacing-mini')
        description = ' '.join(item.text for item in description_elements)
        print(description)
        
        wait = WebDriverWait(driver, 10)
        image_wrapper = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'imgTagWrapper')))

        # Find the image element within the wrapper
        img = image_wrapper.find_element(By.TAG_NAME, 'img')

        # Get the src attribute of the image element
        img_src = img.get_attribute('src')
        print(img_src)
        # Add the product data to the products list as a dictionary
        products.append({"Product Name": heading, "Product Price": price, "Product Description": description, "Product Images": img_src})

    except:
        pass
    # if products!=[]:
    #     break
    # else:
    #     continue

# Save the data to a CSV file
csv_file = 'amazon_sports_products.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["Product Name", "Product Price", "Product Description", "Product Images"]
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()
    csvwriter.writerows(products)

# Remember to close the browser when you're done
driver.quit()