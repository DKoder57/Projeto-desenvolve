public class Autor extends Usuario {
    private boolean tradicional;

    public Autor(String nome, int idade, boolean tradicional) {
        super(nome, idade);
        this.tradicional = tradicional;
    }

    public boolean isTradicional() {
        return tradicional;
    }

    public void setTradicional(boolean tradicional) {
        this.tradicional = tradicional;
    }
}
