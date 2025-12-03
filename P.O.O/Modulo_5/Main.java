public class Main {
   public static void main(String[] args) {
      Autor autor = new Autor("Ray Bradbury", 40, true);
      Usuario usuario = new Usuario("João", 25);
      Livro livro = new Livro("Fahrenheit 451", "Romance", autor);
      Emprestimo emprestimo = new Emprestimo(livro, usuario);

      Artigo artigo = new Artigo("Entendendo Compiladores", autor, "tecnologia", true);

      System.out.println("O livro não está disponível");
      System.out.println("Livro: " + emprestimo.getLivro().getTitulo());
      System.out.println("Autor: " + emprestimo.getLivro().getAutor().getNome());
      System.out.println("Gênero: " + emprestimo.getLivro().getGenero());
      System.out.println("Usuário: " + emprestimo.getUsuario().getNome());
      System.out.println("Idade: " + emprestimo.getUsuario().getIdade());

     
      System.out.println("Artigo: " + artigo.getTitulo());
      System.out.println("Autor do artigo: " + artigo.getAutor().getNome());
      System.out.println("Gênero do artigo: " + artigo.getGenero());
      System.out.println("Publicado: " + artigo.isPublicado());
   }
}
