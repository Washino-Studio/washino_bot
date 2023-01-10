//----------Main.js for Washino Bot----------//





//-----Library-----//

const Discord = require("discord.js")
const intents = new Discord.IntentsBitField(3276799)
const bot = new Discord.Client({intents})
const token = process.env.token
const loadCommands = require("./Loaders/loadCommands")
const loadEvents = require("./Loaders/loadEvents")
const config = require("./config")
const loadSlashCommands = require("./Loaders/loadSlashCommands")



//----Variables----//

bot.commands = new Discord.Collection()

//--Import--//
loadCommands(bot)
loadEvents(bot)
loadSlashCommands(bot)


bot.login(token)
