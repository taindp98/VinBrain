from selenium import webdriver
import os
from time import sleep
def init_browser(url):
    global browser
    browser=webdriver.Firefox(executable_path="./geckodriver")
    browser.get(url)
    sleep(1)
    print('Initial browser...')

def scroll_page():
    # scroll ---> extra page
    sleep(0.5)
    last_height = browser.execute_script("return document.body.scrollHeight")
    # browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    new_height = browser.execute_script('window.scrollTo(0, window.scrollY + 1096);')
    # if new_height == last_height:
    #     sys.exit()
    print('Scrolling...')
    sleep(0.5)
    press_extra()
    print('Scrolled...')
    return True

def press_extra():
    try:
        read_more = browser.find_elements_by_xpath("//div[@class='q-text qu-cursor--pointer QTextTruncated__StyledReadMoreLink-sc-1pev100-2 cDraHQ qt_read_more qu-color--blue_dark qu-fontFamily--sans qu-pl--tiny']")
        print('Page extra..')
        for r in read_more:
            r.click()
            sleep(0.2)
    except Exception as e:
        print('Fail cause {}'.format(str(e)))
        # continue
        


def get_page(curr_url,limit_step):
    list_content = []
    try:
        browser.get(curr_url)
        ## scroll page
        scroll_step = 0
        while scroll_step != limit_step:
            scroll = scroll_page()
            if scroll:
                ## count posts
                posts = browser.find_elements_by_xpath("//div[@class='q-text puppeteer_test_question_title']")
                print('The numbers of posts: {}'.format(len(posts)))
                spans = browser.find_elements_by_css_selector('span.q-box.qu-userSelect--text')
                for span in spans:
                    print(span.text)
                    print('-' * 80)
        # hrefs = browser.find_elements_by_xpath("//h2[@class='entry-title']//a")
        # print(len(hrefs))
        # links_hrefs = [link.get_attribute('href') for link in hrefs]
        
        # for href in links_hrefs:
            # browser.get(href)
            # sleep(0.5)
            # dict_content = {}
            # title = browser.find_element_by_xpath("//h1[@class='entry-title']").text
            # print('title',title)
            # dict_content['title']=title
            # content = browser.find_elements_by_xpath("//div[@class='entry-content clear']/p")
            # print('question',content[0].text)
            # dict_content['question']=content[0].text
            # print('answer',content[1].text)
            # dict_content['answer'] = content[1].text
            # dict_content['answer'] = ','.join([item.text for item in content[1:]])
            # sleep(0.5)
            # list_content.append(dict_content)
            # browser.execute_script("window.history.go(-1)")
            # sleep(1)
    except Exception as e:
        print('Fail {}'.format(str(e)))
    return list_content


# def save_data(list_data,path,quora_url,curr_page):
#     try:
#         folder_name = quora_url.split('/')[2]
#         save_path = os.path.join(path,folder_name)
#         if not os.path.isdir(save_path):
#             os.mkdir(save_path)
#         save_page = os.path.join(save_path,str(curr_page)+'.json')
#         # save_file = open(os.path.join(save_page,'.json'))
#         # dict_final = df_new.to_dict('records')
#         # file_out = open('/home/taindp/PycharmProjects/thesis/data/database_full_feature_2019_2020.json','w')
#         if not os.path.isfile(save_page):
#             open_file = open(save_page,'w')
#             for item in list_data:
#                 item_str = str(item).replace(r"'",r'"')
#                 open_file.write(item_str)
#                 open_file.write('\n')
#             print('Save successful page: {}'.format(curr_page))
#         else:
#             print('Web page existing: {}'.format(curr_page))
#     except Exception as e:
#         print('Fail {}'.format(str(e)))

def get_stroke(quora_url,path):
    count = 0
    # init_browser(quora_url)
    global browser
    browser=webdriver.Firefox(executable_path="./geckodriver")
    browser.get(quora_url)
    limit_step = 5
    # while count != total_page:
    curr_url = str(browser.current_url)
    curr_data = get_page(curr_url,limit_step)
    sleep(0.5)
    # print('curr_data',curr_data)
    # count = next_page(count)
    # save_data(curr_data,path,quora_url,count)
    # if total_page%50 == 0:
        # browser.refresh()


if __name__== '__main__':
    """

    """
    # url = 'https://mekhoebekhoe.com/hoi-dap/suc-khoe-cua-be/'
    url = 'https://www.quora.com/search?q=stroke&time=week&type=question'
    path = '../data'
    # total_page = 453
    get_stroke(url,path)
    browser.close()