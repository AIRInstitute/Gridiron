import Navbar from "../../components/Partials/Navbar";
import NavbarMobile from "../../components/Partials/NavbarMobile";


var MyShared = {
    /* Name */
    name: "DesktopInvetory",
    /* Data */
    data() {
        return {
            user: {
                name: "Pedro",
                surname: "Garcia",
                phone: "345 859 547",
                email: "pedro@gmail.com",
                picture_url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4cJZdoQ1-7OvvKP-8V1zr9C9qchrF3kw1kA&usqp=CAU',
                country: "España",
                state: "Castilla y Leon"
            }

        };
    },
    /* Components */
    components: {
        Navbar,
        NavbarMobile
    },
    /* Props */
    props: {},
    /* Methods */
    methods: {},
    async mounted() {
        let user_id = this.$route.query.user_id

        //  LLamada a la api para pedir los datos
        /*
        await fetch("https://deepvaluemap.ddns.net/api", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    query: `
                    {
                        user(id:"` + user_id + `") {
                          name
                          email
                          picture_url
                        }
                      }
                      
              `,
                    variables: {
                        now: new Date().toISOString(),
                    },
                }),
            })
            .then((res) => res.json())
            .then((result) => {
                this.user = result["data"]["user"];
                if (this.user.picture_url == "") {
                    this.user.picture_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4cJZdoQ1-7OvvKP-8V1zr9C9qchrF3kw1kA&usqp=CAU"
                }
            });
            */
    },
};
export default MyShared;