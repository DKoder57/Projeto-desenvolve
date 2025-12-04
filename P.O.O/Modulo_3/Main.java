public class Main {
    public static void main(String[] args) {
        Autor autor = new Autor(null, 0, false);
        Usuario usuario = new Usuario(null, 0);
        Livro livro = new Livro(null, null, autor);

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
