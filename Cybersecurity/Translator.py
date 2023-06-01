from translate import Translator
translator = Translator(to_lang="es")

try:
    with open('Translate.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('translationfile.txt', mode ='w') as my_file2:
            my_file2.write(translation)
        print(translation)
except FileNotFoundError as err:
    print('file does not exist')