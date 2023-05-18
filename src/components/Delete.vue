<template>
  <div id="delete-livro">
      <h1>REMOVER LIVRO</h1>

      <div class="navBar">
          <div>
              <router-link :to="{ name: 'list' }"><button class="botao">Listar Livros</button></router-link>
              <router-link :to="{ name: 'create' }" class="links"><button class="botao">AdicionarLivro</button></router-link>
          </div>
      </div>

      <form v-on:submit.prevent="removerLivro">

          <div class='form-group'>
              <label name='IDLivro'>ID:</label>
              <input type='text' class='form-control' disabled v-model='livro.id' id='IDLivro' />
          </div>
          <div class="form-group">
              <label name="titulo">Título:</label>
              <input type="text" class="form-control" disabled v-model="livro.Titulo" id="titulo" required>
          </div>
          <div class="form-group">
              <label name="autores">Autores:</label>
              <input type="text" class="form-control" disabled v-model="livro.Autores" id="autores" required>
          </div>

          <div class="form-group">
              <label name="editora">Editora:</label>
              <input type="text" class="form-control" disabled v-model="livro.Editora" id="editora" required>
          </div>

          <div class="form-group">
              <label name="ano">Ano:</label>
              <input type="number" class="form-control" disabled v-model="livro.Ano" id="ano" required>
          </div>

          <div class="form-group">
              <label name="isbn">ISBN:</label>
              <input type="number" class="form-control" disabled v-model="livro.ISBN" id="isbn" required>
          </div>

          <div class="form-group">
              <label name="preco">Preço:</label>
              <input type="number" class="form-control" disabled v-model="livro.Preco" id="ano" required>
          </div>

          <div class="form-grup">
            <button class="botao-delete" @click="deleteLivro">Remover</button>
        </div>
      </form>
  </div>
</div></template>

<script>
export default {
  data() {
      return {
          livro: {}
      }
  },
  created: function () {
      this.getLivroData()
  },
  methods: {
      getLivroData: function () {
          this.$http.get('http://localhost:5000/getid/' + this.$route.params.id).then(
              (response) => {
                  this.livro.id = this.$route.params.id
                  this.livro.Titulo = response.body['Titulo']
                  this.livro.Autores = response.body['Autores']
                  this.livro.Editora = response.body['Editora']
                  this.livro.Ano = response.body['Ano']
                  this.livro.ISBN = response.body['ISBN']
                  this.livro.Preco = response.body['Preco']
                  this.$forceUpdate()
              },
              (response) => { }
          )
      },
      deleteLivro: function () {
          this.$http.get('http://localhost:5000/delete/' + this.livro.id).then(
              (response) => {
                  this.livro = {}
                  alert(response.body['mensagem'])
                  this.$router.push('list')
              },
              (response) => {
                  alert(response.body['mensagem'])
              }
          )
      }
  }
}
</script>

<style scoped>

body {
    font-family: Arial, sans-serif;
    background: linear-gradient(to top left, black, blue); /* Adicionado gradiente de fundo */
    color: #333;
}

h1 {
    display: flex;
    justify-content: center;
    color: #4A90E2;
}

.navBar {
    display: flex;
    justify-content: left;
    align-items: center;
    margin-bottom: 10px;
}

.botao, .botao-add, .botao-delete {
    height: 30px;
    border: none;
    border-radius: 5px;
    background-color: #4A90E2;
    color: #FFF;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.botao:hover, .botao-add:hover, .botao-delete:hover {
    background-color: #F89406;
}

.form-group {
    padding: 5px;
    display: flex; /* Adicionado flex para posicionar os elementos em linha */
    justify-content: space-between; /* Espaçamento entre os elementos */
    align-items: center; /* Alinhamento vertical */
}

label {
    color: white; /* Cor do texto do label para branco */
}

input[type=text], select, textarea, input[type=number] {
    height: 30px;
    flex-grow: 1; /* Adicionado para preencher o espaço disponível */
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    background-color: white; /* Fundo branco */
}

.botao-delete {
    background-color: #D0021B;
}

.botao-delete:hover {
    background-color: #F89406;
}

</style>
