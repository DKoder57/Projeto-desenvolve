Eimport java.time.LocalDateTime;

public class Emprestimo {
    private Livro livro;
    private Usuario usuario;
    private LocalDateTime dataRetirada;
    private LocalDateTime dataDevolucao;

    public Emprestimo(Livro livro, Usuario usuario, LocalDateTime dataRetirada, LocalDateTime dataDevolucao) {
        this.livro = livro;
        this.usuario = usuario;
        this.dataRetirada = dataRetirada;
        this.dataDevolucao = dataDevolucao;
        livro.setDisponivel(false);
    }

    public Livro getLivro() {
        return livro;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public LocalDateTime getDataRetirada() {
        return dataRetirada;
    }

    public LocalDateTime getDataDevolucao() {
        return dataDevolucao;
    }
}

