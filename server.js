const express = require("express")
const app = express()

const port = "49082"
const host = "localhost"

app.use(express.urlencoded({ extended: true }))
app.use(express.json())
app.use(express.static("public"))


app.listen(port)
