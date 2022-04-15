const mongoose = require('mongoose')
const {Schema} = mongoose

const userSchema = new Schema({

    name: String,
    questions: [String],
    answers: [Object]
    })
const userModel = mongoose.model('user',userSchema);
module.exports =  userModel