from instabot.bot import *
from getpass import getpass

if __name__ == "__main__":

    funcao = ''
    hashtags = ['floresta', 'casa']
    comentarios = ["Show!", "Curti!", "Bela foto!", "S2 S2", "Amei!", "STATUS ATUAL: APAIXONADA!"]

    username = input('Qual o usuário?')
    password = getpass(prompt='Qual a senha?')

    while True:
        seleciona_funcao = input('Para apenas comentar,digite 1. \nPara apenas dar like, digite 2. '
                                 '\nPara comentar e dar like, digite 3. \n')
        if seleciona_funcao == '1':
            funcao = 'comentar_fotos(comentarios)'
            break
        elif seleciona_funcao == '2':
            funcao = 'like_foto()'
            break
        elif seleciona_funcao == '3':
            funcao = 'like_comentar(comentarios)'
            break
        else:
            print('Valor invalido!')

    instagram = InstagramBot(username, password)
    instagram.login()

    while True:
        try:
            tag = random.choice(hashtags)
            instagram.selecionar_fotos(tag)
            eval('instagram.' + funcao)
            hashtags.remove(tag)
        except Exception:
            instagram.close_browser()
            time.sleep(60)
            instagram = InstagramBot(username, password)
            instagram.login()
