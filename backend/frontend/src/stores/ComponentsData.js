import { defineStore } from "pinia"

export const useComponentsData = defineStore("ComponentsData", {

    state: () => ({
        components: {
            system: [],
            user: [],
        },
        components_is_used: {
            system: [],
            user: [],
        },
        components_use: [],
        user_info: {
            authenticated: false,
            },
        calculations: [],
        current_calculation: null,
    }),
    actions: {
        updateComponentsIsUsed(){ //revisar para no auth
            this.components_is_used.system = []
            this.components_is_used.user = []
            for (const i in this.components.system){
              const use = Object.values(this.components_use).filter((use) => 
                                                                    use.component === this.components.system[i].id
                                                                    && this.components.system[i].system_component);
              this.components_is_used.system.push(use.length != 0)
            }
            for (const i in this.components.user){
              const use = Object.values(this.components_use).filter((use) => 
                                                                    use.component === this.components.user[i].id
                                                                    && !this.components.system[i].system_component);
              this.components_is_used.user.push(use.length != 0)
            }
        },
    }

})