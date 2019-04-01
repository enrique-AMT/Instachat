<template>
  <div>
    <md-toolbar class="md-primary" md-elevation="1">
      <!--<h3 class="md-title" style="flex: 1">InstaChat</h3>-->
      <md-button class="md-icon-button" style="alignment: center">
          <img src="../assets/EditIcon.png" alt="edit">
      </md-button>
      <md-button class="md-icon-button" style="alignment: center">
        <img src="../assets/DownArrow.png" alt="downArrow">
      </md-button>
    </md-toolbar>

    <md-card>
  <md-list class="md-triple-line">
    <md-list-item>
      <md-avatar>
        <img src="https://placeimg.com/40/40/people/1" alt="People">
      </md-avatar>

      <div class="md-list-item-text">
        <span>Ali Connors</span>
        <span>Brunch this weekend?</span>
        <p>I'll be in your neighborhood doing errands this week. Do you want to meet?</p>
      </div>

      <md-button class="md-icon-button md-list-action">
        <md-icon class="md-primary">star</md-icon>
      </md-button>
    </md-list-item>

    <md-divider class="md-inset"></md-divider>

    <md-list-item>
      <md-avatar>
        <img src="https://placeimg.com/40/40/people/6" alt="People">
      </md-avatar>

      <div class="md-list-item-text">
        <span>me, Scott, Jennifer</span>
        <span>Summer BBQ</span>
        <p>Wish I could come, but I'm out of town this week. :(</p>
      </div>

      <md-button class="md-icon-button md-list-action">
        <md-icon>star_border</md-icon>
      </md-button>
    </md-list-item>

    <md-divider class="md-inset"></md-divider>

    <md-list-item>
      <md-avatar>
        <img src="https://placeimg.com/40/40/people/5" alt="People">
      </md-avatar>

      <div class="md-list-item-text">
        <span>Sandra Adams</span>
        <span>Oui oui</span>
        <p>Do you have Paris recommendations? Have you visited good places?</p>
      </div>

      <md-button class="md-icon-button md-list-action">
        <md-icon>star_border</md-icon>
      </md-button>
    </md-list-item>

    <md-divider class="md-inset"></md-divider>

    <md-list-item>
      <md-avatar>
        <img src="https://placeimg.com/40/40/people/8" alt="People">
      </md-avatar>

      <div class="md-list-item-text">
        <span>Trevor Hansen</span>
        <span>Order confirmation</span>
        <p>Thank you for your recent order from Amazon</p>
      </div>

      <md-button class="md-icon-button md-list-action">
        <md-icon>star_border</md-icon>
      </md-button>
    </md-list-item>
  </md-list>
    </md-card>
  </div>
</template>

<script>
    export default {
        name: "HomeScreen"
    }
</script>

<style scoped>

  .md-card {
    width: 25%;
    height: 100%;
    margin: 4px;
    display: inline-block;
    vertical-align: top;
  }

</style>
