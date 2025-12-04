interface PublicavelInterface {
    void publicar();
}

class EstrategiaLivro implements PublicavelInterface {
    @Override
    public void publicar() {
        System.out.println("Livro publicado");
    }
}

class EstrategiaArtigo implements PublicavelInterface {
    @Override
    public void publicar() {
        System.out.println("Artigo publicado");
    }
}

class Autor {
    private PublicavelInterface estrategia;

    public Autor(String string, int i, boolean b) {
    }

    public void setEstrategia(PublicavelInterface e) {
        this.estrategia = e;
    }

    public void publicar() {
        if (estrategia != null) {
            estrategia.publicar();
        }
    }

    public String getNome() {
        throw new UnsupportedOperationException("Unimplemented method 'getNome'");
    }
}

public class Publicavel {
    public static void main(String[] args) {
        Autor a = new Autor(null, 0, false);
        a.setEstrategia(new EstrategiaLivro());
        a.publicar();
        a.setEstrategia(new EstrategiaArtigo());
        a.publicar();
    }
}
