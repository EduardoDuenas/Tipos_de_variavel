from math import sqrt, pow


class Incerteza:
    # inicialização
    def __init__(self, val=0.0, err=0.0):   # contem dois valores: valor e erro
        self.val = abs(float(val))
        self.err = abs(float(err))

    # definindo operador +
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Incerteza(self.val + other.val, sqrt(pow(self.err,2) + pow(other.err,2)))
        elif isinstance(other, int) or isinstance(other, float):
            return Incerteza(self.val + other, self.err)

    # definindo operador -
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Incerteza(self.val - other.val, sqrt(pow(self.err,2) + pow(other.err,2)))
        elif isinstance(other, int) or isinstance(other, float):
            return Incerteza(self.val - other, self.err)

    # definindo operador /
    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return Incerteza(self.val / other.val, sqrt(pow((self.err / self.val),2) + pow((other.err / other.val),2)))
        elif isinstance(other, int) or isinstance(other, float):
            return Incerteza(self.val / other, self.err / abs(other))

    # definindo operador *
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Incerteza(self.val * other.val, sqrt(pow((self.err / self.val), 2) + pow((other.err / other.val), 2)))
        elif isinstance(other, int) or isinstance(other, float):
            return Incerteza(self.val * other, self.err * abs(other))

    # definindo operador =
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if other.val == self.val and other.err == self.err:
                return True
            else:
                return False
        else:
            return False

    # definindo operador <
    def __lt__(self, other):        # só é menor se for menor somado com ambos os erros
        if isinstance(other, self.__class__):
            return (other.val - self.val - other.err - self.err) > 0
        elif isinstance(other, int) or isinstance(other, float):
            return (other - self.val - self.err) > 0

    # definindo operador <=
    def __le__(self, other):        # só é menor ou igual se for menor ou igual somado com ambos os erros
        if isinstance(other, self.__class__):
            return (other.val - self.val - other.err - self.err) >= 0
        elif isinstance(other, int) or isinstance(other, float):
            return (other - self.val - self.err) >= 0

    # definindo operador >
    def __gt__(self, other):        # só é maior se for maior subtraindo ambos os erros
        if isinstance(other, self.__class__):
            return (other.val - self.val + other.err + self.err) < 0
        elif isinstance(other, int) or isinstance(other, float):
            return (other - self.val + self.err) < 0

    # definindo operador >=
    def __ge__(self, other):  # só é maior ou igual se for maior ou igual subtraindo ambos os erros
        if isinstance(other, self.__class__):
            return (other.val - self.val + other.err + self.err) <= 0
        elif isinstance(other, int) or isinstance(other, float):
            return (other - self.val + self.err) <= 0

    # definindo operador !=
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            if self.val != other.val or self.err != other.err:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'{self.val} ± {self.err}'

    def isequal(self, other, val_err, err_err):
        '''
        Essa função recebe três parametro e retorna se de acordo com os valores passados os números são proximos o
        suficiente, tal que a diferença das grandezas seja menor que var_err e a diferença entre os erros seja menor
        que err_err:
        :param other: um número com ou sem incerteza
        :param val_err: margem de erro entre os valores
        :param err_err: margem de erro entre os erros
        :return: True se próximos o suficiente ou False se não
        '''
        if isinstance(other, self.__class__):
            if abs(self.val - other.val) <= abs(val_err) and abs(self.err - other.err) <= abs(err_err):
                return True
            else:
                return False
        elif isinstance(other, int) or isinstance(other, float):
            if abs(self.val - other) <= abs(val_err) and abs(self.err) <= abs(err_err):
                return True
            else:
                return False
        else:
            return False

    def isclose(self, other, val_err):
        '''
        Essa função recebe dois parametro e retorna se de acordo com os valores passados os números são proximos o
        suficiente, tal que a soma do maior valor com os erros seja maior que o menor valor mais o var_err:
        :param other: um número com ou sem incerteza
        :param val_err: máximo entre tolerada entre os valores
        :return: True se proximo o suficiente ou False se não
        '''
        if isinstance(other, self.__class__):
            if (self.val + self.err + other.err <= other.val + val_err) or \
                    (self.val - self.err - other.err >= other.val - val_err):
                return True
            else:
                return False

        elif isinstance(other, int) or isinstance(other, float):
            if (self.val + self.err <= other + val_err) or (self.val - self.err >= other - val_err):
                return True
            else:
                return False



