from estudiante import devolver_materias

def estudiante_en_materia(estudiante: str, materia: str) -> bool | None: 
  try:
    materias = devolver_materias(estudiante)
    return materia in materias
  except KeyError:
    print(f'ERROR => {estudiante} no se encuentra registrado')

print(estudiante_en_materia('Daniel', 'Mate'))
print(estudiante_en_materia('Daniela', 'Mate'))