String id = scanner.next();
String pw1 = scanner.next();
String pw2 = scanner.next();

String result = "";
// id 패턴 정규식
String idPattern = "^[a-z0-9]{3,20}$";
// pw 패턴 정규식
String pwPatterrn = "^(?=.*?[a-zA-Z])(?=.*?[0-9])(?=.*?[#!@$]).{8,20}$";


// id, pw 패턴이 참이고 비밀번호와 비밀번호 확인이 같으면 pass
// 하나라도 아닐 시 fail 출력 후 종료
if(Pattern.matches(idPattern, id)){
    result = "pass";
} else {
    System.out.println("fail");
    return;
}
if(Pattern.matches(pwPatterrn, pw1)){
    result = "pass";
} else {
    System.out.println("fail");
    return;
}
if (pw1.equals(pw2)){
    result = "pass";
} else {
    System.out.println("fail");
    return;
}


// 결과 값 출력
System.out.println(result);