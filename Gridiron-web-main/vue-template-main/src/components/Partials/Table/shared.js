import Navbar from "../../../components/Partials/Navbar";
import AddModal from "../../../components/Partials/AddModals/AddModal";
import Formulary from "../../../components/Partials/Formulary/Formulary";

var MyShared = {
    /* Name */
    name: "JSONform.dynamicForm",
    /* Data */
    data() {
        return {
            col_num:0,
            editFormData: null,
            exampleObj: null,
            deleteRowId: String,
        };
    },
    /* Components */
    components: {
        Navbar,
        AddModal,
        Formulary
    },
    /* Props */
    props: {
        JSON_table_data: {"table_data": [{}]},
        JSON_table_form: {"dynamicForm": {}},
        crud_option:false,
    },
    /* Methods */
    methods: {
        addRow(data){
            /* ***** Ojo la tabla tiene que tener un elemento -> se prevee cambiar esto ***** */
            this.exampleObj = data[0];
            this.$refs.add.openModal();
        },
        setRowToDelete(id){
            this.deleteRowId = id
            this.$refs.delete.openModal();
            console.log(this.deleteRowId);
        },
        deleteRow(){
            for(var row in this.JSON_table_data.table_data){
                if(this.deleteRowId == this.JSON_table_data.table_data[row].id){
                    console.log(this.JSON_table_data.table_data[row]);
                    this.JSON_table_data.table_data.splice(row);
                }
            }
        },
        editRow(id,data){
            this.$refs.edit.openModal();
            this.editFormData = data;
            //console.log(this.editFormData);
        },
        viewRow(id){
            
        },
        cancelEmitted(){
            this.$refs.edit.closeModal();
            this.$refs.add.closeModal();
        },
        editEmitted(new_data){
            console.log(new_data);
            this.$refs.edit.closeModal();
        },
        addEmitted(new_data){
            console.log(new_data);
            console.log("aqui");
            console.log(this.JSON_table_data.table_data);
            this.JSON_table_data.table_data.push(new_data);
            console.log(this.JSON_table_data.table_data);
            this.$refs.add.closeModal();
        }
    },
    async mounted() {
        // Load data table
        $(document).ready(function() {
            var table = $('#example').DataTable();
            $('input:checkbox').on('change', function() {
                table.draw();
            });
        });

        await console.log(this.JSON_table_data);

    },
};
export default MyShared;