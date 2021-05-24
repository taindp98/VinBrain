from selenium import webdriver
import os
from time import sleep
import requests
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import datetime,date
import uuid
from tqdm import  tqdm


def init_browser(url):
    global browser
    browser=webdriver.Firefox(executable_path="./geckodriver")
    browser.get(url)
    sleep(0.5)
    print('Initial browser...')

def scroll_page():
    # scroll ---> extra page
    # sleep(0.5)
    last_height = browser.execute_script("return document.body.scrollHeight")
    # browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    new_height = browser.execute_script('window.scrollTo(0, window.scrollY + 2048);')
    # if new_height == last_height:
    #     sys.exit()
    print('Scrolling...')
    sleep(1)
    press_extra()
    print('Scrolled...')
    return True

def press_extra():
    try:
        read_more = browser.find_elements_by_xpath("//div[@class='q-text qu-cursor--pointer QTextTruncated__StyledReadMoreLink-sc-1pev100-2 cDraHQ qt_read_more qu-color--blue_dark qu-fontFamily--sans qu-pl--tiny']")
        print('Read more ..')
        for r in read_more:
            r.click()
            sleep(0.5)
    except Exception as e:
        print('Fail cause {}'.format(str(e)))
        # continue
        


def get_page(curr_url,path):
    # list_content = []
    today_time = date.today().strftime("%m_%d_%Y") + '_' + datetime.now().strftime("%H_%M")
    save_path = os.path.join(path,str(today_time)+'.json')
    save_file = open(save_path,mode='a+', encoding='utf-8')
    try:
        browser.get(curr_url)
        ## scroll page
        scroll_step = 0
        ## pointer is last question index of current scroll
        pointer = 0
        break_signal = 0
        while True:
            scroll = scroll_page()
            if scroll:
                ## count posts
                # posts_origin = browser.find_elements_by_xpath("//a[@class='q-box qu-display--block qu-cursor--pointer qu-hover--textDecoration--underline Link___StyledBox-t2xg9c-0 roKEj']")
                posts_origin = browser.find_elements_by_xpath("//div[@class='CssComponent-sc-1oskqb9-0 cXjXFI']")
                ## cut posts follow pointer
                print('='*50)
                print('current url', curr_url)
                print('scroll step',scroll_step)
                print('pointer',pointer)
                print('num posts',len(posts_origin))

                if pointer == len(posts_origin):
                	break_signal += 1
                    # break
                if break_signal == 10:
                	break
                posts = posts_origin[pointer:]
                
                pointer = len(posts_origin)

                # hrefs = [item.get_attribute('href') for item in posts] 

        		# print('extracting post')

                for post in posts:
                    # print('>'*50)
                    dict_question_ans = {}
                    spans = post.find_elements_by_css_selector('span.q-box.qu-userSelect--text')                    # q-box qu-userSelect--text
                    # tag_answers = post.find_elements_by_xpath("//p[@class='q-text qu-display--block']")
                    # tag_answers = post.find_elements_by_xpath("//span[@style='font-weight: normal; font-style: normal; background: rgba(46, 105, 255, 0.2);']")                        
                    # answers = []
                    # print('>'*20)
                    # print(len(spans))
                    # for span in spans:
                        # print(span.text)
                        # print('-'*50)

                    # for ans in tag_answers:
                        # print(ans.text)
                        # answers.append(ans.text)
                    # if len(spans) > 1:
                    dict_question_ans['_id'] = str(uuid.uuid4())[:8]
                    dict_question_ans['question'] = spans[0].text
                    # dict_question_ans['answers'] = answers
                    if len(spans) > 1:
                        dict_question_ans['answers'] = spans[1].text
                    else:
                        dict_question_ans['answers'] = ''
                    # print(dict_question_ans)
                    # save_data(dict_question_ans,path)
                    json.dump(dict_question_ans,save_file,ensure_ascii=False)
                    save_file.write('\n')
                scroll_step += 1
            else:
                break
    except Exception as e:
        print('Fail {}'.format(str(e)))
        pass
def get_stroke(search_term,path):
    global browser
    browser=webdriver.Firefox(executable_path="./geckodriver")
    quora_url = 'https://www.quora.com/search?q={}&type=question'.format(search_term.replace(' ','%20'))
    browser.get(quora_url)
    curr_url = str(browser.current_url)
    curr_data = get_page(curr_url,path)
    # sleep(0.5)


if __name__== '__main__':
    """

    """
    # url = 'https://mekhoebekhoe.com/hoi-dap/suc-khoe-cua-be/'
    # url = 'https://www.quora.com/search?q=stroke&time=week&type=question'
    # urls = ['https://www.quora.com/search?q=stroke%20disease&type=question',
            # 'https://www.quora.com/search?q=stroke&type=question'
            # ]
    # path = '../data'
    path = '../../resource/stroke'
    # total_page = 453
    # search_terms = ['stroke disease','stroke','ischemic stroke',"white stroke", "blood pressure", "red stroke", "high blood", "brain hemorrhage", "factors stroke", "prevent stroke", "related stroke", "sah stroke", "stroke recovery", "advice stroke", "manage stroke", "choice stroke", "recover stroke", "blood clot", "cause stroke", "white strokes", "transient stroke", "stroke occurs", "risk stroke", "red strokes","stroke effect"]
    search_terms = ["white strokes", "transient stroke", "stroke occurs", "risk stroke", "red strokes","stroke effect"]
    # for url in urls[1:]:
    for term in search_terms:
        get_stroke(term,path)
        # browser.close()