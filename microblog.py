from flask import Flask

# criação do app
app = Flask("Microblog")

# é um programa ligado na internet, que receberá visitantes, e portanto, precisa de rotas. O flask faz a junção entre uma URL e uma função do python

# farei algo relacionado ao app e a função embaiixo
# essa "/" significa que quando entrarem no dominio www.ocean.com.br/, a função se executará (/ é a home, a URL básica)
# o @ é um decorator, ele fica em cima da função e faz algo com ela; o route pega a função abaixo e a URL entre parenteses, e as liga

@app.route("/")
def index():
    return "Olá mundo"

# linha de execução dentro do python

app.run()