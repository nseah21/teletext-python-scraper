from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def scrape_data():
    URL = "https://www.singaporepools.com.sg/en/product/Pages/4d_results.aspx"
    LATEST_DRAW_XPATH = "/html/body/form/div[5]/div[1]/div/section/div/div/div/span/section/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/ul/li[1]/div"

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    latest_draw = driver.find_element(By.XPATH, LATEST_DRAW_XPATH)
    data = latest_draw.text.split("\n")

    driver.quit()

    date, id = map(lambda token: token.strip(), data[0].split("Draw No."))
    first, second, third = map(lambda arr: arr[-4:], data[1:4])
    starter = " ".join(data[5:10]).split(" ")
    consolation = " ".join(data[11:16]).split(" ")

    results = {
        "date": date,
        "id": id,
        "first": first,
        "second": second,
        "third": third,
        "starter": starter,
        "consolation": consolation,
    }

    return results
