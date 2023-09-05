<template>

<div class="grid-container">
        <div v-for="(component, index) in local_data" :key="component.pk" >
          <el-card class="box-card" :class="{ 'box-card-selected': selected[index] != 0 && state.add_use}">
            <div class="box-content">
              <span class="name">{{ component.name }}</span>
              <el-popover placement="bottom" :width="550" trigger="click">
                <template #reference>
                  <el-button class="button" text>
                    <font-awesome-icon icon="fa-solid fa-circle-info" size="lg" />
                  </el-button>
                </template>
                <ComponentData 
                :data="component"
                :use="[]" 
                :dialog="false"
                :show_use="false"
                />
              </el-popover>
              <div v-if="state.add_use">
                <el-button v-if="selected[index] == 0" class="button" @click="toggleSelected(index, 1, true)" text>
                   +
                </el-button>
                <el-input-number
                  v-else
                  v-model="local_selected[index]"
                  style="width: 4em;"
                  :min="0"
                  :max="10"
                  controls-position="right"
                  size="small"
                  @change="toggleSelected(index, local_selected[index], false)"
                />
              </div>
              <el-dropdown v-else>
                  <el-button class="button" text>
                   ⚙️
                  </el-button>
                  <template #dropdown>
                    <el-dropdown-menu v-if="system">
                      <el-dropdown-item @click="editComponent" disabled>Editar</el-dropdown-item>
                      <el-dropdown-item @click="duplicateComponent(index)">Duplicar</el-dropdown-item>
                      <el-dropdown-item @click="deleteComponent" divided disabled>Eliminar</el-dropdown-item>
                    </el-dropdown-menu>
                    <el-dropdown-menu v-else>
                      <el-dropdown-item @click="editComponent(index)">Editar</el-dropdown-item>
                      <el-dropdown-item @click="duplicateComponent(index)">Duplicar</el-dropdown-item>
                      <el-dropdown-item @click="deleteComponent(index)" divided>Eliminar</el-dropdown-item>
                    </el-dropdown-menu>
                  </template>
                </el-dropdown>
            </div>
          </el-card>
        </div>
      </div>
</template>
  

<script>

import { useState } from "@/stores/State"

import ComponentData from "@/components/ComponentData.vue"
  export default {
    name: "ComponentGroup",
    components: {
      ComponentData,
    },
    props: ["data2","components","system", "type", "selected"],
    setup(){
    const state = useState();
    return {
      state: state
    }
  },
    data() {
      return {
        local_selected: [... this.selected],
        local_data: this.data2,
      }
    },
    emits: ["duplicate", "edit", "delete", "toggleSelect"],
    // setup(props, ctx) {
    //    ctx.emit()
    // },
    methods:{
      duplicateComponent(index){  
        this.$emit('duplicate', index, this.system)
      },
      editComponent(index){  
        this.$emit('edit', index)
      },
      deleteComponent(index){  
        this.$emit('delete', index)
      },
      toggleSelected(index, value, new_use){
        // console.log(index)
        // this.local_selected[index] = !this.local_selected[index]
        this.local_selected[index] += (new_use ? 1 : 0);
        this.$emit('toggleSelect', index, value, this.system)
      }
    },
    created(){
      // for (const i in this.selected){
      //   this.local_selected.push(this.selected[i])
      
    }
    
  }
</script>


<style>

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 15em  !important;
  margin-bottom: 20px;
}

.box-card-selected {
  outline: 2.5px solid #76ba9d !important;
}



.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);;
  padding-left: 1px;
  padding-right: 1px;
  grid-auto-flow: dense;

}

.box-content {
  display: flex; 
  justify-content: space-between;
}

.el-card .el-card__body{
  padding: 0.4em;
  padding-left: 0.7em;
}

.button {
  padding: 8px !important;
}


.name {
    padding-top: 0.5em;
    flex: 1;
    font-size: 0.9em;
    white-space: nowrap !important; /* Evita el salto de línea */
    overflow: hidden !important; /* Oculta el texto que no cabe en el contenedor */
    text-overflow: ellipsis !important; /* Muestra tres puntos suspensivos (...) al final del texto cortado */
  }

</style>


  