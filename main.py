class Persona:
  def __init__(self, datos_ciudadano: list[tuple[str, str, str, int]]) -> None:
    if datos_ciudadano[3] < 0:
      raise ValueError("La edad no puede ser menor a 0")
    
    object.__setattr__(self, "dni", datos_ciudadano[0])
    object.__setattr__(self, "nombre", datos_ciudadano[1])
    object.__setattr__(self, "apellido", datos_ciudadano[2])
    object.__setattr__(self, "edad", datos_ciudadano[3])
    
  def __setattr__(self, name, value):
    raise AttributeError("Persona es inmutable")
  
  def __repr__(self):
    return f"Persona({self.nombre}) {self.apellido}, {self.edad})"

  def validar_dni(self, persona_list: list[Persona]) -> bool:
    for persona in persona_list:
      if persona.dni == self.dni:
        return False
    
    return True