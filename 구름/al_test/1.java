// N 입력
int N = scanner.nextInt();
// N줄의 번호 입력 받기 위한 변수
int[] array = new int[N];
// 결과 값을 저장할 ArrayList 
List<Integer> result = new ArrayList<Integer>();

// array에 번호 입력받기
for(int i=0; i<N; i++){
    array[i] = scanner.nextInt();
}
// 출력 시 오름차순 출력
Arrays.sort(array);

int cnt = 0;
// 최대 반복 수 1000 * 1000 이므로 실행 제한시간 2초 안에 실행 가능
for(int i=0; i<N; i++){
    cnt = 0;
    // array[i]의 숫자가 배열 안에 있을 시 카운트 증가
    for(int j=0; j<N; j++){
        if(array[i] == array[j]){
            cnt++;
        }
    }
    // 카운트가 1개이면 중복이 아니라는 말이므로 결과 List에 추가
    if(cnt==1){
        result.add(array[i]);
    }
}
// for문을 돌면서 결과 출력
for(int i=0; i<result.size(); i++){
    System.out.printf(result.get(i)+" ");
}