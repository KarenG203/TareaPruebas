import pytest
from operaciones import suma, resta, multiplicacion, division

def test_suma1():
    assert suma(-7,3) ==-4
    print("la funcion suma1 funciona correctamente")
    
def test_suma2():
    assert suma(3,1) ==4
    print("la funcion suma2 funciona correctamente")
    
def test_resta1():
    assert resta(7,3) ==4
    print("la funcion resta1 funciona correctamente")
    
def test_resta2():
    assert resta(-3,1) ==-4
    print("la funcion resta2 funciona correctamente")
    
def test_multiplicacion1():
    assert multiplicacion(7,-3) ==-21
    print("la funcion multiplicacion1 funciona correctamente")
    
def test_multiplicacion2():
    assert multiplicacion(3,1) ==3
    print("la funcion multiplicacion2 funciona correctamente")
    
def test_division1():
    assert division(7,-3) ==-2.3333333333333335
    print("la funcion division1 funciona correctamente")
    
def test_division2():
    assert division(3,1) ==3
    print("la funcion division2 funciona correctamente")
    
    
@pytest.mark.parametrize(
    "input_x, input_y, esperado",
    [
        (5, 8, 13),
        (8, suma(-5,3), 6),
        (suma(-8,1), 6, -1),
    ]
)

def test_suma_params(input_x, input_y, esperado):
    assert suma(input_x, input_y) == esperado
    print ("las funciones parametrizadas funcionan correctamente")
    
    
    
@pytest.mark.parametrize(
    "input_x, input_y, esperado",
    [
        (5, 8, -3),
        (-8, resta(5,3), -10),
        (resta(8,1), -6, 13),
    ]
)

def test_resta_params(input_x, input_y, esperado):
    assert resta(input_x, input_y) == esperado
    print ("las funciones parametrizadas funcionan correctamente")
    
    
    
@pytest.mark.parametrize(
    "input_x, input_y, esperado",
    [
        (-5, 8, -40),
        (8, multiplicacion(-1,3), -24),
        (multiplicacion(-8,1), -6, 48),
    ]
)

def test_multiplicacion_params(input_x, input_y, esperado):
    assert multiplicacion(input_x, input_y) == esperado
    print ("las funciones parametrizadas funcionan correctamente")
    
    
    
@pytest.mark.parametrize(
    "input_x, input_y, esperado",
    [
        (8, 5, 1.6),
        (8, division(5,-3), -4.8),
        (division(8,1), 6, 1.3333333333333333),
    ]
)

def test_division_params(input_x, input_y, esperado):
    assert division(input_x, input_y) == esperado
    print ("las funciones parametrizadas funcionan correctamente")
    
if __name__ == '__operaciones__':
    test_suma1()
    test_suma2()
    test_resta1()
    test_resta2()
    test_multiplicacion1()
    test_multiplicacion2()
    test_division1()
    test_division2()