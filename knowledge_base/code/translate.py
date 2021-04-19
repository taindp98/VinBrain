# from googletrans import Translator
from google_trans_new import google_translator  
translator = google_translator()  
translate_text = translator.translate('You may hear it called things like Constant Spring, Cooley’s anemia, or hemoglobin Bart’s hydrops fetalis. These are common names for different forms of it',lang_tgt='vi')  
# translator = Translator()
# kk = translator.detect('이 문장은 한글로 쓰여졌습니다.')
# kk  = translator.translate('hi good morning', dest='vi',src= 'en')
# 
print(translate_text)