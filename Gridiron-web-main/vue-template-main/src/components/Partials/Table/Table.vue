<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
<div class="table_container" :style="'--my-font-var:' + primaryFont + ';'">
    <button class="btn btn-primary" style="float:right;" @click="addRow(JSON_table_data.table_data)" v-if="crud_option"><i class="fas fa-plus-square"></i></button>
    <table
      id="example"
      class="display nowrap"
      width="100%"
      :style="'--my-font-var:' + primaryFont + ';'"
    >
      <thead>
        <tr>
          <th v-for="header in JSON_table_form.dynamicForm" :key="header">{{header.name}}</th>
          <th v-if="crud_option">Options</th>
        </tr>
      </thead>

      <tfoot>
        <tr>
          <th v-for="header in JSON_table_form.dynamicForm" :key="header">{{header.name}}</th>
          <th v-if="crud_option">Options</th>
        </tr>
      </tfoot>

      <tbody>
        <tr v-for="row in JSON_table_data.table_data" :key="row" :class="row.id">
          <td v-for="(data) in row.data" :key="data" >
            <section v-if="data != 'button'">{{data}}</section>
          </td>
          <td v-if="crud_option">
          <div class="row">
            <div class="col-4">
              <button class="btn btn-danger" @click="setRowToDelete(row.id)"><i class="fas fa-trash-alt"></i></button>
            </div>
            <div class="col-4">
              <button class="btn btn-warning" style="color:white" @click="editRow(row.id, row.data)"><i class="fas fa-pen"></i></button>
            </div>
            <div class="col-4">
              <button class="btn btn-success" @click="viewRow(row.id)"><i class="fas fa-eye"></i></button>
            </div>
          </div>
          </td>
        </tr>
      </tbody>
    </table>
</div>

  <AddModal ref="delete">
    <template v-slot:header>
      <h4>Are you sure you want to delete the item?</h4>
    </template>
    <!-- Habra que controlar que labels mostrar cuando sepamos que hay en material e historico... -->
    <template v-slot:body>

    </template>
    <template v-slot:footer>
      <div>
        <button class="btn btn-danger" @click="$refs.delete.closeModal()">
          No
        </button>
        <button class="btn btn-success" @click="$refs.delete.closeModal(); deleteRow();">
          Yes
        </button>
      </div>
    </template>
  </AddModal>

  <AddModal ref="edit">
    <template v-slot:header>
      <h4>Update your item</h4>
    </template>
    <!-- Habra que controlar que labels mostrar cuando sepamos que hay en material e historico... -->
    <template v-slot:body>
      <Formulary :JSONform="JSON_table_form" :submit_button="false" :editFormData="editFormData" @cancel-emitted="cancelEmitted" @save-emitted="editEmitted"></Formulary>
    </template>
    <template v-slot:footer>
    </template>
  </AddModal>

  <AddModal ref="add">
    <template v-slot:header>
      <h4>Add</h4>
    </template>
    <!-- Habra que controlar que labels mostrar cuando sepamos que hay en material e historico... -->
    <template v-slot:body>
      <Formulary :JSONform="JSON_table_form" :submit_button="false" @add-emitted="addEmitted" @cancel-emitted="cancelEmitted" :add_new="true" :exampleObj="exampleObj"></Formulary>
    </template>
    <template v-slot:footer>
    </template>
  </AddModal>

</template>

<!----------------------------------------------->
<!--                    SCRIPT                 -->
<!----------------------------------------------->
<script>
import MyShared from "./shared";

export default {
  mixins: [MyShared],
};
</script>

<!----------------------------------------------->
<!--                    STYLES                 -->
<!----------------------------------------------->
<style scoped>
.table_container {
  font-family: var(--my-font-var);
  width: 100%;
  padding-bottom: 1em;
  overflow-x: auto;
}
table {
  border-collapse: collapse;
  width: 100%;
}

td,
th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
.col-4{
  justify-content: center;
  padding: 0.2em;
}
</style>


