import java.util.LinkedHashMap;
import java.util.Map;

public class LRUCache {
    LinkedHashMap<String, String> cacheMap;

    public LRUCache(Integer capacity) {
        cacheMap = new LinkedHashMap<>(capacity);
    }

    public void set(String key, String value) {
        if (!cacheMap.containsKey(key)) {
            cacheMap.put(key, value);
        }
    }

    public String get(String key) {
        String value = "";

        if (cacheMap.containsKey(key)) {
            value = cacheMap.get(key);

            LinkedHashMap<String, String> newMap = (LinkedHashMap<String, String>) cacheMap.clone();
            cacheMap.clear();
            cacheMap.put(key, value);
            cacheMap.putAll(newMap);
        }

        return value;
    }

    public void rem(String key) {
        if (cacheMap.containsKey(key)) {
            cacheMap.remove(key);
        }
    }

    public void getAll() {
        for (Map.Entry<String, String> stringStringEntry : cacheMap.entrySet()) {
            System.out.println(stringStringEntry.getKey() + " : " + stringStringEntry.getValue() );
        }
        System.out.println();
    }

    public static void main(String[] args) {
        LRUCache lru = new LRUCache(10);
        lru.set("Jesse", "Pinkman");
        lru.set("Walter", "White");
        lru.set("Jessee", "James");

        lru.getAll();

        System.out.println("Get Jessee: " + lru.get("Jessee") + "\n");

        lru.getAll();

        lru.rem("Walter");

        System.out.println("Get Walter: " + lru.get("Walter") + "\n");

        lru.getAll();
    }
}
