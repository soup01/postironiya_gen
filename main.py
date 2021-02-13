# для работы с api
import requests
import json
# для создания демотиваторов. ну да, мне лень самому было делать код 
from simpledemotivators import demcreate 

# "генерация" рандомной фотки еды
food = requests.get("https://foodish-api.herokuapp.com/api/")
imgurl = requests.get(json.loads(food.text)["image"])
with open("img.jpg", "wb") as out:
	out.write(imgurl.content)

# "генерация" рандомного текста
panch = requests.get(f"https://fish-text.ru/get?{'&type=sentence&number=1'}")
text = json.loads(panch.text)["text"]

# этот кусок кода делит текст на 2 части
a = 0
upper_text = ""
lower_text = ""
for i in text.split():
	if a >= round(len(text.split())/2):
		lower_text = f"{lower_text}{i} "
	else:
		upper_text = f"{upper_text}{i} "
	a += 1

# создание демотиватора
dem = demcreate(upper_text, lower_text)
dem.makeImage('img.jpg')
