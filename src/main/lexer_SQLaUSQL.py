import re
import sqlparse

#Diccionario de traducción SQL a USQL
sql_a_usql = {
    "SELECT": "TRAEME",
    "*": "TODO",
    "FROM": "DE LA TABLA",
    "WHERE": "DONDE",
    "GROUP BY": "AGRUPANDO POR",
    "JOIN": "MEZCLANDO",
    "ON": "EN",
    "DISTINCT": "LOS DISTINTOS",
    "COUNT": "CONTANDO",
    "INSERT INTO": "METE EN",
    "VALUES": "LOS VALORES",
    "UPDATE": "ACTUALIZA",
    "SET": "SETEA",
    "DELETE FROM": "BORRA DE LA TABLA",
    "ORDER BY": "ORDENA POR",
    "LIMIT": "COMO MUCHO",
    "HAVING": "WHERE DEL GROUP BY",
    "EXISTS": "EXISTE",
    "IN": "EN ESTO",
    "BETWEEN": "ENTRE",
    "LIKE": "PARECIDO A",
    "IS NULL": "ES NULO",
    "ALTER TABLE": "CAMBIA LA TABLA",
    "ADD COLUMN": "AGREGA LA COLUMNA",
    "DROP COLUMN": "ELIMINA LA COLUMNA",
    "CREATE TABLE": "CREA LA TABLA",
    "DROP TABLE": "TIRA LA TABLA",
    "DEFAULT": "POR DEFECTO",
    "UNIQUE": "UNICO",
    "PRIMARY KEY": "CLAVE PRIMA",
    "FOREIGN KEY": "CLAVE REFERENTE",
    "NOT NULL": "NO NULO",
    "CAST": "TRANSFORMA A",
}


def traducir_sql_a_usql(consulta_sql):
    # Procesar frases compuestas primero para evitar conflictos
    for sql_frase, usql_frase in sql_a_usql.items():
        consulta_sql = re.sub(rf'\b{re.escape(sql_frase)}\b', usql_frase, consulta_sql, flags=re.IGNORECASE)

    # Parsear la consulta SQL y procesar tokens
    parseada = sqlparse.parse(consulta_sql)[0]
    tokens_traducidos = []

    for token in parseada.tokens:
        token_str = token.value.upper().strip()
        
        # Intentar traducir usando el diccionario o mantener el token original si no hay traducción
        token_traducido = sql_a_usql.get(token_str, token_str)
        
        # Manejar funciones con paréntesis como COUNT()
        if re.match(r"^[A-Z_]+\(.+\)$", token_str):
            palabra_clave, resto = token_str.split('(', 1)
            token_traducido = f"{sql_a_usql.get(palabra_clave, palabra_clave)}({resto}"
        
        tokens_traducidos.append(token_traducido)

    # Unir los tokens y ajustar el formato final
    consulta_final = " ".join(tokens_traducidos)
    consulta_final = re.sub(r'\(\s*', '(', consulta_final)
    consulta_final = re.sub(r'\s*\)', ')', consulta_final)
    consulta_final = re.sub(r'\s*,\s*', ', ', consulta_final)

    return consulta_final


if __name__ == '__main__':
    consulta_usql = "SELECT * FROM usuarios WHERE edad > 18;"
    resultado = traducir_sql_a_usql(consulta_usql)
    print(resultado)  
