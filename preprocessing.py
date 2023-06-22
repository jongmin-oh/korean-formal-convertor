import pandas as pd


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    return lines


informal1 = read_file("./data/수동테깅_병렬데이터/dev.ban.txt")
informal2 = read_file("./data/수동테깅_병렬데이터/test.ban.txt")
informal3 = read_file("./data/수동테깅_병렬데이터/train_ext.ban.txt")
formal1 = read_file("./data/수동테깅_병렬데이터/dev.yo.txt")
formal2 = read_file("./data/수동테깅_병렬데이터/test.yo.txt")
formal3 = read_file("./data/수동테깅_병렬데이터/train_ext.yo.txt")

print(len(informal1) == len(formal1))
print(len(informal2) == len(formal2))
print(len(informal3) == len(formal3))

# Create a DataFrame for parallel data
parallel_df = pd.DataFrame(
    {
        "informal": informal1 + informal2 + informal3,
        "formal": formal1 + formal2 + formal3,
    }
)

# Load KETI conversation corpus data
keti_df = pd.read_excel("./data/ADC KETI 대화코퍼스 전체.xlsx", usecols=["반말", "해요체"])
keti_df = keti_df.rename(columns={"반말": "informal", "해요체": "formal"})

# Load SmileStyle dataset
smile_df = pd.read_csv(
    "./data/smilestyle_dataset.tsv", sep="\t", usecols=["informal", "formal"]
)

# Concatenate all data
df = pd.concat([parallel_df, keti_df, smile_df], ignore_index=True)

# Drop missing values and duplicates
df = df.dropna().drop_duplicates(subset=["informal"]).reset_index(drop=True)

# Clean data by removing periods and commas
df["informal"] = df["informal"].str.replace(".", "").str.replace(",", "")
df["formal"] = df["formal"].str.replace(".", "").str.replace(",", "")

# Save the cleaned data to an Excel file
df.to_excel("./data/formal_convertor_train.xlsx")

print(f"Number of training examples after cleaning: {len(df)}")
