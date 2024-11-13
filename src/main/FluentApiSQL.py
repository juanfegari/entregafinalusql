
class FluentApiSQL:
    def __init__(self):
        self.parts = []

    def traeme(self, columns=None):
        """Agrega la cláusula TRAEME"""
        if columns is None or len(columns) == 0 or (isinstance(columns, list) and all(col is None for col in columns)):
            self.parts.append("SELECT *")
        else:
            self.parts.append(f"SELECT {', '.join(columns)}")
        return self

    def de_la_tabla(self, table):
        """Agrega la cláusula FROM"""
        if not table:
            raise ValueError("El nombre de la tabla no puede estar vacío.")
        self.parts.append(f"FROM {table}")
        return self

    def donde(self, condition):
        """Agrega la cláusula WHERE"""
        if not condition:
            raise ValueError("La cláusula WHERE no puede estar vacía.")
        self.parts.append(f"WHERE {condition}")
        return self

    def ordena_por(self, column, order):
        """Agrega la cláusula ORDER BY"""
        if order not in ["ASC", "DESC"]:
            raise ValueError("El orden debe ser 'ASC' o 'DESC'.")
        self.parts.append(f"ORDER BY {column} {order}")
        return self

    def agrupando_por(self, column):
        """Agrega la cláusula GROUP BY"""
        if not column:
            raise ValueError("La cláusula GROUP BY no puede estar vacía.")
        self.parts.append(f"GROUP BY {column}")
        return self

    def mezclar_con(self, table, condition):
        """Agrega la cláusula JOIN"""
        if not table or not condition:
            raise ValueError("El nombre de la tabla o la condición de JOIN no pueden estar vacíos.")
        self.parts.append(f"JOIN {table} ON {condition}")
        return self

    def contar(self):
        """Agrega la función COUNT"""
        self.parts.append("COUNT(*)")
        return self

    def build(self):
        """Construye y devuelve la consulta SQL"""
        return ' '.join(self.parts) + ';'
    

query = (
FluentApiSQL()
.traeme(["id", "nombre"])
.de_la_tabla("usuarios")
.donde("edad > 18")
.ordena_por("nombre", "DESC")
.build()
)
print(query)  # Salida: SELECT id, nombre FROM usuarios WHERE edad > 18 ORDER BY nombre DESC;