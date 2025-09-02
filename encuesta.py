#Nombre: Miguel Silva 
#Diseñar encuesta para 6 usuarios que guarde el nombre, carrera e idea de proyecto del mismo
def encuesta(cant_usuarios):
    i=0
    nombres=[]
    carreras=[]
    ideas=[]
    while i<cant_usuarios:
        nombre=input("Ingrese su nombre: ")
        nombres.append(nombre)
        carrera=input("Ingrese la carrera que esta estudiando: ")
        carreras.append(carrera)
        idea_proyecto=input("Ingrese su idea de proyecto de este semestre: ")
        ideas.append(idea_proyecto)
        i+=1
    for nom, carre, ide in zip(nombres, carreras, ideas):
        print(f"---------------\nNombre: {nom}\nCarrera: {carre} \nIdea: {ide}\n---------------")
    
def main():
    encuesta(2)

if __name__=="__main__":
    main()