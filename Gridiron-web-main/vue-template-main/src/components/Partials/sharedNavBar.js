import { useUserStore } from './user';

var MyShared = {
    name: "Navbar",
    props: {
        title: String,
    },
    data: () => ({
        user: {
            id: String,
            name: useUserStore().user.name,
            picture_url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4cJZdoQ1-7OvvKP-8V1zr9C9qchrF3kw1kA&usqp=CAU',
            rol:"admin"
        }
      }),
      
    beforeCreate: function () {
        const userStore = useUserStore();
        console.log(userStore.user.name);
        if(userStore.isNotLogged()){
            this.$router.push("/");
        }
    },
    components: {},
    methods: {
        async logout() {
            const userStore = useUserStore();
            userStore.logout()
            this.$router.push("/");
        },
        goUserProfile(id) {
            this.$router.push({ path: 'profile', query: { user_id: id } })
        },
        async mounted() {
            const userStore = useUserStore();
            const user = await userStore.getUser();
            this.user = user;
            this.loaded = true;
        },
    },
};
export default MyShared;