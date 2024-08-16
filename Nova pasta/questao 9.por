programa {
  funcao inicio() {
    real valorPoupanca, rendimento, valorTotal

    escreva("Digite o valor a ser depositado para o mes: ")
    leia(valorPoupanca)

    rendimento = valorPoupanca * 0.007
    valorTotal = valorPoupanca + rendimento

    escreva("Valor depositado: ", valorPoupanca,
    "\nRendimento total: ", rendimento,
    "\nValor total: ", valorTotal)
  }
}
