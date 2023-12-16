const express = require('express');
const socketIO = require('socket.io');
const zod = require('zod');

const app = express();
app.use(express.static('public'))

const PORT = 3000

app.get("/healthcheck", (_, res) => {
	res.send({status: 'healthy'});
});

const server = app.listen(PORT, () => console.log(`Server Started at ${PORT}`));

const io = socketIO(server);

const schema = zod.object({
	user_id: zod.string(),
	to_id: zod.string(),
	date: zod.date(),
	message: zod.string(),
})

io.on("connection", (socket) => {

	let userId = socket.id;

	console.log(`User ${socket.id} is connected`);

	socket.on('message', (data) => {
		// schema.safeParse(data)
		// io.emit('message',data);
		console.log(data);
	});

	socket.on('disconnect', () => console.log(`Bye ${userId}`));
});

