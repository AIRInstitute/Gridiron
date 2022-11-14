import Navbar from "../../../components/Partials/Navbar";

var MyShared = {
    /* Name */
    name: "JSONform.dynamicForm",
    /* Data */
    data() {
        return {
            col_num:0,
        };
    },
    /* Components */
    components: {
        Navbar,
    },
    /* Props */
    props: {
        JSONform: {"dynamicForm": {}},
        submit_button: Boolean,
        editFormData: null,
        add_new:false,
        exampleObj:{}
    },
    /* Methods */
    methods: {
        test_event(i, invalids,textarea){
            textarea[i].addEventListener('keydown', (e) => {
                if(invalids.indexOf(e.key) == -1){
                  // do something
                } else {
                  e.preventDefault();
                }
              });
        },
        savedata(){
            for(var data in this.editFormData){
                console.log(data);
                var input = document.getElementById(data);
                if(input != null){
                    console.log(input)
                    this.editFormData[data] = input.value;
                }else{
                    var inputs = $("input[id*='"+data+"']").each(function (i, el) {
                        //It'll be an array of elements
                    });
                    console.log(inputs); 
                    var options_checked = [];
                    for(var input2 in inputs){
                        console.log(inputs[input2].value + " --> " + inputs[input2].checked);
                        if(inputs[input2].checked){
                            options_checked.push(inputs[input2].value)
                            console.log(options_checked);
                            if(inputs[input2].type == 'checkbox'){
                                this.editFormData[data] = options_checked;  
                            }else{
                                if(inputs[input2].type == 'radio')
                                    this.editFormData[data] = options_checked[0];
                            }
                        }
                    }
                    if(options_checked.length == 0)
                        this.editFormData[data] = []
                }        
            }
            /* ***** Modify data in db (new data is in editFormData) ***** */
            this.$emit('save-emitted',this.editFormData)
        },
        addData(){
            var new_data = {"data":{},
        "id":String};
            //console.log(new_data);
            for(var data in this.exampleObj.data){
                //console.log(data);
                var input = document.getElementById(data);
                if(input != null){
                    //console.log(input)
                    new_data.data[data] = input.value;
                }else{
                    var inputs = $("input[id*='"+data+"']").each(function (i, el) {
                        //It'll be an array of elements
                    });
                    console.log(inputs); 
                    var options_checked = [];
                    for(var input2 in inputs){
                        //console.log(inputs[input2].value + " --> " + inputs[input2].checked);
                        if(inputs[input2].checked){
                            options_checked.push(inputs[input2].value)
                            //console.log(options_checked);
                            if(inputs[input2].type == 'checkbox'){
                                new_data.data[data] = options_checked;  
                            }else{
                                if(inputs[input2].type == 'radio')
                                    new_data.data[data] = options_checked[0];
                            }
                        }
                    }
                    if(options_checked.length == 0)
                        new_data.data[data] = []
                }        
            }
            //console.log("=== Example Obj ===");
            //console.log(this.exampleObj);
            //console.log("=== New data ===");
            //console.log(new_data);
            new_data.id= "0";
            /* ***** Add data in db (new data is in editFormData) ***** */
            this.$emit('add-emitted',new_data);
        }
    },
    async created() {
        await this.JSONform;
        let name, invalids, i=0;
        let textarea = [];
        for(var key in this.JSONform.dynamicForm){
            if (this.JSONform.dynamicForm.hasOwnProperty(key)) {
                //console.log("----"+ key + "----");

                /* ----- set values of selected rows for edit -----*/ 
                for(var datakey in this.editFormData){
                    if(datakey == key){
                        var input = document.getElementById(datakey)
                        //console.log('--- ' + datakey+' ---');
                        //console.log(input)
                        if(input != null){
                            if(input.tagName == 'SELECT'){
                                var option = document.getElementById(datakey)
                                option.value = this.editFormData[datakey]
                            }
                            if(input.type != 'file')
                                input.value = this.editFormData[datakey];
                        }else{
                            if(typeof(this.editFormData[datakey]) == 'object'){
                                for(var k=0; k<this.editFormData[datakey].length; k++){
                                    //console.log(datakey + " " + this.editFormData[datakey][k]);
                                    var input2 = document.getElementById(datakey + " " + this.editFormData[datakey][k])
                                    input2.checked = true;
                                }
                            }else{
                                var input2 = document.getElementById(datakey + " " + this.editFormData[datakey])
                                input2.checked = true;
                            }     
                        }
                    }
                }
                for(var key2 in this.JSONform.dynamicForm[key]){
                    if (this.JSONform.dynamicForm[key].hasOwnProperty(key2)) {
                        //console.log(key2 + " -> " + this.JSONform.dynamicForm[key][key2]);
                        if(key2 == "id"){
                            name = this.JSONform.dynamicForm[key][key2];
                        }
                        if(key2 == "invalid_chars"){
                            invalids = Object.values(this.JSONform.dynamicForm[key][key2]);
                            //console.log(invalids);
                            textarea.push(document.getElementById(name));
                            //console.log(textarea);
                            this.test_event(i,invalids,textarea)
                            i++;
                        }
                        
                    }
                }
            }
        }
    },emits: ['cancel-emitted','save-emitted','add-emitted']
};
export default MyShared;