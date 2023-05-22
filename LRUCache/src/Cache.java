import java.util.ArrayList;
import java.util.List;

public class Cache {
    private List<String> keyList;
    private List<String> valueList;
    private Integer capacity;

    public Cache(Integer capacity) {
        keyList = new ArrayList<>(capacity);
        valueList = new ArrayList<>(capacity);
        this.capacity = capacity;
    }


    public void set(String key, String value) {
        if (!keyList.contains(key) && !keyList.contains(value) && keyList.size() != capacity) {
            keyList.add(0, key);
            valueList.add(0, value);
        } else if (!keyList.contains(key) && !keyList.contains(value) && keyList.size() == capacity) {
            int lastIndex = keyList.size() -1;
            keyList.remove(lastIndex);
            valueList.remove(lastIndex);
            keyList.add(0, key);
            valueList.add(0, value);
        }
    }

    public String get(String key) {
        String value = "";
        int index = keyList.indexOf(key);

        if (keyList.contains(key)) {
            value = valueList.get(index);

            keyList.remove(index);
            valueList.remove(index);
            keyList.add(0, key);
            valueList.add(0, value);
        }

        return value;
    }

    public void rem(String key) {
        if (keyList.contains(key)) {
            int index = keyList.indexOf(key);
            keyList.remove(index);
            valueList.remove(index);
        }
    }
    
//    public void getAll() {
//
//        for (int i = 0; i < keyList.size(); i++) {
//            System.out.println(keyList.get(i) + " " + valueList.get(i));
//        }
//
//        System.out.println();
//    }
}
