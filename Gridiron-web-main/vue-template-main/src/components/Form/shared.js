import Navbar from "../../components/Partials/Navbar";
import NavbarMobile from "../../components/Partials/NavbarMobile";


var MyShared = {
    /* Name */
    name: "Personal",
    /* Data */
    data() {
        return {
            users: null,
        };
    },
    /* Components */
    components: {
        Navbar,
        NavbarMobile,
    },
    /* Props */
    props: {},
    /* Methods */
    methods: {},
    async mounted() {},
};
export default MyShared;