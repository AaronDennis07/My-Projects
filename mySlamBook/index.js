const express = require('express');
const app = express();
const mongoose = require('mongoose');
const User = require('./models/user');
const ejs = require('ejs');
const path = require('path');
const session = require('express-session');
const method_override = require('method-override');
const cookie_parser = require('cookie-parser');
const asyncHandler = require('./utils/asyncHandler');
const flash = require('express-flash');
const helmet = require('helmet');

const scriptSrcUrls = [
    "https://code.jquery.com/jquery-3.6.0.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.js",
    "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js",
    "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6813609620822362"
];

const styleUrls = [
    "https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.css",
    "https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css",
    "https://fonts.googleapis.com/css2?family=Lobster&display=swap",
]

const fontUrls = [
    "https://fonts.googleapis.com",
    "https://fonts.gstatic.com", 

]

app.use(express.urlencoded({extended: true}));
app.use(method_override('_method'));
app.set('view engine','ejs');
app.set('views',path.join('views'));
app.use(express.static('public'));
app.use(cookie_parser('mySecret'));
app.use(session({ cookie: { maxAge: 60000 } ,resave:true,saveUninitialized: true,secret: 'this website was written by aaron'}));
app.use(flash());
app.use((req, res, next) => {
    res.locals.created = req.flash('created');
    res.locals.submitted = req.flash('submitted');
    next();
})
app.use(helmet.contentSecurityPolicy({
    directives:{
    defaultSrc: [],
    connectSrc: ["self"],
    scriptSrc: ["'unsafe-inline'","'self'",...scriptSrcUrls],
    styleSrc: ["'self'","'unsafe-inline'",...styleUrls],
    workerSrc: ["'self'","blob:"],
    objectSrc: [],
    imgSrc: [
        "'self'",
        "blob:",
        "data:",
        "https://res.cloudinary.com/aaron07/"
    ],
    fontSrc: ["'self'",...fontUrls]
}}));
if(process.env.NODE_ENV !== 'production'){
    require('dotenv').config();
}
mongoose.connect(process.env.DB_URL || "mongodb://localhost:27017/userData")
.then(()=>{
    console.log('connected');
})
.catch((error)=>{
    console.log(error);
})



app.get('/',(req,res)=>{
    const {userID} = req.cookies;
    const {after} = req.query;
    
    if(userID){
       if(after){
        req.flash('submitted',`slam book successfully submitted`);
        res.redirect(`/index/${userID}`);   
       }
       else{
        res.redirect(`/index/${userID}`);
       }
    }
  
    else{

    res.render('pages/new');
    }
})



app.post('/',asyncHandler(async(req,res)=>{
    const expireTime = new Date(new Date().getTime() + (1000*60*60*24*40));
    const {name, questions} = req.body;
    const user = new User({name,questions});
    await user.save();
    res.cookie('userID',user.id,{expires: expireTime});
    req.flash('created','slam book successfully created');   
    res.redirect(`/index/${user.id}`);
}))


app.get('/show/:id/:num',asyncHandler(async(req,res)=>{
    const {id,num}  = req.params;
    const shareLink = `${req.protocol}://${req.hostname}/index/${id}`;
    const foundUser = await User.findById(id);
    const questions = foundUser.questions;
    const answers  = Object.values(foundUser.answers[num])[0];
    const name = Object.keys(foundUser.answers[num])[0];
    res.render('pages/show',{questions,answers,name,shareLink});
}))



app.get('/index/:id',asyncHandler(async(req,res)=>{
    const {id} = req.params; 
    const shareLink = `${req.protocol}://${req.hostname}/answer/${id}`;
    const user = await User.findById(id);
    const allEntries = user.answers.map(name=>(Object.keys(name)[0]));
    const count = allEntries.length;
    const name = user.name;

    res.render('pages/index',{allEntries,count,id,name,shareLink});
}))

app.patch('/answers',asyncHandler(async(req,res)=>{
    const {id,name, answers} = req.body;
    await User.findByIdAndUpdate(id,{$push:{answers:{[name]:answers}}});
    req.flash('submitted',`slam book successfully submitted`);
    res.redirect('/?after="true"');
}))

app.get('/answer/:id',asyncHandler(async(req,res)=>{
    const {id}  = req.params;
    if(req.cookies.userID === id){
        const userID = req.cookies.userID;
        res.redirect(`/index/${id}`);
        
    }
    else{
    const foundUser = await User.findById(id);
    res.render('pages/answers',{foundUser,id});
    }
}))

app.get('/error',(req,res,next)=>{
    try {
        throw new Error('BROKEN');
      } catch (err) {
        next(err);
      }
})

app.use((error, req, res, next) => {
    console.log(error);
    res.status(404).render('pages/error');
  })

app.get("*",(req,res)=>{
    res.send("404 not found");
})
port = process.env.PORT;
app.listen(port || 8000,()=>{
    console.log(`listening at port ${port }`);
})


