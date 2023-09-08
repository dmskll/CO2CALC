import { defineStore } from "pinia"
import { axios } from "@/common/api.service.js"
import { useComponentsData } from "@/stores/ComponentsData"
import { useNoAuthID } from "@/stores/NoAuthID"


export const useOperations = defineStore("Operations", {
    
    state: () => ({
        store : useComponentsData(),
        max_id: useNoAuthID(),
    }),

    actions: {
        async saveCalculation(calculation){
            console.log(this.store.user_info)
            const body = {
              "name": calculation.name
            } 
            if(calculation.id){
              // el componente existe
              this.store.current_calculation.name = body.name;
              if(!this.store.user_info.authenticated)
                return
      
              let endpoint = "/api/calculation/"+ calculation.id + "/"
                await axios.put(endpoint, body)
                  .then(response => {
                    console.log(response.data);
                  })
                  .catch(error => {
                    this.errorMessage = error.message;
                    console.error("There was an error!", error);
                  });
            }
            else{
              // el componente NO existe
              if(!this.store.user_info.authenticated){
                this.store.calculations.push({
                  "id": this.max_id.calculation,
                  "owner": null,
                  "name": body.name,
                 })
                 this.max_id.calculation++;
                 this.changeCalculation(this.store.calculations.length - 1);
                 return
              } 
              console.log(this.store.current_calculation )

              let endpoint = "/api/calculation/"
              await axios.post(endpoint, body)
                .then(response => {
                  this.store.calculations.push(response.data);
                  this.changeCalculation(this.store.calculations.length - 1);
                  console.log(this.store.current_calculation )
                })
                .catch(error => {
                  this.errorMessage = error.message;
                  console.error("There was an error!", error);
                });
                console.log(this.store.current_calculation )

            }
        },
        changeCalculation(index){
            this.store.current_calculation = this.store.calculations[index];
        },
        async newComponentUse(component, emission){
            let time = component.is_server ? 6 : 0;
            if(!this.store.user_info.authenticated){
              this.store.components_use.push({
                "id": this.max_id.use,
                "system_component": component.system_component,
                "component": component.id,
                "hours": time,
                "server_years": 6,
                "emissions": parseInt(emission),
              })
              this.max_id.use++;
              this.store.updateComponentsIsUsed();
              return
            } 
              const body = {
                "component": component.id,
                "hours": time,
                "server_years": 6,
                "emissions": parseInt(emission),
              }
              let endpoint = "/api/calculation/"+ this.store.current_calculation.id +"/usage/"
              await axios.post(endpoint, body)
              .then(response => {
                response.data["system_component"] = component.system_component;
                this.store.components_use.push(response.data);
                this.store.updateComponentsIsUsed();
              })
              .catch(error => {
                this.errorMessage = error.message;
                console.error("There was an error!", error);
              });
        },
        saveComponentData(component, index){
           
        // El cuerpo que se enviará en el POST
            const body = {
            "worst_case": component.worst_case,
            "best_case": component.best_case,
            "middle_case": component.middle_case,
            "cfp": 0,
            "cfp_build_phase": component.cfp,
            "cfp_deviation_standard": component.cfp_deviation_standard,
            "name": component.name,
            "description": component.description,
            "is_server": component.is_server,
            "hosted_apps": component.hosted_apps,
            };
    
            if (component.id){
            //si tiene id es un uso existente entonces hay que editarlo
            //encontramos el index en la array de usage y modificamos el elemento, 
            //si no se encuentra el index es -1
            
            //console.log("id")
            //const index = this.local_data.usage.findIndex((local_data) => local_data.id === data.id);

            if(!this.store.user_info.authenticated){
                this.store.components.user[index] = component;
                return
            }
    
            let endpoint = "/api/component/" + component.id + "/"
            axios.put(endpoint, body)
            .then(response => {
                console.log(response.data);
                this.store.components.user[index] = component;
            })
            .catch(error => {
                this.errorMessage = error.message;
                console.error("There was an error!", error);
            });    
            
            }
            else { //si no tiene indice significa que es un componente nuevo
        
                if(!this.store.user_info.authenticated){
                    //le damos -1 como id para marcar que se ha creado pero que no se añade en la database
                    component["id"] = this.max_id.component;
                    component["system_component"] = false;
                    this.store.components.user.push(component);
                    this.max_id.component++;
                    return
                }
        
                let endpoint = "/api/component/"
                console.log(body);
                axios.post(endpoint, body)
                    .then(response => {
                    console.log(response.data);
                    this.store.components.user.push(response.data);
                    })
                    .catch(error => {
                    this.errorMessage = error.message;
                    console.error("There was an error!", error);
                    });
            }
        },
        deleteComponent(index){
            const id = this.store.components.user[index].id
            this.store.components.user.splice(index, 1);
                
            if(!this.store.user_info.authenticated)
                return
        
            let endpoint = "/api/component/" + id +"/";
                axios.delete(endpoint)
                    .then(response => {
                    console.log(response);
                    })
                    .catch(error => {
                    this.errorMessage = error.message;
                    console.error("There was an error!", error);
                    });
        },
    }

})