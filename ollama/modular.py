import csv

# Comma-separated values
csv_data = """Question,Answer
What is the purpose of the Maharashtra Land Revenue Code (Second Amendment) Act, 2007?,The purpose of the act is to revive the Maharashtra Revenue Tribunal.
What does the act amend?,The act amends the Maharashtra Land Revenue Code.
What happens to the reference to the Maharashtra Revenue Tribunal in enactments specified in the Schedule to this Act?,The reference shall be referred to as the Maharashtra Revenue Tribunal.
What happens to the reference to the Maharashtra Revenue Tribunal in rules, regulations, bye-laws, notifications, orders issued under any of these enactments or other enactments?,The reference shall be referred to as the Maharashtra Revenue Tribunal.
What instrument was previously referred to as the Divisional Commissioner by virtue of the provisions of section 14 of the Maharashtra Land Revenue Code (Amendment) Act, 2002?,Any instrument that was to be construed as the Divisional Commissioner.
What will the reference now be referred to as?,The Maharashtra Revenue Tribunal."""

# Split the CSV data into rows
rows = [line.split(" , ", 1) if line else ["", ""] for line in csv_data.split("\n")]

# Write the CSV data to a file
output_file = "question_answer_pairs.csv"
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(rows)

print("CSV file has been created successfully:", output_file)
