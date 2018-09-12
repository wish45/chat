
$(document).ready(function(){
	var roomName = {{ room_name }};
	console.log(roomName);
    var socket = new WebSocket('ws://127.0.0.1:8000/chat/'+roomName);
	//새 웹소켓 오브젝트를 생성하여 8000/chat서버에 접속,
	//var socket = new WebSocket('ws://127.0.0.1:8000/chat/);



    socket.onopen = websocket_conexion_ok;
	//onopen은 서버측에서 클라이언트와 웹 소켓 연결이 되었을대 호출되는 함수.
	socket.onmessage = websocket_msj_recibido;
	//onmessage는 클라이언트에서 서버측으로 메시지를 보내면 호출되는 함수.
	//메세지가 수신되면 메세지 이벤트가 onmessage함수로 전달된다.


	$('#formulario').submit(function(e){
		e.preventDefault();
		datos = {
			'nombre' : $('input[name="nombre"]').val(),
			'mensaje': $('input[name="texto"]').val()
		}
		socket.send(JSON.stringify(datos));
		//서버로 json 데이터를 전송함.
        //
		$('#formulario')[0].reset(); //채팅 텍스트필드 value를 모두 초기화함.
	});

});


function websocket_conexion_ok(){
	//alert('La conexión se ha establecido');
}



function websocket_msj_recibido(e){
    //alert("message sending...");
	datos = JSON.parse(e.data); //string에서 json타입으로 형변환.
	//alert(datos);  [object Object]
	//alert(e.data); {"nombre":"사용자 아이디","mensaje":"텍스트 내용"}

    if(datos.nombre== $('#name').val()){
	codigo = '<div class="col-12">'				+
				'<div class="nombre text-right">'				+
					'<h4>'+ datos.nombre +'</h4>'	+
				'</div>'							+
				'<div class="contenido text-right">'			+
					'<p>'+ datos.mensaje +'</p>'	+
				'</div>'							+
			'</div>';
	$('#conversacion').append(codigo);
	} else{
        codigo = '<div class="col-12 " >'				+
				'<div class="nombre">'				+
					'<h4>'+ datos.nombre +'</h4>'	+
				'</div>'							+
				'<div class="contenido">'			+
					'<p>'+ datos.mensaje +'</p>'	+
				'</div>'							+
			'</div>';
	$('#conversacion').append(codigo);
    }
}

//
// onmessage	EventListener	"message" 이름의 MessageEvent
// 이벤트가 발생하면 처리할 핸들러입니다.
// 이는 서버로부터 메세지가 도착했을 때 호출됩니다.
// onopen	EventListener	WebSocket 인터페이스의 연결상태가
// readyState 에서 OPEN으로 바뀌었을 때 호출되는 이벤트 리스너입니다. ;
// 연결 상태가 OPEN으로 바뀌었다는 말은 데이터를 주고 받을 준비가 되었다는 뜻입니다.
// 이 리스너가 처리하는 이벤트는 "open"이라는 이벤트 하나입니다.
