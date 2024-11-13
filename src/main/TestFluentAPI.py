import unittest
import coverage

cov = coverage.Coverage()
cov.start()

from FluentApiSQL import FluentApiSQL  

class TestFluentApiSQL(unittest.TestCase):

    def test_select_all(self):
        query = FluentApiSQL().traeme().de_la_tabla("usuarios").build()
        self.assertEqual(query, "SELECT * FROM usuarios;")

    def test_select_specific_columns(self):
        query = FluentApiSQL().traeme(["id", "nombre"]).de_la_tabla("usuarios").build()
        self.assertEqual(query, "SELECT id, nombre FROM usuarios;")

    def test_where_clause(self):
        query = (
            FluentApiSQL()
            .traeme(["id", "nombre"])
            .de_la_tabla("usuarios")
            .donde("edad > 18")
            .build()
        )
        self.assertEqual(query, "SELECT id, nombre FROM usuarios WHERE edad > 18;")

    def test_order_by(self):
        query = (
            FluentApiSQL()
            .traeme(["id", "nombre"])
            .de_la_tabla("usuarios")
            .ordena_por("nombre", "DESC")
            .build()
        )
        self.assertEqual(query, "SELECT id, nombre FROM usuarios ORDER BY nombre DESC;")

    def test_group_by(self):
        query = (
            FluentApiSQL()
            .traeme(["id", "nombre"])
            .de_la_tabla("usuarios")
            .agrupando_por("ciudad")
            .build()
        )
        self.assertEqual(query, "SELECT id, nombre FROM usuarios GROUP BY ciudad;")

    def test_join_clause(self):
        query = (
            FluentApiSQL()
            .traeme(["id", "nombre"])
            .de_la_tabla("usuarios")
            .mezclar_con("pedidos", "usuarios.id = pedidos.usuario_id")
            .build()
        )
        self.assertEqual(query, "SELECT id, nombre FROM usuarios JOIN pedidos ON usuarios.id = pedidos.usuario_id;")

    def test_count_function(self):
        query = (
            FluentApiSQL()
            .traeme()
            .contar()
            .de_la_tabla("usuarios")
            .build()
        )
        self.assertEqual(query, "SELECT * COUNT(*) FROM usuarios;")

    def test_complex_query(self):
        query = (
            FluentApiSQL()
            .traeme(["id", "nombre"])
            .de_la_tabla("usuarios")
            .donde("edad > 18")
            .agrupando_por("ciudad")
            .ordena_por("nombre", "DESC")
            .build()
        )
        self.assertEqual(query, "SELECT id, nombre FROM usuarios WHERE edad > 18 GROUP BY ciudad ORDER BY nombre DESC;")
    
    def test_empty_columns(self):
        query = FluentApiSQL().traeme([]).de_la_tabla("usuarios").build()
        self.assertEqual(query, "SELECT * FROM usuarios;")  # O el comportamiento esperado

    def test_invalid_where_clause(self):
        with self.assertRaises(ValueError):
            FluentApiSQL().traeme().de_la_tabla("usuarios").donde("") 

    def test_unsupported_order(self):
        with self.assertRaises(ValueError):
            FluentApiSQL().traeme().de_la_tabla("usuarios").ordena_por("nombre", "INVALID")  

    def test_no_table(self):
        with self.assertRaises(ValueError):
            FluentApiSQL().traeme().de_la_tabla("").build() 

# Detener la cobertura y generar el informe
cov.stop()
cov.save()
cov.report()  # Muestra el informe en la terminal
cov.html_report(directory='coverage_html_report')  # Genera un informe HTML en la carpeta especificada

if __name__ == '__main__':
    unittest.main()
