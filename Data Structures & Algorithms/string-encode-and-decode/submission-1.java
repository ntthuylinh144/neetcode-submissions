

public class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();

        for (String s : strs) {
            sb.append(s.length());
            sb.append('#');
            sb.append(s);
        }

        return sb.toString();
    }

    public List<String> decode(String encoded) {
        List<String> result = new ArrayList<>();

        int i = 0;

        while (i < encoded.length()) {

            // 1. Find '#'
            int j = i;

            while (encoded.charAt(j) != '#') {
                j++;
            }

            // 2. Get length
            int length = Integer.parseInt(encoded.substring(i, j));

            // 3. Get string
            String s = encoded.substring(j + 1, j + 1 + length);

            result.add(s);

            // 4. Move to next encoded string
            i = j + 1 + length;
        }

        return result;
    }
}
