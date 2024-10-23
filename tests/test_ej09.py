from src.ej09 import func_comprobacion_contrasena
def test_func_comprobacion_contrasena():
    assert func_comprobacion_contrasena('contraseña') == '¡La contraseña es correcta!'
