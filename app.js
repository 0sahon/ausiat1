const http = require('http');
const { parse } = require('querystring');

const server = http.createServer((req, res) => {
    if (req.method === 'POST') {
        collectRequestData(req, result => {
            console.log(result);
            res.end(`Parsed data belonging to ${result.message}`);
        });
    } else {
        res.end(`
        <!doctype html>
        <html>
        
        <body>
            <form action="/" method="POST">
                <label for="message" name="message">Message: </label><br>
                <textarea name="YourMessage" id="" cols="30" rows="08"></textarea> <br>
                <button type="submit" name = "submit">Submit</button>
        
            </form>
        </body>
        
        </html>
        `);
    }
});
server.listen(3000);

function collectRequestData(request, callback) {
    const FORM_URLENCODED = 'application/x-www-form-urlencoded';
    if (request.headers['content-type'] === FORM_URLENCODED) {
        let body = '';
        request.on('data', chunk => {
            body += chunk.toString();
        });
        request.on('end', () => {
            callback(parse(body));
        });
    } else {
        callback(null);
    }
}