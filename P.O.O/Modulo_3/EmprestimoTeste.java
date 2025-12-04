public class EmprestimoTeste {
    public static void main(String[] args) {
        Livro livro = new Livro("Dom Casmurro", null, null);
        Usuario usuario = new Usuario("João", 0);

        Object emprestimo;
        System.out.println("Livro: " + ((Object) emprestimo).getLivro());
        System.out.println("Usuário: " + ((Object) emprestimo).getUsuario());
        System.out.println("Disponível: " + livro.isDisponivel());
    }
}
