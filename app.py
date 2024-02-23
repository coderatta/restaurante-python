from models.Restaurante import Restaurante


def main():
    restaurante1 = Restaurante("nome1", "cate1")
    restaurante2 = Restaurante("nome2", "cate2")
    restaurante1.alternar_estado()
    Restaurante.listar_restaurantes()
    restaurante2.avaliar("gabriel", 9.2)
    restaurante2.avaliar("gabriel2", 0.0)
    restaurante2.avaliar("gabriel3", 6.5)
    restaurante2.avaliar("gabriel4", 5.0)
    restaurante2.mostrar_media
    restaurante2.ver_avaliacoes()


if __name__ == "__main__":
    main()
