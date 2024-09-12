data: dict[str, list[str]] = {
  "Daniel": ["Mate", "Computacion"],
  "Maria": ["Mate", "Fisica"],
}

def devolver_materias(estudiante: str) -> list[str]:
  return data[estudiante]