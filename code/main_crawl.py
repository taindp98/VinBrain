from selenium import webdriver
import os
from time import sleep
def init_browser(url):
    global browser
    browser=webdriver.Firefox(executable_path="./geckodriver")
    browser.get(url)
    sleep(1)
    print('Initial browser...')

def get_page(curr_url):
    list_content = []
    try:
        browser.get(curr_url)
        hrefs = browser.find_elements_by_xpath("//h2[@class='entry-title']//a")
        # print(len(hrefs))
        links_hrefs = [link.get_attribute('href') for link in hrefs]
        
        for href in links_hrefs:
            browser.get(href)
            sleep(0.5)
            dict_content = {}
            title = browser.find_element_by_xpath("//h1[@class='entry-title']").text
            # print('title',title)
            dict_content['title']=title
            content = browser.find_elements_by_xpath("//div[@class='entry-content clear']/p")
            # print('question',content[0].text)
            dict_content['question']=content[0].text
            # print('answer',content[1].text)
            # dict_content['answer'] = content[1].text
            dict_content['answer'] = ','.join([item.text for item in content[1:]])
            sleep(0.5)
            list_content.append(dict_content)
            browser.execute_script("window.history.go(-1)")
            sleep(1)
    except Exception as e:
        print('Fail {}'.format(str(e)))
    return list_content

def next_page(count):
    try:
        link_next_page = browser.find_element_by_xpath("//a[@class='next page-numbers']").get_attribute('href')
        browser.get(link_next_page)
        sleep(0.5)
        count+=1
    except Exception as e:
        print('Fail {}'.format(str(e)))
    return count

def save_data(list_data,path,hos_url,curr_page):
    try:
        folder_name = hos_url.split('/')[2]
        save_path = os.path.join(path,folder_name)
        if not os.path.isdir(save_path):
            os.mkdir(save_path)
        save_page = os.path.join(save_path,str(curr_page)+'.json')
        # save_file = open(os.path.join(save_page,'.json'))
        # dict_final = df_new.to_dict('records')
        # file_out = open('/home/taindp/PycharmProjects/thesis/data/database_full_feature_2019_2020.json','w')
        if not os.path.isfile(save_page):
            open_file = open(save_page,'w')
            for item in list_data:
                item_str = str(item).replace(r"'",r'"')
                open_file.write(item_str)
                open_file.write('\n')
            print('Save successful page: {}'.format(curr_page))
        else:
            print('Web page existing: {}'.format(curr_page))
    except Exception as e:
        print('Fail {}'.format(str(e)))

def get_hospital(hos_url,path,total_page):
    count = 0
    # init_browser(hos_url)
    global browser
    browser=webdriver.Firefox(executable_path="./geckodriver")
    browser.get(hos_url)
    while count != total_page:
        curr_url = str(browser.current_url)
        curr_data = get_page(curr_url)
        sleep(0.5)
        # print('curr_data',curr_data)
        count = next_page(count)
        save_data(curr_data,path,hos_url,count)
        if total_page%50 == 0:
            browser.refresh()


if __name__== '__main__':
    """
    https://bvndtp.org.vn/hoi-dap/
    https://benhlytramcam.vn/hoi-dap-tu-van/
    https://isofhcare.com/cong-dong/Chuyen-khoa-Lao-va-benh-phoi-10
    https://thaythuocvietnam.vn/thay-thuoc-tra-loi/
    https://mekhoebekhoe.com/hoi-dap/suc-khoe-cua-be/


    Crawl: Title, Question, Answer, Tags (optional)

    """
    url = 'https://mekhoebekhoe.com/hoi-dap/suc-khoe-cua-be/'
    path = '../data'
    total_page = 453
    get_hospital(url,path,total_page)
    browser.close()