from translate import Translator


message = "Hello, do you want to visit?"

temp = message.split(" ")

sentence = ""

translator_fr = Translator(to_lang="fr", from_lang="en")
translator_en = Translator(to_lang="en", from_lang="fr")

translation = translator_fr.translate(message)

for word in temp:

  sentence += (translator_fr.translate(word) + " ")
  

print(translation)
print(translator_en.translate(translation))

print(sentence)
print(translator_en.translate(sentence))
