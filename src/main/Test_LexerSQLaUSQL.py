import unittest
from lexer_SQLaUSQL import *
import coverage

cov = coverage.Coverage()
cov.start()

class TestTraductorSQLaUSQL(unittest.TestCase):

    def test_select_simple(self):
        consulta_sql = "SELECT * FROM usuarios WHERE edad > 18;"
        esperado = "TRAEME * DE LA  TABLA USUARIOS  DONDE  EDAD > 18 ;"
        resultado = traducir_sql_a_usql(consulta_sql)
        self.assertEqual(resultado, esperado)

    def test_select_distinct(self):
        consulta_sql = "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid';"
        esperado = "TRAEME LOS  DISTINTOS NOMBRE  DE LA  TABLA CLIENTES  DONDE  CIUDAD = 'MADRID' ;"
        resultado = traducir_sql_a_usql(consulta_sql)
        self.assertEqual(resultado, esperado)

    def test_insert_into(self):
        consulta_sql = "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25);"
        esperado = "METE EN  USUARIOS (NOMBRE, EDAD) LOS  VALORES ('JUAN', 25) ;"
        resultado = traducir_sql_a_usql(consulta_sql)
        self.assertEqual(resultado, esperado)

    def test_update(self):
        consulta_sql = "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero';"
        esperado = "ACTUALIZA EMPLEADOS  SETEA  SALARIO = 3000 DONDE  PUESTO = 'INGENIERO' ;"
        resultado = traducir_sql_a_usql(consulta_sql)
        self.assertEqual(resultado, esperado)

    def test_join(self):
        consulta_sql = "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = 'Barcelona';"
        esperado = "TRAEME * DE LA  TABLA PEDIDOS  MEZCLANDO CLIENTES  EN  PEDIDOS.CLIENTE_ID = CLIENTES.ID DONDE  CLIENTES.CIUDAD = 'BARCELONA' ;"
        resultado = traducir_sql_a_usql(consulta_sql)
        self.assertEqual(resultado, esperado)

    def test_count_group_by(self):
        consulta_sql = "SELECT COUNT() FROM ventas GROUP BY producto HAVING COUNT() > 5;"
        esperado = "TRAEME  CONTANDO() DE  LA TABLA  VENTAS AGRUPANDO  POR PRODUCTO  WHERE DEL AGRUPANDO POR  CONTANDO() > 5 ;"
        resultado = traducir_sql_a_usql(consulta_sql)
        self.assertEqual(resultado, esperado)

    def test_delete(self):
        consulta_sql = "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25;"
        esperado = "DELETE  DE LA  TABLA CLIENTES  DONDE EDAD  ENTRE  18  AND  25 ;"
        resultado = traducir_sql_a_usql(consulta_sql)
        self.assertEqual(resultado, esperado)

    def test_alter_add_column(self):
        consulta_sql = "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL;"
        esperado = "CAMBIA LA  TABLA EMPLEADOS  AGREGA LA  COLUMNA DIRECCION  VARCHAR(255)  NO  NULO ;"
        resultado = traducir_sql_a_usql(consulta_sql)
        self.assertEqual(resultado, esperado)

    def test_alter_drop_column(self):
        consulta_sql = "ALTER TABLE empleados DROP COLUMN direccion;"
        esperado = "CAMBIA LA  TABLA EMPLEADOS  ELIMINA LA  COLUMNA DIRECCION ;"
        resultado = traducir_sql_a_usql(consulta_sql)
        self.assertEqual(resultado, esperado)

cov.stop()
cov.save()
cov.report()  
cov.html_report(directory='coverage_html_report')

if __name__ == '__main__':
    unittest.main()
