public class Main {
    public static void main(String[] args) {
        Autor autor = new Autor("Ray Bradbury", 40); // Corrigido nome do autor
        Usuario usuario = new Usuario("João", 25);
        Livro livro = new Livro("Fahrenheit 451", "Romance", autor); // Corrigido título e gênero

        Emprestimo emprestimo = new Emprestimo(
            livro, usuario
        );

        System.out.println("O livro não está disponível");
        System.out.println("Livro: " + livro.getTitulo());
        System.out.println("Autor: " + livro.getAutor().getNome());
        System.out.println("Gênero: " + livro.getGenero());
        System.out.println("Usuário: " + usuario.getNome());
        System.out.println("Idade: " + usuario.getIdade());
    }
}
