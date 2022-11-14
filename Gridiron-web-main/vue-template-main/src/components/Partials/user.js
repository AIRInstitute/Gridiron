import { defineStore } from "pinia";
import axios from "axios";
import {ref, computed,watch} from "vue";
import qs from "qs";

//const URL = 'http://212.128.140.209:8000/get_token_oauth';

export const useUserStore = defineStore("user", () =>{
    
    const user = ref({
        name: undefined,
        CLIENT_ID: "9688c413-7e9c-4246-bb77-136a57b3a3f9",
        CLIENT_SECRET: undefined,
    })

    const username = computed(() => user.value.name)
    
    function login (newName,pass) {
        var auth = btoa(process.env.VUE_APP_CLIENT_ID + ':' + process.env.VUE_APP_CLIENT_SECRET);
        var basicAuth = "Basic " + auth;              

        // make request
        const payload = {
            'name': newName,
            'password': pass,
            'authorization': basicAuth
        }

        // set headers
        const headers = {
            'Content-Type': 'application/json',
        }  
        //user.name = newName;
        
        const info = axios.post(process.env.VUE_APP_CLIENT_URL, payload, headers)
        .then(response => {
            var data = response.data
            console.log("Data: " + JSON.stringify(data))  
            if(data != "Invalid grant: user credentials are invalid" && data != "Missing parameter: `password`" && data != "Missing parameter: `username`"){
                user.value.name = newName;
                console.log("User: " + user.value.name)
                return true;
            }
            else{
                return false;
            }
            //user.CLIENT_SECRET = data.access_token
                   
        })
        .catch(e => {
            console.log(e);
        })
        
        return info;
        //console.log("Info: " + info);
    }

    const logout = () => {
        user.value.name = undefined;
    }
    const isNotLogged = () => {
        return user.value.name == undefined;
    }

    if(localStorage.getItem("user")){
        user.value = JSON.parse(localStorage.getItem("user"));
    }
    watch(user,
        (userVal) => {
            localStorage.setItem(("user"), JSON.stringify(userVal));
        },
        { deep: true }
    );

    return {user, username, login, logout, isNotLogged}
});



