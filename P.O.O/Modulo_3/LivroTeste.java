public class LivroTeste {
    public static void main(String[] args) {
        Livro livro = new Livro("Dom Casmurro");

        System.out.println("Título: " + livro.getTitulo());
        System.out.println("Disponível: " + livro.isDisponivel());

        livro.setDisponivel(false);

        System.out.println("Disponível após alteração: " + livro.isDisponivel());
    }
}
