public static Scanner scanner = new Scanner(System.in);

public static void main(String[] args)
{   //프로그램의 시작부 
        int N = scanner.nextInt();
        int M = scanner.nextInt();
    
        // 결과 값을 저장할 ArrayList 
        List<Integer> result = new ArrayList<Integer>();
        
        String word = scanner.next();
        char[] word_arr = word.toCharArray();
        
        String[] cdd = new String[M];
        
        for(int i=0; i<M; i++){
            cdd[i] = scanner.next();
        }
        
        cdd.sort();
        
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                char[] cdd_word = cdd[j].toCharArray();
            }
        }
        
}