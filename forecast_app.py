import requests
import webbrowser

#----------------Main Title----------------------------------
print('\n')
print('\t\t\t ' + '-' * 22)
print('\t\t\t|    ' + 'ПРОГНОЗ ПОГОДЫ' + '    |')
print('\t\t\t ' + '-' * 22, "Special thanks to @igor_chubin")
print("~" * 24 + '\t' * 3 + "~" * 30)

#------------User's Input---------------------------------------
your_city = str(input('\n    Ваш город (на английском и с большой буквы Пример: Astrakhan): \n '))

url = 'https://wttr.in/{}'.format(your_city)

#--------------------Open Browser's Page------------------------
reqs = requests.get(url)

webbrowser.open(url, new=1)