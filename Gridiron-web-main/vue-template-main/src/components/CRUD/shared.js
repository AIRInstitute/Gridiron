import Navbar from "../../components/Partials/Navbar";
import NavbarMobile from "../../components/Partials/NavbarMobile";
import Formulary from "../../components/Partials/Formulary/Formulary";
import Table from "../../components/Partials/Table/Table";
import AddModal from "../../components/Partials/AddModals/AddModal";



var $ = require('jquery');
var dt = require('datatables.net');

var MyShared = {
    /* Name */
    name: "Personal",
    /* Data */
    data() {
        return {
            JSON_table_form: {"dynamicForm": {}},
            JSON_table_data: {"table_n": {}},
        };
    },
    /* Components */
    components: {
        Navbar,
        NavbarMobile,
        Formulary,
        Table,
        AddModal
    },
    async mounted() {
        await (this.JSON_table_form = require('./TableConfig/form.json'));
        await (this.JSON_table_data = require('./TableConfig/table.json'));
    },
};
export default MyShared;