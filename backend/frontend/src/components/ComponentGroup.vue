<template>

<div class="grid-container">
        <div v-for="(component, index) in local_data" :key="component.pk" >
          <el-card class="box-card">
            <div class="box-content">
              <span class="name">{{ component.name }}</span>

              <el-popover placement="bottom" :width="550" trigger="hover">
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
                <el-dropdown>
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
          <br>     
        </div>

      </div>


</template>
  


<script>

import ComponentData from "@/components/ComponentData.vue"
  export default {
    name: "ComponentGroup",
    components: {
      ComponentData,
    },
    props: ["data","system"],
    watch: {
      data() {
        this.local_data = JSON.parse(JSON.stringify(this.data))
      },
    },
    emits: ["duplicate", "edit", "delete"],
    // setup(props, ctx) {
    //    ctx.emit()
    // },
    data() {
      return {
        local_data: JSON.parse(JSON.stringify(this.data))
      }
    },
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
  width: 240px;
  margin-bottom: 20px;
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
  }

</style>


  