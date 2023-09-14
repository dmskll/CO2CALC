import { defineStore } from "pinia"

export const useState = defineStore("State", {

    state: () => ({
        add_calc: false,
        add_use: false,
        change_use: false,
        use_index: 0,
        edit_component: false,
        component_to_edit: {
            index: null,
            system: false,
        }
    }),
    actions: {
        resetState(){ 
            this.add_calc = false;
            this.add_use = false;
            this.change_use = false;
            this.edit_component = false;

        },
    }

})