# FEITO POR: FELIPE FERREIRA DE FRANÇA  | Grupo 7 Tema 8 | Prova 2

# 8 - Sistema de Gerenciamento de Estacionamento
#Controla a entrada e saída de veículos em vagas de estacionamento. Deve registrar horário de 
#entrada, saída e calcular o valor a ser pago com base no tempo de permanência. Também pode listar placa_saida, hora_saida, dia_saida, vaga_vazia


#Aqui crio a classe pai "Estacionamento", aqui é onde seram registradas a placa do veiculo, horario da entrada, dia da entrada e a vaga na qual esta ocupando
class Estacionamento:
    def __init__(self, placa, hora, dia, vaga):
        self.set_placa(placa)
        self.set_hora(hora)
        self.set_dia(dia)
        self.set_vaga(vaga)

#Aqui pego os atributos privados da classe de cima em uma nova classe para facilitar ao chamar os atributos da classe mais a frente no código
    def get_placa(self):
        return self.placa
    def get_hora(self):
        return self.hora
    def get_dia(self):
        return self.dia
    def get_vaga(self):
        return self.vaga

#Aqui eu crio os erros, quando as informações digitadas pelo usuário não estão de acordo o erro aparece pedindo para que o usuário digite aos conformes da plataforma
    def set_placa(self, placa):
        placa = str(placa)
        if len(placa) == 7:
            self.placa = placa
        else:
            raise ValueError("A placa de um veículo deve conter exatamente 7 dígitos.")
    def set_hora(self, hora):
        if 0 <= hora <= 24:
            self.hora = hora
        else:
            raise ValueError("A hora deve estar entre 0 e 24.")
    def set_dia(self, dia):
        if 1 <= dia <= 31:
            self.dia = dia
        else:
            raise ValueError("O dia deve estar entre 1 e 31.")
    def set_vaga(self, vaga):
        vaga = str(vaga)
        if 1 <= len(vaga) <= 2:
            self.vaga = vaga
        else:
            raise ValueError("O número da vaga deve ter 1 ou 2 dígitos.")

#Esta é uma classe polimorfa genérica na qual servirá para mostrar na tela as informações de maneira mais limpa e organizada referente ao código
    def exibir_info(self):
        pass

#Aqui crio a classe filha "Entrada", aqui é onde serão registradas a placa do veículo, horário da entrada, dia da entrada e a vaga na qual está ocupando
class Entrada(Estacionamento):
    def exibir_info(self):
        print(f"Placa: {self.get_placa()} | Entrou às {self.get_hora()} horas | Do dia: {self.get_dia()} | Vaga ocupada número: {self.get_vaga()}")

#Aqui crio a classe filha "Saida", que registra as informações quando o carro sai do estacionamento
class Saida(Estacionamento):
    def exibir_info(self):
        print(f"Placa: {self.get_placa()} | Saiu às {self.get_hora()} horas | Do dia: {self.get_dia()} | Vaga liberada número: {self.get_vaga()}")

#O "Sistema" armazena os atributos que foram criados nas classes acima em uma lista e depois mostra na tela todos os itens no qual coloquei
class Sistema:
    def __init__(self):
        self.registros = []
    def adicionar_registro(self, registro):
        try:
            self.registros.append(registro)
            print("Entrada/Saída registrada com sucesso!")
        except ValueError as e:
            print(f"Erro ao registrar: {e}")
    def listar_entradas(self):
        print("\nEntradas registradas:")
        for r in self.registros:
            if isinstance(r, Entrada):
                r.exibir_info()
    def listar_saidas(self):
        print("\nSaídas registradas: ")
        for r in self.registros:
            if isinstance(r, Saida):
                r.exibir_info()

#Aqui o programa chama a classe "Sistema" e mostra as placas de veiculos que entraram ou sairam no estacionamento da classe "Estacionamento"

#Entrada do veículo, vai mostrar placa, hora da entrada do veiculo, dia da entrada, vaga que ocupa:
sistema = Sistema()
entrada = Entrada(1234567, 17, 12, 11)
sistema.adicionar_registro(entrada)
sistema.listar_entradas()

#Saída do veículo, vai mostrar placa, hora da saida do veiculo, dia da saida, vaga que foi liberada:
saida = Saida(1234567, 12, 14, 11)
sistema.adicionar_registro(saida)
sistema.listar_saidas()