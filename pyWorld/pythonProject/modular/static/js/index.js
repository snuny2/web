function getMessage() { // 데이터를 요청하는 getMessage()로 구성 //
    // fetch() 함수는 서버로 요청을 보내기 위한 함수, 서버주소와 요청내용을 입력받음 //
    let message = fetch('/api/message/get').then(response => {
        return response.text();
    }).catch(error => { // 오류발생시 실행되는 내용, 콘솔창에서 보여줌 //
        console.log('[Error]fetch.api.message.get:', error);
    });

    return message; // 응답도착시 내용 반환 //
}