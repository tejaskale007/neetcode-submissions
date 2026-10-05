class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map <String , List<String>> solveProblem =new HashMap<>();
        for(int i = 0 ; i<strs.length ; i++){
        String temp = strs[i];
         char[] charArray = temp.toCharArray();
        Arrays.sort(charArray);
        String sortedString = new String(charArray);
        solveProblem.computeIfAbsent(sortedString, k -> new ArrayList<>()).add(strs[i]);

        
        }
       List<String> allValues = solveProblem.values().stream()
                                    .flatMap(List::stream)
                                    .toList();
      return solveProblem.values().stream().toList();                            
    }
}
