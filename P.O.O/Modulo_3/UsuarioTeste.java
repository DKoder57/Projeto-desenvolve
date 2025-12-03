public class UsuarioTeste {
    public static void main(String[] args) {
        Usuario usuario = new Usuario("João", 30);

        System.out.println("Nome: " + usuario.getNome());
        System.out.println("Idade: " + usuario.getIdade());
    }
}
