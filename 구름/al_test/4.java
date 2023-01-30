public static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args)
    {   //프로그램의 시작부 
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        
        // 패스워드 패턴 입력받아 비교할 수 있게 쪼개어 놓기
        String word = scanner.next();
        List<String> word_lst = new ArrayList<String>();
        String[] splitWord = word.split("");
        for(int i=0; i<splitWord.length;i++){
            word_lst.add(splitWord[i]);
        }
        
        // 후보키 저장
        String[] candidate = new String[M];
        for(int i=0; i<M; i++){
            candidate[i] = scanner.next();
        }
        
        // 사전순이므로 정렬
        Arrays.sort(candidate);
        // 결과 값 저장 변수
        String result1 = new String();
        
        // 1. 후보 암호 개수만큼 반복한다.
        for(int i=0; i<M; i++){
            List<String> cdd_word_lst = new ArrayList<String>();
            String[] cdd_word = candidate[i].split("");
            for(int j=0; i<cdd_word.length;j++){
                cdd_word_lst.add(candidate[j]);
            }
            // 후보 암호와 패턴이 일치하는지 아닌지 판단 여부 변수
            boolean flag = true;
            
            for(int j=0; j<cdd_word_lst.length; j++){
                // 2. 패턴이 일차하면 진행, 아니면 flag를 false로 하고 반복문 탈출
                if(flag){
                    if(word_lst[j] == cdd_word_lst[j] || word_lst[j] == "?"){
                        continue;
                    }
                } else{
                    flag = false;
                    break;
                }
            }
            
            // 3. 암호 후보랑 패턴이 끝까지 일치한다면 결과에 저장, 전체 패턴에서 암호 후보 길이만큼 제거
            if(flag){
                result1 += cdd_word[i];
                for (int j=0; j<cdd_word_lst.length; j++){
                    word_lst.remove(j);
                }
            }
        }
        // 4. 결과 값 출력
        System.out.println(result1);
    }