public class Main {
    public static void main(String[] args) {
        Autor autor = new Autor("Ray Bradburry", 40);
        Usuario usuario = new Usuario("Luca", 25);
        Livro livro = new Livro("Farenheit 451", "alfabeto", autor);

        Emprestimo emprestimo = new Emprestimo(
            livro, usuario,
            "Quarta Maio 08 23:37:21 BRT 2024",
            "Quarta Maio 08 23:37:21 BRT 2024"
        );

        System.out.println("O livro não está disponível");
        System.out.println("Livro: " + livro.getTitulo());
        System.out.println("Autor: " + livro.getAutor().getNome());
        System.out.println("Genero: " + livro.getGenero());
        System.out.println("Usuario: " + usuario.getNome());
        System.out.println("Idade: " + usuario.getIdade());
        System.out.println("Data de Retirada: " + emprestimo.getDataRetirada());
        System.out.println("Data de Devolucao: " + emprestimo.getDataDevolucao());
    }
}
