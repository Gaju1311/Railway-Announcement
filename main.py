import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def textToSpeecheng(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)    

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios: 
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1 - Generate kripya dheyan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_.mp3", format="mp3")

    # 2 is from-city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_.mp3", format="mp3")

    # 6 is to-city

    # 7 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_.mp3", format="mp3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_.mp3", format="mp3")

    # 10 is platform number

    # 11 - Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_.mp3", format="mp3")

    # 12 - May I have your attention please train no.
    textToSpeecheng("may"+" "+"i"+" "+"have"+" "+"your"+" "+"attention"+" "+"please"+"  "+"train"+"number"+" ", '12_.mp3')

    #13 is train no. and name in eng
    
    # 14 - from eng
    textToSpeecheng("from", '14_.mp3')

    #15 from city eng

     # 16 - to eng
    textToSpeecheng("to", '16_.mp3')

    #17 to city eng

     # 18 - via
    textToSpeecheng("via", '18_.mp3')

    #19 via city eng

     # 20 - is ariving shortly on platform no.
    textToSpeecheng("is"+ " "+"ariving"+ " "+"shortly"+ " "+"on"+ " "+"platform"+ " "+"number", '20_.mp3')

    #21 platform no. eng

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from-city
        textToSpeech(item['from'], '2_.mp3')

        # 4 - Generate via-city
        textToSpeech(item['via'], '4_.mp3')
 
        # 6 - Generate to-city
        textToSpeech(item['to'], '6_.mp3')

        # 8 - Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_.mp3')

        # 10 - Generate platform number
        textToSpeech(item['platform'], '10_.mp3')

        # 15 - Generate from-city eng
        textToSpeecheng(item['from'], '15_.mp3')

        # 19 - Generate via-city eng
        textToSpeecheng(item['via'], '19_.mp3')
 
        # 17 - Generate to-city eng
        textToSpeecheng(item['to'], '17_.mp3')

        # 13 - Generate train no and name in eng
        textToSpeecheng(item['train_no'] + " " + item['train_name'], '13_.mp3')

        # 21 - Generate platform number in eng
        textToSpeecheng(item['platform'], '21_.mp3')

        audios = [f"{i}_.mp3" for i in range(1,22)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...") 
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
    

