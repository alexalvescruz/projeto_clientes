def cpf_valido(cpf):
    return len(cpf) == 11


def nome_valido(nome):
    def is_alpha_space(str):
        return all(char.isalpha() or char.isspace() for char in str)

    return is_alpha_space(nome)


def rg_valido(rg):
    return len(rg) == 9


def celular_valido(celular):
    return len(celular) < 11
