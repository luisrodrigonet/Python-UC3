
### 📁 `produtos/models.py`

```python
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Produto(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do produto")
    descricao = models.TextField(help_text="Descrição detalhada do produto")
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Preço de venda do produto"
    )
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='produtos'
    )
    estoque = models.PositiveIntegerField(
        default=0, 
        help_text="Quantidade do produto em estoque"
    )
    disponivel = models.BooleanField(
        default=True, 
        help_text="Indica se o produto está disponível para venda"
    )
    imagem = models.ImageField(
        upload_to='produtos/', 
        blank=True, 
        null=True, 
        help_text="Imagem de exibição do produto"
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']
```

-----

### 📁 `site_loja/models.py`

```python
from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto
from PIL import Image

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(default='perfil_padrao.jpg', upload_to='imagens_perfil')

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.imagem.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.imagem.path)

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=150)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False, help_text="Marca se a mensagem foi lida")

    def __str__(self):
        return f"{self.nome} - {self.assunto}"

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio']

class Comentario(models.Model):
    produto = models.ForeignKey(
        Produto, 
        on_delete=models.CASCADE, 
        related_name='comentarios'
    )
    autor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comentarios'
    )
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return f'Comentário de {self.autor.username} em {self.produto.nome}'

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
        ordering = ['-data_publicacao']

class Compra(models.Model):
    class StatusCompra(models.TextChoices):
        PAGAMENTO_PENDENTE = 'Pendente', 'Pagamento Pendente'
        PROCESSANDO = 'Processando', 'Processando'
        ENVIADO = 'Enviado', 'Enviado'
        ENTREGUE = 'Entregue', 'Entregue'
        CANCELADO = 'Cancelado', 'Cancelado'

    cliente = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    data_compra = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=StatusCompra.choices,
        default=StatusCompra.PAGAMENTO_PENDENTE
    )
    
    def __str__(self):
        return f'Compra #{self.id} - {self.cliente.username}'
    
    def get_total(self):
        total = sum(item.get_custo() for item in self.itens.all())
        return total

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ['-data_compra']

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='itens_comprados')
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome} na Compra #{self.compra.id}'
    
    def get_custo(self):
        return self.preco_unitario * self.quantidade

    class Meta:
        verbose_name = "Item de Compra"
        verbose_name_plural = "Itens de Compra"
```