import { defineStore } from "pinia"

export const useNoAuthID = defineStore("NoAuthID", {

    state: () => ({
        calculation: 1,
        use: 1,
        component: 1,
    }),

})