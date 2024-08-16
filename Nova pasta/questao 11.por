programa {
  funcao inicio() {
    real acrescimo, custo, quantidade

    escreva("digite o custo total do produto: ")
    leia(custo)

    escreva("digite a quantidade a ser vendida: ")
    leia(quantidade)

    custo = quantidade * custo

    escreva("o valor total bruto será: ", custo," \ninforme quanto voce gostaria de lucro em porcetagem em cima do preco bruto: ")
    leia(acrescimo)

    acrescimo = custo * (acrescimo/100)

    escreva("O valor total do seu produto com lucro será: ", (custo + acrescimo))
  }
}
