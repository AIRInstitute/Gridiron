<!----------------------------------------------->
<!--                  TEMPLATE                 -->
<!----------------------------------------------->
<template>
  <div class="form_container" :style="'--my-font-var:' + primaryFont + ';'">
      <div
        class=""
        v-for="(form) in JSONform.dynamicForm"
        :key="form"
      >
        <label class="labels">{{ form.name }}</label>
        <input
          :v-model="form.id"
          :id="form.id"
          :type="form.type"
          :step="form.step"
          :min="form.min"
          :max="form.max"
          :maxlength="form.maxlength"
          :placeholder="form.placeholder"
          :class="'form-control ' + form.name"
          v-if="
            form.type != 'selector' &&
            form.type != 'checkbox' &&
            form.type != 'radio' &&
            form.type != 'range'
          "
        />        

        <div class="row" v-if="form.type == 'range'">
          <input
            :id="form.id"
            :type="form.type"
            :min="form.min"
            :max="form.max"
            :class="'form-control-range ' + form.name"
            oninput="this.nextElementSibling.value = this.value"
          />
          <output>{{ form.value }}</output>
        </div>

        <select
          class="form-select"
          aria-label="Default select example"
          v-if="form.type == 'selector'"
          :id="form.id"
        >
          <option :value="option" v-for="option in form.options" :key="option">
            {{ option }}
          </option>
        </select>

        <div v-if="form.type == 'checkbox'">
          <div class="form-check" v-for="option in form.options" :key="option">
            <input
              type="checkbox"
              class="form-check-input"
              :id="form.id + ' ' + option"
              :name="form.name"
              :value="option"
            />
            <label :for="option"> &nbsp; {{ option }}</label
            ><br />
          </div>
        </div>

        <div v-if="form.type == 'radio'">
          <div class="form-check" v-for="option in form.options" :key="option">
            <input
              type="radio"
              class="form-check-input"
              :id="form.id + ' ' + option"
              :name="form.name"
              :value="option"
            />
            <label :for="option"> &nbsp; {{ option }}</label
            ><br />
          </div>
        </div>
      </div>
      <button type="submit" class="btn btn-primary" style="float: right" v-if="submit_button">
        Enviar
      </button>
      <div v-if="editFormData!=null">
        <button class="btn btn-danger" @click="$emit('cancel-emitted')">
          Cancel
        </button>
        <button class="btn btn-success" @click="savedata">
          Save
        </button>
      </div>
      <div v-if="add_new==true">
        <button class="btn btn-danger" @click="$emit('cancel-emitted')">
          Cancel
        </button>
        <button class="btn btn-success" @click="addData">
          Save
        </button>
      </div>
  </div>
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
.form_container {
  font-family: var(--my-font-var);
  margin: 1em;
  padding: 1em;
}
a {
  text-decoration: none;
}

.form-control:focus {
  box-shadow: none;
  border-color: var(--my-color-var);
}
.labels {
  font-size: 11px;
}
</style>


