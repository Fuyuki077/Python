programa {
  funcao inicio() {
    real custoFabrica, comissao, impostos, valorTotal

    escreva("digite o valor de fabrica do carro: ")
    leia(custoFabrica)

    impostos = custoFabrica * 0.45
    comissao = impostos * 0.28
    valorTotal = custoFabrica + comissao + impostos

    escreva("O valor total do carro será: ", valorTotal)
  }
}
