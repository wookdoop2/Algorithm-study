package programmers.level1;

public class 완주하지못한선수 {
    public static String solution(String[] participant, String[] completion) {
        String answer = "";
        for(int i = 0; i < participant.length; i++) {
            for(int j = 0; j < completion.length; j++) {
                if(participant[i].equals(completion[j])) {
                    System.out.println(participant[i]);
                }
            }
        }
        return answer;
    }
}
