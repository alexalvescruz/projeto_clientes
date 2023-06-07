import re
from validate_docbr import CPF


def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)


def nome_valido(nome):
    def is_alpha_space(str):
        return all(char.isalpha() or char.isspace() for char in str)

    return is_alpha_space(nome)


def rg_valido(rg):
    return len(rg) == 9


def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)

    return resposta
