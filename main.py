class Persona:
  def __init__(self, datos_ciudadano: list[tuple[str, str, str, int]]) -> None:
    dni = datos_ciudadano[0]
    nombre = datos_ciudadano[1]
    apellido = datos_ciudadano[2]
    edad = datos_ciudadano[3]
    
    if edad < 0:
      raise ValueError("La edad no puede ser menor a 0")
    
    object.__setattr__(self, "dni", dni)
    object.__setattr__(self, "nombre", nombre)
    object.__setattr__(self, "apellido", apellido)
    object.__setattr__(self, "edad", edad)
    
  def __setattr__(self, name, value):
    raise AttributeError("Persona es inmutable")
  
  def __repr__(self):
    return f"{self.nombre} {self.apellido}, {self.edad}"

  def validar_dni(self, persona_list: list[Persona]) -> bool:
    for persona in persona_list:
      if persona.dni == self.dni:
        return False
    
    return True
  
class RegistroPersonas:
  def __init__(self, datos: list[tuple[str, str, str, int]]):
    self.lista_personas: list[Persona] = []
    for dato in datos:
      persona = Persona(dato)
      if persona.validar_dni(self.lista_personas):
        self.lista_personas.append(persona)
    
    self.registros_formateados: list[dict[str, str, str, int]] = []
    
  def formateo_registros(self):
    for persona in self.lista_personas:
      self.registros_formateados.append({persona.dni : {persona.nombre, persona.apellido, persona.edad}})
    return self.registros_formateados
      
  def get_mayor(self):
    return max(self.lista_personas, key=lambda persona : persona.edad)
  
  def get_menor(self):
    return min(self.lista_personas, key=lambda persona : persona.edad)
  
  def segmentacion_poblacion(self, threshold=25):
    mayores = []
    menores = []
    
    for persona in self.lista_personas:
      if persona.edad >= threshold:
        mayores.append(persona)
      else:
        menores.append(persona)
    return mayores, menores, len(mayores), len(menores)
  
  def promedio_edad(self):
    sum_edades = 0
    cant_personas = 0
    for persona in self.lista_personas:
      sum_edades += persona.edad
      cant_personas += 1
    return sum_edades/cant_personas
  
  def __getitem__(self, dni):
    for persona in self.lista_personas:
      if persona.dni == dni:
        return persona.edad






datos = [
    ('38506456', 'Giovani', 'Lo Celso', 30),
    ('33908456', 'Lionel', 'Messi', 39),
    ('34467890', 'Angel', 'Di Maria', 38),
    ('44393204', 'Nicolas', 'Paz', 20),
    ('42910290', 'Franco', 'Ibarra', 23),
    ('43423127', 'Jaminton', 'Campaz', 24),
]

datos_personas = RegistroPersonas(datos)
print(datos_personas.formateo_registros())
print(datos_personas.get_mayor())
print(datos_personas.get_menor())
print(datos_personas.segmentacion_poblacion())
print(datos_personas.promedio_edad())
print(datos_personas["34467890"])