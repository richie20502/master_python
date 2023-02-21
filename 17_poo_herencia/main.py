import clases

persona = clases.Personas
persona.setNombre("nombr")
persona.setApellidos("apet")
persona.setAltura("229cm")
persona.setEdad("100 años")

print(f"persona: {persona.getNombre()}  {persona.getApellidos()}")
print(persona.hablar())
