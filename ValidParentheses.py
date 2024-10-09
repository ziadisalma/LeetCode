class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>();
        Stack<Character> stack = new Stack<>();
        Stack<Character> stack2 = new Stack<>();

        map.put(')','(');
        map.put(']','[');
        map.put('}','{');
        if (s.length() % 2 != 0){
                return false;
            }
        for(char c: s.toCharArray()){
            
            if (map.containsValue(c)){
                stack.push(c);
            }
            else if (map.containsKey(c)){
                if(stack.isEmpty() || stack.pop()!= map.get(c)){
                    return false;
                }
                stack2.push(c);
            }
          
            
        }
        if (stack2.size()!= s.length()/2){
                return false;
            }  
        return true;
    }
}