public class Autor extends Usuario {
    private boolean tradicional;
    private PublicavelInterface estrategiaPublicacao;

    public Autor(String nome, int idade, boolean tradicional) {
        super(nome, idade);
        this.tradicional = tradicional;
    }

    public boolean isTradicional() { return tradicional; }
    public void setTradicional(boolean tradicional) { this.tradicional = tradicional; }

    public void setEstrategiaPublicacao(PublicavelInterface estrategia) {
        this.estrategiaPublicacao = estrategia;
    }

    public void setEstrategia(PublicavelInterface estrategia) {
        setEstrategiaPublicacao(estrategia);
    }

    public void publicar() {
        if (estrategiaPublicacao != null) {
            estrategiaPublicacao.publicar();
        } else {
            System.out.println("Nenhuma estratégia definida");
        }
    }
}
