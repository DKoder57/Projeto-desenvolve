public class Main {
    public static void main(String[] args) {
        Autor autor = new Autor();
        Usuario usuario = new Usuario();
        Livro livro = new Livro();

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
