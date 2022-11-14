import Navbar from "../../components/Partials/Navbar";
import NavbarMobile from "../../components/Partials/NavbarMobile";
import Formulary from "../../components/Partials/Formulary/Formulary";
import Table from "../../components/Partials/Table/Table";


var $ = require('jquery');
var dt = require('datatables.net');

var MyShared = {
    /* Name */
    name: "Personal",
    /* Data */
    data() {
        return {
            users: null,
            JSON_table_form: {"dynamicForm": {}},
            JSON_table_data: {"table_n": {}},
        };
    },
    /* Components */
    components: {
        Navbar,
        NavbarMobile,
        Formulary,
        Table
    },
    async mounted() {
        await (this.JSON_table_form = require('./form.json'));
        await (this.JSON_table_data = require('./table.json'));

        console.log(this.JSON_table_data)
    },
};
export default MyShared;