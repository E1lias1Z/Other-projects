import requests
import webbrowser

print('\n')
print('\t\t\t ' + '-' * 22)
print('\t\t\t|    ' + 'ПРОГНОЗ ПОГОДЫ' + '    |')
print('\t\t\t ' + '-' * 22, "Special thanks to @igor_chubin")
print("~" * 24 + '\t' * 3 + "~" * 30)

your_city = str(input('\n    Ваш город (на английском и с большой буквы Пример: Astrakhan): \n '))

url = 'https://wttr.in/{}'.format(your_city)

reqs = requests.get(url)

webbrowser.open(url, new=1)