class Vehiculo(): 
  def __init__(self,color,ruedas): 
    self.color=color
    self.ruedas=ruedas
  def __str__(self): 
    return f"Color {self.color} , Ruedas {self.ruedas}"


class Coche(Vehiculo): 
  def __init__(self, color, ruedas, velocidad, cilindrada):
      Vehiculo.__init__(self, color, ruedas)
      self.velocidad = velocidad
      self.cilindrada = cilindrada
  def __str__(self):
      return Vehiculo.__str__(self) + f", {self.velocidad} km/h, {self.cilindrada} cc"

class Bicicleta(Vehiculo): 
  def __init__(self,color,ruedas,tipo): 
    Vehiculo.__init__(self,color,ruedas) 
    self.tipo=tipo 
  def __str__(self): 
    return Vehiculo.__str__(self) + f" , Tipo : {self.tipo}" 

class Camioneta(Coche): 
  def __init__(self,color,ruedas,velocidad,cilindrada,carga): 
    Coche.__init__(self,color,ruedas,velocidad,cilindrada)
    self.carga=carga 
  def __str__(self): 
    return Coche.__str__(self)+ f" , carga : {self.carga} Kgms" 

class Motocicleta(Bicicleta): 
  def __init__(self,color,ruedas,tipo,velocidad,cilindrada): 
    Bicicleta.__init__(self,color,ruedas,tipo)
    self.velocidad=velocidad
    self.cilindrada=cilindrada
  def __str__(self): 
    return Bicicleta.__str__(self) + f", Velocidad : {self.velocidad} , Cilindrada : {self.cilindrada}"


combi=Coche("Verde",4,90,1800)
fiorino=Camioneta("Blanca",4,150,1200,500) 
trek=Bicicleta("Platinada",2,"Deportiva")
jumbo=Motocicleta("Roja",2,"Urbana",120,125) 



lista=[combi,fiorino,trek,jumbo]

def catalogar(vehiculos,ruedas=None): 
  contador=0
  if ruedas is None:  
        for i in vehiculos: 
            print(type(i).__name__,i)
    
  elif ruedas is not None: 
      for i in vehiculos:
        if i.ruedas==ruedas: 
          contador+=1
        
  
  if contador!=0: 
        print(f"Se han encontrado {contador} Vehiculos con {ruedas} ruedas") 
  elif contador==0 and ruedas is not None:
        print("No se han encontrado vehiculos con dicho criterio")
    
     

catalogar(lista,3)













