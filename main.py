import codecs


def imparejable(persona):
    nombre, apellido, localidad, edad, genero, generoDeInteres = persona
    return generoDeInteres == "N" or edad <= 10


def matchea(persona, pretendiente):
    _, _, persona_localidad, persona_edad, persona_genero, persona_generoDeInteres = persona
    _, _, pretendiente_localidad, pretendiente_edad, pretendiente_genero, pretendiente_generoDeInteres = pretendiente

    return pretendiente_localidad == persona_localidad \
           and (persona_generoDeInteres == "A" or pretendiente_genero == persona_generoDeInteres) \
           and (pretendiente_generoDeInteres == "A" or persona_genero == pretendiente_generoDeInteres) \
           and ((persona_edad >= 18 and pretendiente_edad >= 18) or (persona_edad < 18 and pretendiente_edad < 18))

def esIndiferente(persona):
    nombre, apellido, localidad, edad, genero, generoDeInteres = persona
    return generoDeInteres == "A"


def personaComoImprimible(persona):
    nombre, apellido, localidad, edad, genero, generoDeInteres = persona
    return "{}, {}, {}, {}, {}, {}".format(nombre, apellido, localidad, edad, genero, generoDeInteres)


def dividir(personas):
    segregados = []
    parejas = []
    personasEmparejables = []

    for persona in personas:
        if imparejable(persona):
            segregados.append(persona)
        elif not esIndiferente(persona):
            personasEmparejables.insert(0, persona)
        else:
            personasEmparejables.append(persona)

    return segregados, parejas, personasEmparejables


def conquistar(divididos):
    segregados, parejas, personasEmparejables = divididos

    while personasEmparejables:
        persona = personasEmparejables.pop(0)

        matcheado = False
        for (i, candidato) in enumerate(personasEmparejables):
            if matchea(persona, candidato):
                personasEmparejables.pop(i)
                parejas.append((persona, candidato))
                matcheado = True
                break

        if not matcheado:
            segregados.append(persona)

    return segregados, parejas


def abrirYParsear(ruta):
    personas = []

    with codecs.open(ruta, "r", "iso-8859-1") as file:
        for line in file:
            personaRaw = line.strip().split(", ")
            persona = (personaRaw[0], personaRaw[1], personaRaw[2], int(personaRaw[3]), personaRaw[4], personaRaw[5])
            personas.append(persona)

    return personas


def imprimirResultados(segregados, parejas):
    with open("parejas.txt", "w+") as salida:
        for (i, candidato) in parejas:
            linea = i.nombre + ", " + i.apellido + ", " + str(
                i.edad) + " - " + candidato.nombre + ", " + candidato.apellido + ", " + str(
                candidato.edad) + " - " + i.localidad + "\n"
            salida.write(linea)

    with open("disparejos.txt", "w+") as segundasalida:
        for soltero in segregados:
            linea = soltero.nombre + ", " + soltero.apellido + ", " \
                    + str(soltero.edad) + ", " + soltero.localidad + ", " + soltero.generoDeInteres
            divisor = False

            if soltero.edad <= 10:
                linea = linea + ". No fue matcheado por baja edad. "
                divisor = True

            if soltero.generoDeInteres == "N":
                linea = linea + ". No fue matcheado porque no presentaba interes. "
                divisor = True

            if divisor:
                linea = linea + "\n"
            else:
                linea = linea + " No fue matcheado porque no se le encontro pareja por localidad.\n"

            segundasalida.write(linea)


if __name__ == '__main__':
    personas = abrirYParsear("ejemplo1.txt")
    divididos = dividir(personas)
    segregados, parejas = conquistar(divididos)

    print("Segregados: {}".format(len(segregados)))

    print("Matcheados: {}".format(len(parejas)))

    imprimirResultados(segregados, parejas)