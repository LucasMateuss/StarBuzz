from time import sleep
import urllib.request


def achaPreco(url):
    pagina = urllib.request.urlopen(url)
    texto  = pagina.read().decode("utf8")
    inicio  = texto.find(">$") + 2
    fim = inicio + 4
    preco  = texto[inicio:fim]
    return(float(preco))

def menorPreco():
    while True:
        cliente = achaPreco('http://beans.itcarlow.ie/prices.html')
        clienteFidelidade = achaPreco('http://beans.itcarlow.ie/prices-loyalty.html')

        menorValor = (cliente if cliente < clienteFidelidade else clienteFidelidade)
        site = "Cliente" if menorValor == cliente else "Cliente Fidelidade"
        link = 'http://beans.itcarlow.ie/prices.html' if site == 'Cliente' else 'http://beans.itcarlow.ie/prices-loyalty.html'
        precoMinimo = 4.7
        if cliente <= precoMinimo or clienteFidelidade <= precoMinimo:
            print(f'Compra agora no site {site}\nPreço: {menorValor}')
            break
        else:
            print('Espere')
            sleep(2)
    return f"""<p>Preço Baixou!! - Preço: U${menorValor:.2f} - Acesse a página do {site}</p>
    <p>Link: {link}.</p>"""

def enviar_email():  
    import win32com.client as win32
    outlook = win32.Dispatch("Outlook.Application")
    message =  outlook.CreateItem(0)
    message.Display()
    message.To = "lucasmateus290903@gmail.com"
    message.Subject = 'Preço do café'
    message.Body =  ""
    body = f"""
    <p>{menorPreco()}</p>
    """
    message.HTMLBody = body 
    message.Send()


if __name__ == "__main__":
    enviar_email()
