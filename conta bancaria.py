class ContaBancaria:
    def __init__(self,numero,saldo,nome,tipo,limite,status=False):
        self,numero=numero
        self,saldo=saldo
        self,nome=nome
        self,tipo=tipo
        self,limite=limite
        self,status=status

        def verificarsaldo(self):
            print(f'saldo: R$ {self.saldo}')
        def depositor(self, valor_deposito):
            self.saldo+=valor_deposito
            print(f'deposito um valor de: R$ {valor_deposito}')
            self.verificado()

        def sacar(self, valor_saque):
             if valor_saque > self.limite:
                 print(f'O valor do saque de R$ {valor_saque} é maior que seu limite de R$ {self.limite}')
             elif valor_saque > self.saldo:
                 print(f'Saldo insuficiente')
                 self.saldo -= valor_saque
                 print(f"Sacando um valor de: R$ {valor_saque}")
                 self.verificarsaldo()

        def ativarconta(self):
            if status = False:
                status = True
                print("Conta Ativada")
            else:
                print("Essa conta já está ativada")

    conta1=ContaBancaria(123456789,1000,50,"Kevin","Cor",5000)
    conta1.ativarconta()
    conta1.verificarsaldo()
    conta1.depositar(983)
    conta1.sacar(12)
    conta1.depositar(9000)
    conta1.sacar(6000)

