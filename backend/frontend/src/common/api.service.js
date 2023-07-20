const axios = require("axios");

axios.default.xsrfCookieName = "csrftoken";
axios.default.xsrfHeaderName = "X-CSRFTOKEN";

export { axios };