def question ():
     rules=input("Tienes que responder cada pregunta con un  SI o con un NO, entiendes : ")
     if rules != "si":
          return print("Intenta de nuevo")
     else:print("Siguiente pregunta")
     Quest1=input("Tienes hambre: ")
     if Quest1 !="si":
        return print("Entonces vamos a caminar ")
     else:
        print("Siguiente pregunta")

     Quest2=input("Quieres comer en algun restaurante: ")
     if Quest2 !="si":
        return print("Vamos a comer en algun lugar")
     else:
        print("Siguiente pregunta")

     Quest3=input("Quieres comer pizza: ")
     if Quest3 !="si":
        return print("Vamos a comer una hamgurguesa entonces ")
     else:
        print("Lets go eat a pizza")
question ()