const express = require('express'); // express모듈을 찾아 포함 //
const app = express(); // express객체생성 //
const port = 8000; // 포트 지정, 식별자역할 //

app.use('/static', express.static(__dirname + '/static')); // 참고하는 외부파일을 /static로 설정, express는 현재경로 //

app.listen(port, () => { // listen()함수 실행, HTTP요청 대기 //
    console.log('Connected to 8000 port.');
});

app.get('/', (req, res) => { // /에 접근시 수행할 작업 기술 //
    let options = {
        root: __dirname
    };
    res.sendFile('templates/index.html', options); // 프런트엔드 index.html을 전달 //
});

app.get('/api/message/get', (req,res) => { // /api/message/get에 요청들어오면 Hello, World!출력 //
    res.send('Hello, World!');
});