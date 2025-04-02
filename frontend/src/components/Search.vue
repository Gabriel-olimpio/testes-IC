<template>
   <div class="container">
        <img src="/Intuitive-are.jpg" alt="logo-intuitivecare" />
        <h2>Buscador de Operadoras</h2>
        <input v-model="termo" placeholder="Digite algum nome" @keyup.enter="buscar"/>
        <button @click="buscar">Buscar</button>

        <ul v-if="results.length">
            <li v-for="op in results" :key="op.Registro_ANS">
                <strong>Operadora: {{ op.Nome_Fantasia || op.Razao_Social }}</strong>
                <p>CNPJ: {{  op.CNPJ }}</p>
            </li>
        </ul>
        <p v-else-if="buscado">Operadora não encontrada...</p>
   </div>
</template>


<script>
import axios from "axios";

export default {
    data() {
        return {
            termo: "",
            results: [],
            buscado: false
        };
    },
    methods: {
        async buscar() {
            if (!this.termo) return;
            try {
                const response = await axios.get(`http://127.0.0.1:5000/buscar?termo=${this.termo}`);
                this.results = response.data;
            } catch (error) {
                console.log("Erro na busca da operadora:", error);
            }
            this.buscado = true;
        }
    }
};
</script>

<style>
.container {
  max-width: 600px;
  margin: auto;
  text-align: center;
}
input {
  padding: 8px;
  margin-right: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  padding: 8px 12px;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
}
button:hover {
  background-color: #0056b3;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  border-bottom: 1px solid #ddd;
  padding: 8px;
}
</style>