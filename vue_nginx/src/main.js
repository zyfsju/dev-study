import Vue from "vue";
import App from "./App.vue";
import msal from "vue-msal";
import router from "./router";
// import store from "./store";

Vue.use(msal, {
    auth: {
        clientId: "<CLIENT_ID>", // Change here
        // authority: "https://login.microsoftonline.com",
        authority: "https://login.microsoftonline.com/<TENANT_ID>", // Change here
        redirectUri: process.env.VUE_APP_AUTH_REDIRECT_URL,
        requireAuthOnInitialize: true,
        // scopes: ["user.read.all", "user.read"], //"mailboxsettings.read", "calendars.readwrite"],
    },

    request: {
        scopes: [
            "user.read.all",
            // `user.read`,
            `profile`,
            // `https://backend-api-hosted-on-functionapp.azurewebsites.net/user_impersonation`,
        ],
    },
    graph: {
        callAfterInit: true,
        endpoints: {
            profile: "/me",
            // photo: { url: "/me/photo/$value", responseType: "blob", force: true },
            avatar: {
                url: "/me/photos/48x48/$value",
                responseType: "blob",
                force: true,
            },
        },
    },
    cache: {
        cacheLocation: "sessionStorage",
    },
});

Vue.config.productionTip = false;

new Vue({
    router,
    // store,
    render: (h) => h(App),
}).$mount("#app");
