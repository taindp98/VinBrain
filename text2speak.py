# import requests




# def get_token(subscription_key):
#     fetch_token_url = 'https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken'
#     headers = {
#         'Ocp-Apim-Subscription-Key': subscription_key
#     }
#     response = requests.post(fetch_token_url, headers=headers)
#     access_token = str(response.text)
#     print(access_token)

# get_token(subscription_key)

from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig


subscription_key = '931c9038-e3d1-45c1-8f6c-5da5f27de8c7'

speech_config = SpeechConfig(subscription=subscription_key, region="westus2")

audio_config = AudioOutputConfig(filename="./audio/test_19apr.wav")

synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
synthesizer.speak_text_async("chào bạn")
