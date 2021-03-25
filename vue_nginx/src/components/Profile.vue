<template>
  <div>
    <div>USER PROFILE</div>
    <div v-if="user" style="text-align: center;">
      <el-avatar :size="100" :src="user.avatar"></el-avatar>
      <h4>{{ user.name }}</h4>
      <div><button @click="$msal.signOut()">logout</button></div>
      <!-- {{ user }} -->
    </div>
    <div v-else>
      Please sign-in <button @click="$msal.signIn()">Sign In</button>
    </div>

    <!--     <div>
      <p>access token: {{ msal.accessToken }} id token: {{ msal.idToken }}</p>
    </div> -->
  </div>
</template>

<script>
//Importing the mixin locally (omit the following line if you are using the 'framework.globalMixin' option)
import { msalMixin } from "vue-msal";

export default {
  name: "ProfileComponent",
  mixins: [msalMixin],
  computed: {
    user() {
      let user = null;
      if (this.msal.isAuthenticated) {
        // Note that the dollar sign ($) is missing from this.msal
        user = {
          ...this.msal.user,
          profile: {},
        };
        if (this.msal.graph && this.msal.graph.profile) {
          user.profile = this.msal.graph.profile;
        }
        if (this.msal.graph && this.msal.graph.avatar) {
          const url = window.URL || window.webkitURL;
          const blobUrl = url.createObjectURL(this.msal.graph.avatar);
          user.avatar = blobUrl;
        }
      }
      return user;
    },
  },
};
</script>
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
