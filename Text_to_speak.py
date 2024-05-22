from gtts import gTTS
import os

Text = "สวัสดีครับ ผมชื่อเชน หวังว่าอาจารย์จะรับผมเป็นลูกศิษย์ด้วยนะครับ"

X = gTTS(Text, lang='th')
X.save("output.mp3")

os.system("start output.mp3")