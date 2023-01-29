BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// 단어의 개수 n 입력
int N = Integer.parseInt(br.readLine());

// N줄의 영단어 입력 받기 위한 변수
String[] array = new String[N];
// 영어 모음
char vowels[] = {'a', 'e', 'i', 'o', 'u'};


// array에 번호 입력받기
for(int i=0; i<N; i++){
    array[i] = br.readLine();
}

// 영단어가 모음인지 아닌지 확인 변수
boolean flag = false;

// 시작
for(int i=0; i<N; i++){
    // i번째 영단어 배열로 나누기
    String word = array[i];
    char[] word_arr = word.toCharArray();
    // 영단어가 바뀌면 flag초기화
    flag = false;
    
    // 결과 값 변수
    String result = "";
    // 연속된 영어 모음 개수
    int cnt = 0;
    
    // i번째 영단어 새로운 단어로 만들기
    for(int j=0; j<word_arr.length; j++){
        // 영어 모음 반복문
        for(int k=0; k<5; k++){
            // 모음이면 flag를 참으로
            if(word_arr[j] == vowels[k]){
                flag = true;
                
            }
        }
        
        // 영어 모음이면 카운트 증가, 아니면 카운트 0으로 초기화
        if(flag){
            cnt++;
        } else {
            cnt = 0;
        }
        // 카운트가 1보다 작거나 같으면 모음이 아니거나 첫 번째 모음이기 때문에 결과에 추가
        if(cnt<=1){
            result += word_arr[j];
        }
        // 다음 단어를 보기 전 flag를 false로 초기화
        flag = false;
    }
    // 결과 값 출력
    System.out.println(result);
}