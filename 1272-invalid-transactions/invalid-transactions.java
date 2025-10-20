import java.util.*;

class Solution {
    public List<String> invalidTransactions(String[] transactions) {
        // Step 1: Parse transactions into objects
        List<Transaction> list = new ArrayList<>();
        int y =-1;
        for (String t : transactions) {
            String[] parts = t.split(",");
            String name = parts[0];
            int time = Integer.parseInt(parts[1]);
            int amount = Integer.parseInt(parts[2]);
            String city = parts[3];
            y++;
            list.add(new Transaction(name, time, amount, city,y, t));
        }

        // Step 2: Check invalid transactions
        Set<Integer> invalid = new HashSet<>();

        for (int i = 0; i < list.size(); i++) {
            Transaction t1 = list.get(i);
            
            // Rule 1: amount > 1000
            if (t1.amount > 1000) {
                invalid.add(t1.index);
            }

            // Rule 2: within 60 mins with same name but different city
            for (int j = i + 1; j < list.size(); j++) {
                Transaction t2 = list.get(j);
                if (t1.name.equals(t2.name)
                        && Math.abs(t1.time - t2.time) <= 60
                        && !t1.city.equals(t2.city)) {
                    invalid.add(t1.index);
                    invalid.add(t2.index);
                }
            }
        }

        ArrayList<Integer> idx = new ArrayList<Integer>(invalid);
        System.out.println(idx);
        ArrayList result = new ArrayList<>();

        for (int id : idx){
            result.add(transactions[id]);
        }

        return result;
    }

    // Helper class
    static class Transaction {
        String name;
        int time;
        int amount;
        String city;
        String original;
        int index;

        Transaction(String name, int time, int amount, String city, int y ,String original) {
            this.name = name;
            this.time = time;
            this.amount = amount;
            this.city = city;
            this.original = original;
            this.index = y;
        }
    }
}
