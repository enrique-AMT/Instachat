<template>
  <header class="header">
    <h1>InstaChat</h1>
    <div id="nav">
      <md-field>
        <label>Type here!</label>
        <md-input v-model="type"></md-input>
        <span class="md-helper-text">Helper text</span>
      </md-field>
      <!--<router-link to="/">Home</router-link> |-->
      <!--<router-link to="/about">About</router-link>-->
    </div>
  </header>
</template>

<script>
  export default {
    name: 'Header'
  }
</script>

<style scoped>
  .header {
    background: #5292f9;
    color: #fff;
    text-align: left;
    padding: 10px;
  }

  .header a {
    color: #fff;
    padding-right: 5px;
    text-decoration: none;
  }
</style>
