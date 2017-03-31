def saludo(idioma):
    def saludo_es():
        print("Hola")
    def saludo_en():
        print("Hi")
    idioma_func={"es":saludo_es,
                "en":saludo_en
                }
    return idioma_func[idioma]

saludar=saludo("es")
saludar()