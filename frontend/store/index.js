export const state = () => ({
    prediction: "",
    image: ""
})

export const mutations = {
    addimage(state, image){
        state.image = image
    },
    add(state, response){
        state.prediction = response
    }
}

