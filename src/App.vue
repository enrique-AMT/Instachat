<template>
  <div id="app">
    <!--<Header />-->
    <router-view/>
  </div>
</template>

<script>
  import Header from './components/Header'
  import LoginScreen from "./components/LoginScreen";
  export default {
  name: 'App',
  components: {
    'Header': Header,
    "LoginScreen": LoginScreen
  },
  data( ){
    return{

    }
  }
}
</script>

<style>
  *{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body{
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.4;
  }
</style>
