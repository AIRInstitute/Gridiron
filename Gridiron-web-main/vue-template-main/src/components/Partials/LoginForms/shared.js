import { useUserStore } from '../user';


var MyShared = {
    /* Name */
    name: "LoginForm",
    inject: ["mq"],

    /* Data */
    data: () => ({
        pass: null,
        username: useUserStore().user.name,
        loginfail: false,
    }),

    /* Components */
    components: {},
    /* Props */
    props: {},
    /* Methods */
    methods: {
        onEnter(username, pass) {
            this.login(username, pass);
        },
        login(username, pass) {
            //const userStore = useUserStore();
            // username.login() en Gridiron-web-main\vue-template-main\src\components\Partials\user.js
            var res = useUserStore().login(username, pass);
            console.log("Res: ", res);
            
            res.then((value) => {
                if (value) {
                    console.log("Login completed")
                    this.$router.push("Dashboard");

                } else {
                    console.log("Login failed");
                    this.loginfail = true;
                }
            });
            
            /*
            if (res) {
                console.log("Login completed")
                this.$router.push("Dashboard");    
                           
            } else {
                console.log("Login failed");
                this.loginfail = true;
            }
            */
        }
    },
    /* Emits */
    emits: ["emits", "emits"],
};

export default MyShared;