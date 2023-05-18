<template>
  <main class="back">
    <div id="list-livros">
      <h1>LISTA DE LIVROS</h1>

      <div class="navBar">
        <div>
          <router-link :to="{ name: 'list' }"><button class="botao">Listar Livros</button></router-link>
          <router-link :to="{ name: 'create' }" class="links"><button class="botao">Adicionar Livro</button></router-link>
        </div>

      </div>

      <table class="table table-hover">
        <thead>
          <tr>
            <th>ID</th>
            <th>Título</th>
            <th>Autores</th>
            <th>Editora</th>
            <th>Ano</th>
            <th>ISBN</th>
            <th>Preço</th>
            <th></th>
            <th></th>
          </tr>

        </thead>

        <tbody>
          <tr v-for='livro in livros' v-bind:key="livro">
            <td>{{ livro._id['$oid'] }}</td>
            <td>{{ livro.Titulo }} </td>
            <td>{{ livro.Autores }} </td>
            <td>{{ livro.Editora }} </td>
            <td>{{ livro.Ano }} </td>
            <td>{{ livro.ISBN }}</td>
            <td>{{ livro.Preco }}</td>
            <td>
              <router-link :to="{ name: 'delete', params: { id: livro._id['$oid'] } }"><button class="delete">Remover</button></router-link>
            </td>
            <td>
              <router-link :to="{ name: 'update', params: { id: livro._id['$oid'] } }"><button class="update">Alterar</button></router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      livros: []
    }
  },

  created: function () {
    this.fetchUsuarioData()
  },

  methods: {
    fetchUsuarioData: function () {
      this.$http.get('http://localhost:5000/index').then(
        (response) => {
          this.livros = response.body
        },
        (response) => { }
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
    justify-content: left;
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
