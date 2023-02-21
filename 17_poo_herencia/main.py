import clases

persona = clases.Personas
persona.setNombre("nombr")
persona.setApellidos("apet")
persona.setAltura("229cm")
persona.setEdad("100 años")

print(f"persona: {persona.getNombre()}  {persona.getApellidos()}")
print(persona.hablar())
print("--------------------------")

informatico = clases.Informatico()
informatico.setNombre("inform")
informatico.setApellidos("inf apt")
print(f"informatico: {informatico.getNombre} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print("--------------------------")