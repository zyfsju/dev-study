<template>
  <div class="profile">
    <!--    <img alt="Vue logo" src="../assets/logo.png">-->
    <Profile />
  </div>
</template>

<script>
// @ is an alias to /src
import Profile from "@/components/Profile.vue";

export default {
  name: "Profile",
  components: {
    Profile,
  },
};
</script>
