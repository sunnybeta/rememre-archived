const express = require('express');

const app = express();
const PORT = 3002

app.get("/_internal_/healthcheck", (_, res) => {
	res.send({status: 'healthy'})
});

app.listen(PORT, () => console.log(`Server Started at ${PORT}`));
