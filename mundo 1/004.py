a1 = input("DIGITE: ") #a1.is...() somente no tipo string
print("TIPO PRIMITVO:",type(a1))
print("TIPO NUMERO:",a1.isnumeric())
print("TIPO DECIMAL:",a1.isdecimal())
print("TIPO MINUSCULA",a1.islower())
print("TIPO ESPACO",a1.isspace())
print("PODE SER UM NOME DE VAR:",a1.isidentifier())

# .isnumeric() → Retorna True se a string contiver apenas números (inclusive números em Unicode)
# Exemplo:
# "123".isnumeric() → True
# .isdigit() → Retorna True se a string contiver apenas dígitos (0–9), sem espaços ou letras
# Exemplo:
# "42".isdigit() → True

# .isdecimal() → Retorna True apenas para números decimais puros (sem frações ou potências)
# Exemplo:
# "456".isdecimal() → True

# .isalpha() → Retorna True se a string contiver apenas letras (sem números ou espaços)
# Exemplo:
# "Python".isalpha() → True

# .isalnum() → Retorna True se a string contiver apenas letras e/ou números (sem símbolos ou espaços)
# Exemplo:
# "abc123".isalnum() → True

# .islower() → Retorna True se todas as letras forem minúsculas
# Exemplo:
# "python".islower() → True

# .isupper() → Retorna True se todas as letras forem maiúsculas
# Exemplo:
# "PYTHON".isupper() → True

# .istitle() → Retorna True se cada palavra começar com letra maiúscula (estilo título)
# Exemplo:
# "Meu Nome É Humberto".istitle() → True

# .isspace() → Retorna True se a string contiver apenas espaços em branco (inclui \n e \t)
# Exemplo:
# "   ".isspace() → True

# .isprintable() → Retorna True se todos os caracteres forem imprimíveis (sem \n, \t, etc.)
# Exemplo:
# "abc123".isprintable() → True

# .isascii() → Retorna True se todos os caracteres forem do conjunto ASCII (0–127)
# Exemplo:
# "abc".isascii() → True

# .isidentifier() → Retorna True se a string for um nome de variável válido em Python
# Exemplo:
# "nome_valido1".isidentifier() → True
