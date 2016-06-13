# RecognizerLinkChallenge

Reconhecimento de Estruturas de Links.

# Como funciona

Criei 3 arquivos: 1 de base (xml), um serviço python que consulta a base e mantem a base em pé e aguardando requests de link feitos pelo arquivo shopback.php

Para rodar o shopback.py você precisa da base xmllojas.xml na mesma pasta, criei tudo no mesmo arquivo porém a idéia é ter um pool de arquivos xml e quando o arquivo restartar (preferencialmente de 1h em 1h em um cron) novas bases possam entrar, não fiz isso porém a modificação não seria dificil.

Voce precisara do python instalado e do modulo untangle para instala-lo é só ter o modulo pip instalado em seu computador e rodar o comando pip install untangle

Para colocar o servico python de pé é só rodar o comando python shopback.py -s <uma porta que devera estar tambem no .php>

Com isso teremos a base de dados carregada e ouvindo requisições pedidas.

Para enviar requisições é só inserir o shopback.php na pasta de projetos do apache e rodar no browser da seguinte maneira:

localhost/shopback.php?url=http://www.lojadamaria.com.br/categoria-legais

Onde url é a página que a tag mandará.

Acredito que não tenha feito a automatização por conta da falta de tempo, mas neste caso os proximos passos que iria fazer para o objetivo ficar completo seriam:

1. Contar número de ocorrencias que um problema ocorre
2. Passou de um limiar teriamos duas soluções (enviar um e-mail para alguem verificar ou cortar a string de um modo que recuperaria o padrão das formas que estão na base e tentar casar com os requests que chegam ao servidor).

Bem, acredito que não tenha finalizado o desafio, tive algumas coisas no final de semana mas a ideia era essa.


