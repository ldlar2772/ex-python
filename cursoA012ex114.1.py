import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/tratamento-de-erros-em-python/modulos/exercicio-114-site-esta-acessivel/')
except:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso.')