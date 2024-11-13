import unittest
from lexer_USQLaSQL import *
import coverage

cov = coverage.Coverage()
cov.start()

class Test_TraductorUSQL(unittest.TestCase):
    
    def test_seleccionar_todo(self):
        consulta_usql = "TRAEME TODO DE_LA_TABLA usuarios DONDE edad > 18; "
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertEqual(resultado, "SELECT * FROM usuarios WHERE edad > 18;")

    def test_seleccionar_sin_where(self):
        consulta_usql = "TRAEME TODO DE_LA_TABLA usuarios;"
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertEqual(resultado, "SELECT * FROM usuarios;")

    def test_seleccionar_contando(self):
        consulta_usql = "TRAEME CONTANDO(TODO) DE_LA_TABLA ventas;"
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertEqual(resultado, "SELECT COUNT(*) FROM ventas;")
    
    def test_seleccionar_con_donde(self):
        consulta_usql = "TRAEME NOMBRE DE_LA_TABLA empleados DONDE edad > 30;"
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertEqual(resultado, "SELECT NOMBRE FROM empleados WHERE edad > 30;")
    
    def test_insertar(self):
        consulta_usql = "METE_EN empleados (nombre, edad) LOS_VALORES ('Juan', 25);"
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertEqual(resultado.strip(), "INSERT INTO empleados (nombre , edad) VALUES ('Juan', 25);")
    
    def test_actualizar(self):
        consulta_usql = "ACTUALIZA empleados SETEA nombre = 'Pedro' DONDE id = 1;"
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertEqual(resultado, "UPDATE empleados SET nombre = 'Pedro' WHERE id = 1;")
    
    def test_borrar(self):
        consulta_usql = "BORRA_DE_LA_TABLA empleados DONDE id = 1;"
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertEqual(resultado, "DELETE FROM empleados WHERE id = 1;")

    def test_alter_agregar_columna(self):
        consulta_usql = "CAMBIA_LA_TABLA empleados AGREGA_LA_COLUMNA nuevo_columna VARCHAR(50) NO_NULO;"
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertEqual(resultado, "ALTER TABLE empleados ADD COLUMN nuevo_columna VARCHAR(50) NOT NULL;")
    
    def test_alter_eliminar_columna(self):
        consulta_usql = "CAMBIA_LA_TABLA empleados ELIMINA_LA_COLUMNA viejo_columna;"
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertEqual(resultado, "ALTER TABLE empleados DROP COLUMN viejo_columna;")
    
    def test_seleccionar_con_join(self):
        consulta_usql = "TRAEME TODO DE_LA_TABLA empleados MEZCLANDO departamentos EN empleados.depto_id = departamentos.id;"
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertEqual(resultado, "SELECT * FROM empleados JOIN departamentos ON empleados.depto_id = departamentos.id;")

    def test_consulta_sql_valida(self):
        consulta_sql = "SELECT * FROM usuarios WHERE edad > 18;"
        resultado = es_consulta_sql_valida(consulta_sql)
        self.assertTrue(resultado)

    '''
    def test_consulta_sql_no_valida(self):
        consulta_sql = "SELECT FROM usuarios WHERE > 18;"
        resultado = es_consulta_sql_valida(consulta_sql)
        self.assertFalse(resultado)
    '''

    def test_insertar_valores_incorrectos(self):
        consulta_usql = "METE_EN empleados (nombre, edad) LOS_VALORES (Juan, 25);"
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertIsNone(resultado)  # Espera que falle

    def test_update_sin_where(self):
        consulta_usql = "ACTUALIZA empleados SETEA nombre = 'Pedro';"
        resultado = traducir_usql_a_sql(consulta_usql)
        self.assertIsNone(resultado)  # Espera que falle


cov.stop()
cov.save()
cov.report()  
cov.html_report(directory='coverage_html_report')  

if __name__ == '__main__':
    unittest.main()
