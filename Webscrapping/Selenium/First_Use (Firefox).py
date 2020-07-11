from selenium import webdriver

MAX_PAGE_NUMBER = 5
MAX_PAGE_DIGIT = 3

# Buyers | Price
# name1    price1
# name2    price2
# etc.
with open('result.csv', 'w') as file:
    file.write("Buyers, Price \n")

# Open up a firefox browser and navigate to web page
driver = webdriver.Firefox()

for page in range(1, MAX_PAGE_NUMBER+1):

    page_num = (MAX_PAGE_DIGIT - len(str(page))) * '0' + str(page)
    url = f'https://econpy.pythonanywhere.com/ex/{page_num}.html'

    driver.get(url)

    # Extract lists of 'buyers' and 'prices' based on xpath
    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

    # Print to csv file all of the buyers and prices on current page
    num_page_items = len(buyers)
    with open('result.csv', 'a') as file:
        for iterator in range(num_page_items):
            print(buyers[iterator].text + "," + prices[iterator].text, file=file)

# Close browser once task is completed
driver.close()
