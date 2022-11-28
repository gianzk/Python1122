### diccionario Escuela

Escuela={
    'Alumnos':[
        {
            "DNI":78787878,
            "NOMBRE":"GIANMARCO",
            "GRADO":"1ERO"
        },
        {
            "DNI":78787878,
            "NOMBRE":"GIANMARCO",
            "GRADO":"1ERO"
        },
    ],
    'Profesores':[
        {
            "DNI":46464646,
            "NOMBRE":"Profesor1",
            "Cursos":["curso1","curso2"]
        },
        {
            "DNI":46464646,
            "NOMBRE":"Profesor1",
            "Cursos":["curso1","curso2"]
        }
    ]
}

print(type(Escuela.get("Alumnos")))
print(Escuela.get("Alumnos")[0]["DNI"])