<template>

  <div style="display: flex;  justify-content: center;">
    <div style="flex: 1; text-align: left;" >
      <p v-if="!dialog">{{ local_data.name }}</p>
    <el-form
      :model="local_data"
      style="max-width: 300px"
      :disabled="!dialog"
    >
      <el-popover
        v-if="dialog"
        :visible="local_data.name == ''"
        placement="bottom"
        :width="220"
        content="Introduce un valor valido"
      >
      <template #reference>
        <el-input
          v-if="dialog"
          v-model="local_data.name"
          type="textarea"
          autosize
          placeholder="Nombre"
          style="margin-top: 10px;"
        />
      </template>
      </el-popover>

    </el-form>
  </div>

  <el-form
    style="flex: 2; display: flex;"
    label-position="top"
    :inline="true"
  >
  

      <el-form-item label="Horas usadas" v-if="show_use && !local_data.is_server" style="flex: 1;" >
        <el-popover
          :visible="local_use.hours == null"
          placement="bottom"
          :width="220"
          content="Introduce un valor valido"
        >
          <template #reference>
            <el-input-number 
              v-model="local_use.hours" 
              @focusin="old_hours=local_use.hours" 
              @focusout="saveHours" 
              :precision="2" 
              :step="0.1" 
              :max="1000" 
              :controls="false" 
            />
          </template>
        </el-popover>
      </el-form-item>
      <el-form-item label="Años de uso" v-if="show_use && local_data.is_server" style="flex: 1;">
        <el-popover
          :visible="local_use.server_years == null"
          placement="bottom"
          :width="220"
          content="Introduce un valor valido"
        >
          <template #reference>
            <el-input-number 
              v-model="local_use.server_years" 
              @focus="old_hours=local_use.server_years" 
              @focusout="saveHours"  
              :min="1" 
              :max="15" 
              :controls="false" 
            />
          </template>
        </el-popover>
      </el-form-item>
      <el-form-item label="Emisiones" v-if="show_use" style="flex: 1;">
      <el-popover
        v-if="show_use"
        :visible="local_use.emissions == ''"
        placement="bottom"
        :width="220"
        content="Introduce un valor valido"
      >
        <template #reference>
          <el-input v-if="show_use" @input="handleInput" @focusin="old_emissions=local_use.emissions" @focusout="saveEmissions" v-model="local_use.emissions" maxlength="3" >
                    <template #prepend>
                      <el-dropdown>
                      <el-button style="width: 3.7em;">
                        <font-awesome-icon icon="fa-solid fa-bolt" size="lg" /> 
                      </el-button>
                      <template #dropdown>
                        <el-dropdown-menu >
                          <div v-for="(mix) in store.mix" :key="mix.pk" >
    
                          <el-dropdown-item  @click="this.local_use.emissions=String(mix.emissions); saveEmissions()" > 
                            {{ mix.name }}
                          </el-dropdown-item>
    
                          </div>
                        </el-dropdown-menu>
                      </template>
                    </el-dropdown>
                    </template>
                    <template #append ><div style="font-size: 0.7em;">gCO2/kWh</div></template>
            </el-input>
        </template>
      </el-popover>
      </el-form-item>
      <div v-if="dialog" style="margin-left: auto; margin-right: auto;">
        <el-checkbox  v-model="local_data.is_server" label="servidor" size="large" />

      </div>
    </el-form>

  </div>



  <el-collapse v-model="activeNames">
    <el-collapse-item :title="getTitle()"  name="1" :disabled="!show_use">
      <div style="margin: 1em 7em 1em 7em;">
        <el-input
          v-model="local_data.description"
          type="textarea"
          autosize
          placeholder="Descripcción"
          resize="none"
          rows="2"
          :disabled="!dialog"
        />
  
      </div>
  <el-row :gutter="20">
    <el-col :span="12">
      <el-form
        label-width="150px"
        :model="local_data"
        style="max-width: 230px; text-align: left;"
        :disabled="!dialog"
      >
      <div  style="text-align: center; margin-top:30px;">
        <b>Fase de fabricación (KgCO2)</b>
      </div>
      <br>
      <el-form-item label="CFP Fabricación">
        <el-popover
          :visible="local_data.cfp_build_phase == null"
          placement="bottom"
          :width="220"
          content="Introduce un valor valido"
        >
          <template #reference>
            <el-input-number
              v-model="local_data.cfp_build_phase" 
              :precision="2" 
              :step="0.1" 
              :max="1000" 
              :controls="false" 
              />
          </template>
        </el-popover>

          <!-- <el-input-number
            class="input-right"
            style="width: 10px;"
            v-model="local_data.cfp_build_phase" 
            :precision="2" 
            :step="0.1" 
            :max="1000" 
            
            :controls="false" 
          /> -->

      </el-form-item>
      <el-form-item label="Desviación">
        <el-popover
          :visible="local_data.cfp_deviation_standard == null"
          placement="bottom"
          :width="220"
          content="Introduce un valor valido"
        >
          <template #reference>
            <el-input-number v-model="local_data.cfp_deviation_standard" :precision="2" :step="0.1" :max="1000" :controls="false" />
          </template>
        </el-popover>
      </el-form-item>
      <div  v-if="local_data.is_server" style="text-align: center; margin-top:30px;">
        <b>Aplicaciones alojadas</b>
        <br>
        <el-popover
          :visible="local_data.hosted_apps == null"
          placement="bottom"
          :width="220"
          content="Introduce un valor valido"
        >
          <template #reference>
            <el-input-number v-model="local_data.hosted_apps" :min="0" :max="50" :controls="true" />
          </template>
        </el-popover>
      </div>
    </el-form>
    </el-col>
    <el-col :span="12">
      <el-form
        label-width="150px"
        :model="local_data"
        
        :disabled="!dialog"
      >
      <div  style="text-align: center; margin-top:30px;">
        <b>Fase de uso (W)</b> <br><br>
      </div>
    
      <el-form-item label="Caso medio">
        <el-popover
          :visible="local_data.middle_case == null"
          placement="bottom"
          :width="220"
          content="Introduce un valor valido"
        >
          <template #reference>
            <el-input-number v-model="local_data.middle_case" :precision="2" :step="0.1" :max="1000" :controls="false" />
          </template>
        </el-popover>
      </el-form-item>
    
      <el-form-item label="Caso pesimo">
        <el-popover
          :visible="local_data.worst_case == null"
          placement="bottom"
          :width="220"
          content="Introduce un valor valido"
        >
          <template #reference>
            <el-input-number v-model="local_data.worst_case" :precision="2" :step="0.1" :max="1000" :controls="false" />
          </template>
        </el-popover>
      </el-form-item>
    
      <el-form-item label="Caso optimo">
        <el-popover
          :visible="local_data.best_case == null"
          placement="bottom"
          :width="220"
          content="Introduce un valor valido"
        >
          <template #reference>
            <el-input-number v-model="local_data.best_case" :precision="2" :step="0.1" :max="1000" :controls="false" />
          </template>
        </el-popover>
      </el-form-item>
    </el-form>
    </el-col>
  </el-row>
</el-collapse-item>
    </el-collapse>

  <div  class="dialog-footer" v-if="dialog">
    <el-button @click="$emit('close')" plain>Cancelar</el-button>
    <el-button color="#7cd4ac" @click="$emit('save', local_data)" plain>
      Guardar
    </el-button>
  </div>
</template>
  



<script>

import { useComponentsData } from "@/stores/ComponentsData"

  export default {
    name: "ComponentData",
    props: ["data", "dialog", "use", "show_use"],
    emits: ["saveUse", "save", "close"],
    watch: {
      data() {
        console.log("watch")
        this.local_data = JSON.parse(JSON.stringify(this.data));
        this.local_use = JSON.parse(JSON.stringify(this.use));
      },
    },
    setup(){
    const store = useComponentsData();
    return {
      store: store,
    }

  },
    data() {
      return {
        local_data: JSON.parse(JSON.stringify(this.data)),
        local_use: JSON.parse(JSON.stringify(this.use)),
        old_hours: 0,
        old_emissions: null,
        activeNames: [],
      }
    },
    methods: {
      handleInput() {
        // if (isNaN(value)) {
        //   this.local_use.emissions = 0;
        // }
        this.local_use.emissions = this.local_use.emissions.replace(/[^0-9]/g, "");

      // Si el valor no es numérico, no se actualizará myNumber y el campo seguirá siendo null
      },
      getTitle(){
        return this.show_use ? "más información" : ""
      },
      saveHours(){
        // si se ha modificado el campo lo enviamos
        if(this.local_data.is_server){
          if(this.old_hours != this.local_use.server_years){
            this.$emit('saveUse', this.local_use)
          }
        }
        else{
          if(this.old_hours != this.local_use.hours)
            this.$emit('saveUse', this.local_use)
        }
      },
      saveEmissions(){
        // si se ha modificado el campo lo enviamos
        if(this.old_emissions != this.local_use.emissions){
          this.$emit('saveUse', this.local_use)
        }
      }

    },
    created()
      {
        // si está en modo dialogo abrimos el primer y unico collapse
        this.local_use.emissions = String(this.local_use.emissions);
        if (!this.show_use)
          this.activeNames = ['1'];
      }
  }
</script>


<style>

el-popover{
  font-family: "Times New Roman", Times, serif!;
}
.code-container{
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
}
.code-block{
  flex: 1;
  width: 50%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}

.input-left{
  width: 5em
}
.input-left .el-input__wrapper{
  border-radius: 0.4em 0em 0em 0.4em;
  width: 5em;
}

.input-right .el-input__wrapper{
  border-radius: 0em 0.4em 0.4em 0em;
}
</style>


  