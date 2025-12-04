public class Main {
    public static void main(String[] args) {
        Autor autor = new Autor("Ray Bradbury", 40, true);
        Usuario usuario = new Usuario("João", 25);
        Livro livro = new Livro("Fahrenheit 451", "Romance", autor);
        Emprestimo emprestimo = new Emprestimo(livro, usuario);
        Artigo artigo = new Artigo("Entendendo Compiladores", autor, "tecnologia", true);

        System.out.println("==== EMPRÉSTIMO ====");
        System.out.println("O livro não está disponível");
        System.out.println("Livro: " + emprestimo.getLivro().getTitulo());
        System.out.println("Autor: " + emprestimo.getLivro().getAutor().getNome());
        System.out.println("Gênero: " + emprestimo.getLivro().getGenero());
        System.out.println("Usuário: " + emprestimo.getUsuario().getNome());
        System.out.println("Idade: " + emprestimo.getUsuario().getIdade());

        System.out.println("\n==== PUBLICAÇÃO ====");
        autor.setEstrategia(new EstrategiaLivro());
        autor.publicar();

        autor.setEstrategia(new EstrategiaArtigo());
        autor.publicar();

        System.out.println("\n==== ARTIGO ====");
        System.out.println("Artigo: " + artigo.getTitulo());
        System.out.println("Autor do artigo: " + artigo.getAutor().getNome());
        System.out.println("Gênero do artigo: " + artigo.getGenero());
        System.out.println("Publicado: " + artigo.isPublicado());
    }
}

// ===== Classes auxiliares no mesmo arquivo =====

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

class Usuario {
    private String nome;
    private int idade;

    public Usuario(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome() { return nome; }
    public int getIdade() { return idade; }
}

class Autor extends Usuario {
    private PublicavelInterface estrategiaPublicacao;

    public Autor(String nome, int idade, boolean tradicional) {
        super(nome, idade);
    }

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

class Livro {
    private String titulo;
    private String genero;
    private Autor autor;

    public Livro(String titulo, String genero, Autor autor) {
        this.titulo = titulo;
        this.genero = genero;
        this.autor = autor;
    }

    public String getTitulo() { return titulo; }
    public String getGenero() { return genero; }
    public Autor getAutor() { return autor; }
}

class Emprestimo {
    private Livro livro;
    private Usuario usuario;

    public Emprestimo(Livro livro, Usuario usuario) {
        this.livro = livro;
        this.usuario = usuario;
    }

    public Livro getLivro() { return livro; }
    public Usuario getUsuario() { return usuario; }
}

class Artigo {
    private String titulo;
    private Autor autor;
    private String genero;
    private boolean publicado;

    public Artigo(String titulo, Autor autor, String genero, boolean publicado) {
        this.titulo = titulo;
        this.autor = autor;
        this.genero = genero;
        this.publicado = publicado;
    }

    public String getTitulo() { return titulo; }
    public Autor getAutor() { return autor; }
    public String getGenero() { return genero; }
    public boolean isPublicado() { return publicado; }
}
