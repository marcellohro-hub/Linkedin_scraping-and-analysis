Fiz um web-scraping de 600 vagas da página resultante da pesquisa "engenharia mecânica" no linkedin e depois analisei os dados. O objetivo é gerar insights sobre esse mercado.

Maioria das vagas são de até 3 meses atrás.

Reparei que os posts poderiam ser separados por nichos, esse gráfico mostra o número de posts de cada nicho.

| ![](https://github.com/marcellohro-hub/Linkedin_scraping-and-analysis/blob/master/img/nichos.png) | 
|:--:| 
| *Desempenho dos modelos* |

Fiz uma lista de palavras-chave que mais aparecem nas descrições das vagas utilizando ferramentas de uma biblioteca de NLP (Natural language Processing), e dessa lista escolhi manualmente apenas os nomes que tem a ver com habilidades e técnicas da área. Com isso foi possível fazer o gráfico de habilidade x número de posts que pedem tal habilidade:

| ![](https://github.com/marcellohro-hub/Linkedin_scraping-and-analysis/blob/master/img/habilidades.png) | 
|:--:| 
| *Desempenho dos modelos* |

Salário médio e desvio-padrão de cada nível. Maioria das vagas não colocam salário, portanto não acho recomendado utilizar modelos de ML para prever salários:

| ![](https://github.com/marcellohro-hub/Linkedin_scraping-and-analysis/blob/master/img/download.png) | 
|:--:| 
| *Desempenho dos modelos* |

Maioria das vagas são para São Paulo:

| ![](https://github.com/marcellohro-hub/Linkedin_scraping-and-analysis/blob/master/img/local.png) | 
|:--:| 
| *Desempenho dos modelos* |

E aqui uma tabela de correlação entre o nicho a habilidade e o salário (lembrando que maioria dos posts não colocam salário).

| ![](https://github.com/marcellohro-hub/Linkedin_scraping-and-analysis/blob/master/img/corr.png) | 
|:--:| 
| *Desempenho dos modelos* |
