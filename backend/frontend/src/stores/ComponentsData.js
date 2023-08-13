import { defineStore } from "pinia"

export const useComponentsData = defineStore("ComponentsData", {

    state: () =>{
        return {
            components: {
                system: [],
                user: [],
            },
            components_use: [],
            user_info: {
                authenticated: false,
              },
            calculations: [],
            current_calculation: null,

        }
    },
    actions: {

    }

})