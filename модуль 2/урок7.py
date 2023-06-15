from gtts import gTTS

my_file = open("test.txt", "r", encoding = "utf-8")
my_str = my_file.read()

render = gTTS(text=my_str, lang="ru")


my_file.close()
render.save("nikita")