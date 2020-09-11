// 카카오 2020인턴십
package programmers.level1;

class 키패드누르기 {
    public  String solution(int [] numbers, String hand) {
        StringBuilder sb = new StringBuilder();

        int pl = 10;
        int pr = 12;

        for(int num : numbers) {
            if(num ==1 || num == 4 || num == 7) {
                sb.append("L");
                pl = num;
            }else if(num == 3 || num == 6 || num == 9) {
                sb.append("R");
                pr = num;
            }else {
                int distanceL = distance(pl, num);
                int distanceR = distance(pr, num);

                if(distanceL > distanceR) {
                    sb.append("R");
                    pr = num;
                }else if(distanceL < distanceR) {
                    sb.append("L");
                    pl = num;
                }else {
                    if(hand.equals("right")) {
                        sb.append("R");
                        pr = num;
                    }else {
                        sb.append("L");
                        pl = num;
                    }
                }

            }
        }
        return sb.toString();
    }

    public static int distance(int dst, int num) {

        if(num == 0) {
            num = 11;
        }

        if(dst == 0) {
            dst = 11;
        }

        int x0 = (dst-1) / 3;
        int y0 = (dst-1) % 3;

        int x1 = (num-1) / 3;
        int y1 = (num-1) % 3;

        return Math.abs(x0-x1) + Math.abs(y0 - y1);

    }
}
