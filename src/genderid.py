
import pandas as pd
import openai
from tqdm import tqdm

# input the file name
print(
    "Input CSV file name (make sure that your terminal is in the same directory as the file, otherwise you can input the file path as well)"
)
file_name = input("> ")

# upload the csv file
df = pd.read_csv(file_name)
print("File correctly uploaded!")
df.head()

# input column name to be checked
print("Input the name column that needs to be check")
column_name = input("> ")

# input API key for Openai
print("Input your OpenAI API key: ")
key = input("> ")

# upload OpenAI model
model = "gpt-3.5-turbo"
openai.api_key = key

# transform the column name into list to be iterated
name_list = df[column_name].to_list()

# change model prompt based on nationality

NATIONALITIES = [
    "Afghan",
    "Albanian",
    "Algerian",
    "American",
    "Andorran",
    "Angolan",
    "Antiguans",
    "Argentinean",
    "Armenian",
    "Australian",
    "Austrian",
    "Azerbaijani",
    "Bahamian",
    "Bahraini",
    "Bangladeshi",
    "Barbadian",
    "Barbudans",
    "Batswana",
    "Belarusian",
    "Belgian",
    "Belizean",
    "Beninese",
    "Bhutanese",
    "Bolivian",
    "Bosnian",
    "Brazilian",
    "British",
    "Bruneian",
    "Bulgarian",
    "Burkinabe",
    "Burmese",
    "Burundian",
    "Cambodian",
    "Cameroonian",
    "Canadian",
    "Cape Verdean",
    "Central African",
    "Chadian",
    "Chilean",
    "Chinese",
    "Colombian",
    "Comoran",
    "Congolese",
    "Costa Rican",
    "Croatian",
    "Cuban",
    "Cypriot",
    "Czech",
    "Danish",
    "Djibouti",
    "Dominican",
    "Dutch",
    "Dutchman",
    "Dutchwoman",
    "East Timorese",
    "Ecuadorean",
    "Egyptian",
    "Emirian",
    "Equatorial Guinean",
    "Eritrean",
    "Estonian",
    "Ethiopian",
    "Fijian",
    "Filipino",
    "Finnish",
    "French",
    "Gabonese",
    "Gambian",
    "Georgian",
    "German",
    "Ghanaian",
    "Greek",
    "Grenadian",
    "Guatemalan",
    "Guinea-Bissauan",
    "Guinean",
    "Guyanese",
    "Haitian",
    "Herzegovinian",
    "Honduran",
    "Hungarian",
    "I-Kiribati",
    "Icelander",
    "Indian",
    "Indonesian",
    "Iranian",
    "Iraqi",
    "Irish",
    "Israeli",
    "Italian",
    "Ivorian",
    "Jamaican",
    "Japanese",
    "Jordanian",
    "Kazakhstani",
    "Kenyan",
    "Kittian and Nevisian",
    "Kuwaiti",
    "Kyrgyz",
    "Laotian",
    "Latvian",
    "Lebanese",
    "Liberian",
    "Libyan",
    "Liechtensteiner",
    "Lithuanian",
    "Luxembourger",
    "Macedonian",
    "Malagasy",
    "Malawian",
    "Malaysian",
    "Maldivan",
    "Malian",
    "Maltese",
    "Marshallese",
    "Mauritanian",
    "Mauritian",
    "Mexican",
    "Micronesian",
    "Moldovan",
    "Monacan",
    "Mongolian",
    "Moroccan",
    "Mosotho",
    "Motswana",
    "Mozambican",
    "Namibian",
    "Nauruan",
    "Nepalese",
    "Netherlander",
    "New Zealander",
    "Ni-Vanuatu",
    "Nicaraguan",
    "Nigerian",
    "Nigerien",
    "North Korean",
    "Northern Irish",
    "Norwegian",
    "Omani",
    "Pakistani",
    "Palauan",
    "Panamanian",
    "Papua New Guinean",
    "Paraguayan",
    "Peruvian",
    "Polish",
    "Portuguese",
    "Qatari",
    "Romanian",
    "Russian",
    "Rwandan",
    "Saint Lucian",
    "Salvadoran",
    "Samoan",
    "San Marinese",
    "Sao Tomean",
    "Saudi",
    "Scottish",
    "Senegalese",
    "Serbian",
    "Seychellois",
    "Sierra Leonean",
    "Singaporean",
    "Slovakian",
    "Slovenian",
    "Solomon Islander",
    "Somali",
    "South African",
    "South Korean",
    "Spanish",
    "Sri Lankan",
    "Sudanese",
    "Surinamer",
    "Swazi",
    "Swedish",
    "Swiss",
    "Syrian",
    "Taiwanese",
    "Tajik",
    "Tanzanian",
    "Thai",
    "Togolese",
    "Tongan",
    "Trinidadian or Tobagonian",
    "Tunisian",
    "Turkish",
    "Tuvaluan",
    "Ugandan",
    "Ukrainian",
    "Uruguayan",
    "Uzbekistani",
    "Venezuelan",
    "Vietnamese",
    "Welsh",
    "Yemenite",
    "Zambian",
    "Zimbabwean",
]

# Prompt the user for nationality and validate it
print("Please enter the nationality:")
nationality = input("> ").capitalize()  # Capitalize to standardize the input format

while nationality not in NATIONALITIES:
    print("Nationality name not found, please type again:")
    nationality = input("> ").capitalize()

# Confirm the nationality input
if nationality:
    print("Nationality name found.")
else:
    print("No nationality provided. Proceeding without nationality.")

# define empty name_list
res_list = []

for name in tqdm(name_list, desc="Processing names"):
    # adjust the prompt based on whether a nationality has been provided
    if nationality:
        prompt = [
            {
                "role": "user",
                "content": f"check this {nationality} name: {name}. Based on the name, assign a gender, using one of the two labels: [male,female]",
            }
        ]
    else:
        prompt = [
            {
                "role": "user",
                "content": f"check this name: {name}. Based on the name, assign a gender, using one of the two labels: [male,female]",
            }
        ]

    # generate a response from ChatGPT using the question chat message
    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        temperature=0.0,
    )

    # extract the answer from the response
    answer = response.choices[0].message["content"]

    res_list.append(answer)


# create a new column to append the results
df["gender"] = res_list

print("Prompt results ready")

# input name for final file
print("Input the name of the final csv file")
output_file_name = input("> ")

df.to_csv(output_file_name, index=False)
print("File successfully created")
