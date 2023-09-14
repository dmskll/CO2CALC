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
        mix: [
            {
                name: "mix españa",
                emissions: 259,
            },
            {
                name: "renovable 100%",
                emissions: 0,
            },
        ]
    }),
    actions: {
        updateComponentsIsUsed(){ //revisar para no auth
            this.components_is_used.system = []
            this.components_is_used.user = []
            var id;
            var system_component;
            for (const i in this.components.system){
                id = this.components.system[i].id
                system_component = this.components.system[i].system_component;
                const use = Object.values(this.components_use).filter((use) => 
                                                                    use.component === id
                                                                    && (this.user_info.authenticated || system_component));
              this.components_is_used.system.push(use.length != 0)
            }
            for (const i in this.components.user){
                id = this.components.user[i].id
                system_component = this.components.user[i].system_component;
                const use = Object.values(this.components_use).filter((use) => 
                                                                    use.component === id
                                                                    && (this.user_info.authenticated || system_component));
              this.components_is_used.user.push(use.length != 0)
            }
        },
    }

})