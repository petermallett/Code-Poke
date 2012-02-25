
import java.io.Console;

class JavaPoke {
	public static void main(String[] args) {
		Console c = System.console();
		if (c == null) {
			System.err.println("No console.");
			System.exit(1);
		}

		String inputStr = c.readLine("Enter the number of items, followed by each item on its own line: ");

		int numItems = 0;
		try {
			numItems = Integer.parseInt(inputStr);
		}
		catch (NumberFormatException e) {
			System.err.println("Number of items input was not numeric " + e.getMessage());
			System.exit(1);
		}

		Activity[] activities = new Activity[numItems];

		for (int x = 0; x < numItems; x++) {
			inputStr = c.readLine();
			inputStr = inputStr.trim();
			String[] parts = inputStr.split(" ");
			if (parts.length != 2) {
				System.out.println("Parse error: input lines must be in the form of '[name] [number]'. Encountered: '" + inputStr + "'");
				System.exit(1);
			}
			else {
				int value = 0;
				try {
					value = Integer.parseInt(parts[1]);
				}
				catch (NumberFormatException e) {
					System.err.println("Second part of input line must be a numeric caloric value.");
					System.exit(1);
				}
				
				activities[x] = new Activity(parts[0], value);
			}
		}

		//input complete, compute sums until a solution is found
		for (int x = 0; x < Math.pow(2, numItems); x++) {
			int sum = 0;
			int count = 0;
			String[] tempList = new String[numItems];

			for (int y = 0; y < numItems; y++) {
				int binMask = (int)Math.pow(2, y);
				if ((binMask & x) != 0) {
					sum += activities[y].value;
					tempList[count] = activities[y].name;
					count += 1;

					if (sum == 0 && y != 0) {
						System.out.println("Solution: \n");
						for (int z = 0; z < count; z++) {
							System.out.println(tempList[z]);
						}
						System.exit(0);
					}
				}

			}
		}
	}
}

class Activity {
	public String name;
	public int value;

	public Activity(String name, int value) {
		this.name = name;
		this.value = value;
	}
}

/*
12
free-lunch 802
mixed-nuts 421
orange-juice 143
heavy-ddr-session -302
cheese-snacks 137
cookies 316
mexican-coke 150
dropballers-basketball -611
coding-six-hours -466
riding-scooter -42
rock-band -195
playing-drums -295
*/
