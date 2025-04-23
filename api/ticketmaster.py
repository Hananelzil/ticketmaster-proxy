const https = require("https");

module.exports = async (req, res) => {
  const agent = new https.Agent({
    rejectUnauthorized: false,
  });

  const options = {
    hostname: "www.ticketmaster.co.il",
    path: "/wbtxapi/api/v1/bxcached/event/getAllTopEvent/iw",
    method: "GET",
    agent,
  };

  const request = https.request(options, (response) => {
    let data = "";

    response.on("data", (chunk) => (data += chunk));
    response.on("end", () => {
      try {
        const json = JSON.parse(data);
        res.status(200).json(json);
      } catch (e) {
        res.status(500).json({ error: "Invalid JSON from Ticketmaster" });
      }
    });
  });

  request.on("error", (error) => {
    res.status(500).json({ error: error.message });
  });

  request.end();
};

