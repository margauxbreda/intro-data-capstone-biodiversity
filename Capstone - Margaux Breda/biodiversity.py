{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone 2: Biodiversity Project"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "You are a biodiversity analyst working for the National Parks Service.  You're going to help them analyze some data about species at various national parks.\n",
    "\n",
    "Note: The data that you'll be working with for this project is *inspired* by real data, but is mostly fictional."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 1\n",
    "Import the modules that you'll be using in this assignment:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 2\n",
    "You have been given two CSV files. `species_info.csv` with data about different species in our National Parks, including:\n",
    "- The scientific name of each species\n",
    "- The common names of each species\n",
    "- The species conservation status\n",
    "\n",
    "Load the dataset and inspect it:\n",
    "- Load `species_info.csv` into a DataFrame called `species`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "species=pd.read_csv('species_info.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Inspect each DataFrame using `.head()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  category                scientific_name  \\\n",
      "0   Mammal  Clethrionomys gapperi gapperi   \n",
      "1   Mammal                      Bos bison   \n",
      "2   Mammal                     Bos taurus   \n",
      "3   Mammal                     Ovis aries   \n",
      "4   Mammal                 Cervus elaphus   \n",
      "\n",
      "                                        common_names conservation_status  \n",
      "0                           Gapper's Red-Backed Vole                 NaN  \n",
      "1                              American Bison, Bison                 NaN  \n",
      "2  Aurochs, Aurochs, Domestic Cattle (Feral), Dom...                 NaN  \n",
      "3  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)                 NaN  \n",
      "4                                      Wapiti Or Elk                 NaN  \n"
     ]
    }
   ],
   "source": [
    "print(species.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 3\n",
    "Let's start by learning a bit more about our data.  Answer each of the following questions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many different species are in the `species` DataFrame?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5541\n"
     ]
    }
   ],
   "source": [
    "species_count= species[\"scientific_name\"].nunique()\n",
    "print(species_count)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the different values of `category` in `species`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Mammal' 'Bird' 'Reptile' 'Amphibian' 'Fish' 'Vascular Plant'\n",
      " 'Nonvascular Plant']\n"
     ]
    }
   ],
   "source": [
    "species_type = species[\"category\"].unique()\n",
    "print(species_type)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the different values of `conservation_status`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "conservation_statuses = species.conservation_status.nunique()\n",
    "print(conservation_statuses)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 4\n",
    "Let's start doing some analysis!\n",
    "\n",
    "The column `conservation_status` has several possible values:\n",
    "- `Species of Concern`: declining or appear to be in need of conservation\n",
    "- `Threatened`: vulnerable to endangerment in the near future\n",
    "- `Endangered`: seriously at risk of extinction\n",
    "- `In Recovery`: formerly `Endangered`, but currnetly neither in danger of extinction throughout all or a significant portion of its range\n",
    "\n",
    "We'd like to count up how many species meet each of these criteria.  Use `groupby` to count how many `scientific_name` meet each of these criteria."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  conservation_status  scientific_name\n",
      "0          Endangered               15\n",
      "1         In Recovery                4\n",
      "2  Species of Concern              151\n",
      "3          Threatened               10\n"
     ]
    }
   ],
   "source": [
    "conservation_counts=species.groupby(\"conservation_status\").scientific_name.nunique().reset_index()\n",
    "print conservation_counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we saw before, there are far more than 200 species in the `species` table.  Clearly, only a small number of them are categorized as needing some sort of protection.  The rest have `conservation_status` equal to `None`.  Because `groupby` does not include `None`, we will need to fill in the null values.  We can do this using `.fillna`.  We pass in however we want to fill in our `None` values as an argument.\n",
    "\n",
    "Paste the following code and run it to see replace `None` with `No Intervention`:\n",
    "```python\n",
    "species.fillna('No Intervention', inplace=True)\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "species.fillna('No Intervention', inplace = True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Now run the same `groupby` as before to see how many species require `No Protection`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "protection_counts = species.groupby('conservation_status')\\\n",
    "    .scientific_name.nunique().reset_index()\\\n",
    "    .sort_values(by='scientific_name')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's use `plt.bar` to create a bar chart.  First, let's sort the columns by how many species are in each categories.  We can do this using `.sort_values`.  We use the the keyword `by` to indicate which column we want to sort by.\n",
    "\n",
    "Paste the following code and run it to create a new DataFrame called `protection_counts`, which is sorted by `scientific_name`:\n",
    "```python\n",
    "protection_counts = species.groupby('conservation_status')\\\n",
    "    .scientific_name.count().reset_index()\\\n",
    "    .sort_values(by='scientific_name')\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "protection_counts = species.groupby('conservation_status')\\\n",
    "    .scientific_name.count().reset_index()\\\n",
    "    .sort_values(by='scientific_name')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's create a bar chart!\n",
    "1. Start by creating a wide figure with `figsize=(10, 4)`\n",
    "1. Start by creating an axes object called `ax` using `plt.subplot`.\n",
    "2. Create a bar chart whose heights are equal to `scientific_name` column of `protection_counts`.\n",
    "3. Create an x-tick for each of the bars.\n",
    "4. Label each x-tick with the label from `conservation_status` in `protection_counts`\n",
    "5. Label the y-axis `Number of Species`\n",
    "6. Title the graph `Conservation Status by Species`\n",
    "7. Plot the grap using `plt.show()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (10,4))\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(protection_counts)),protection_counts.scientific_name.values)\n",
    "ax.set_xticks(range(len(protection_counts)))\n",
    "ax.set_xticklabels(protection_counts.conservation_status.values)\n",
    "plt.ylabel('Number of Species')\n",
    "plt.title('Conservation Status by Species')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 4\n",
    "Are certain types of species more likely to be endangered?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a new column in `species` called `is_protected`, which is `True` if `conservation_status` is not equal to `No Intervention`, and `False` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "species['is_protected'] = species.conservation_status != 'No Intervention'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's group by *both* `category` and `is_protected`.  Save your results to `category_counts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_counts = species.groupby(['category', 'is_protected'])\\\n",
    "                         .scientific_name.nunique().reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_count` using `head()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    category  is_protected  scientific_name\n",
      "0  Amphibian         False               72\n",
      "1  Amphibian          True                7\n",
      "2       Bird         False              413\n",
      "3       Bird          True               75\n",
      "4       Fish         False              115\n"
     ]
    }
   ],
   "source": [
    "print category_counts.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "It's going to be easier to view this data if we pivot it.  Using `pivot`, rearange `category_counts` so that:\n",
    "- `columns` is `conservation_status`\n",
    "- `index` is `category`\n",
    "- `values` is `scientific_name`\n",
    "\n",
    "Save your pivoted data to `category_pivot`. Remember to `reset_index()` at the end."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_pivot = category_counts.pivot(columns='is_protected',\n",
    "                                      index='category',\n",
    "                                      values='scientific_name')\\\n",
    "                                .reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_protected           category  False  True\n",
      "0                     Amphibian     72     7\n",
      "1                          Bird    413    75\n",
      "2                          Fish    115    11\n",
      "3                        Mammal    146    30\n",
      "4             Nonvascular Plant    328     5\n",
      "5                       Reptile     73     5\n",
      "6                Vascular Plant   4216    46\n"
     ]
    }
   ],
   "source": [
    "print(category_pivot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `.columns` property to  rename the categories `True` and `False` to something more description:\n",
    "- Leave `category` as `category`\n",
    "- Rename `False` to `not_protected`\n",
    "- Rename `True` to `protected`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_pivot.columns = ['category', 'not_protected', 'protected']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a new column of `category_pivot` called `percent_protected`, which is equal to `protected` (the number of species that are protected) divided by `protected` plus `not_protected` (the total number of species)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            category  not_protected  protected  percent_protected\n",
      "0          Amphibian             72          7           0.088608\n",
      "1               Bird            413         75           0.153689\n",
      "2               Fish            115         11           0.087302\n",
      "3             Mammal            146         30           0.170455\n",
      "4  Nonvascular Plant            328          5           0.015015\n",
      "5            Reptile             73          5           0.064103\n",
      "6     Vascular Plant           4216         46           0.010793\n"
     ]
    }
   ],
   "source": [
    "print category_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like species in category `Mammal` are more likely to be endangered than species in `Bird`.  We're going to do a significance test to see if this statement is true.  Before you do the significance test, consider the following questions:\n",
    "- Is the data numerical or categorical?\n",
    "- How many pieces of data are you comparing?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Based on those answers, you should choose to do a *chi squared test*.  In order to run a chi squared test, we'll need to create a contingency table.  Our contingency table should look like this:\n",
    "\n",
    "||protected|not protected|\n",
    "|-|-|-|\n",
    "|Mammal|?|?|\n",
    "|Bird|?|?|\n",
    "\n",
    "Create a table called `contingency` and fill it in with the correct numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "contingency= [[30, 146], [75, 413]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In order to perform our chi square test, we'll need to import the correct function from scipy.  Past the following code and run it:\n",
    "```py\n",
    "from scipy.stats import chi2_contingency\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.stats import chi2_contingency"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now run `chi2_contingency` with `contingency`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.6875948096661336\n"
     ]
    }
   ],
   "source": [
    "pval = chi2_contingency(contingency)[1]\n",
    "print(pval)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like this difference isn't significant!\n",
    "\n",
    "Let's test another.  Is the difference between `Reptile` and `Mammal` significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.03835559022969898\n"
     ]
    }
   ],
   "source": [
    "contingency_reptile_mammal = [[30, 146],\n",
    "                              [5, 73]]\n",
    "\n",
    "pval_reptile_mammal = chi2_contingency(contingency_reptile_mammal)[1]\n",
    "print(pval_reptile_mammal)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Yes! It looks like there is a significant difference between `Reptile` and `Mammal`!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Conservationists have been recording sightings of different species at several national parks for the past 7 days.  They've saved sent you their observations in a file called `observations.csv`.  Load `observations.csv` into a variable called `observations`, then use `head` to view the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            scientific_name                            park_name  observations\n",
      "0        Vicia benghalensis  Great Smoky Mountains National Park            68\n",
      "1            Neovison vison  Great Smoky Mountains National Park            77\n",
      "2         Prunus subcordata               Yosemite National Park           138\n",
      "3      Abutilon theophrasti                  Bryce National Park            84\n",
      "4  Githopsis specularioides  Great Smoky Mountains National Park            85\n"
     ]
    }
   ],
   "source": [
    "observations = pd.read_csv(\"observations.csv\")\n",
    "print(observations.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Some scientists are studying the number of sheep sightings at different national parks.  There are several different scientific names for different types of sheep.  We'd like to know which rows of `species` are referring to sheep.  Notice that the following code will tell us whether or not a word occurs in a string:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Does \"Sheep\" occur in this string?\n",
    "str1 = 'This string contains Sheep'\n",
    "'Sheep' in str1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Does \"Sheep\" occur in this string?\n",
    "str2 = 'This string contains Cows'\n",
    "'Sheep' in str2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use `apply` and a `lambda` function to create a new column in `species` called `is_sheep` which is `True` if the `common_names` contains `'Sheep'`, and `False` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Select the rows of `species` where `is_sheep` is `True` and examine the results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            category              scientific_name  \\\n",
      "3             Mammal                   Ovis aries   \n",
      "1139  Vascular Plant             Rumex acetosella   \n",
      "2233  Vascular Plant           Festuca filiformis   \n",
      "3014          Mammal              Ovis canadensis   \n",
      "3758  Vascular Plant             Rumex acetosella   \n",
      "3761  Vascular Plant            Rumex paucifolius   \n",
      "4091  Vascular Plant                 Carex illota   \n",
      "4383  Vascular Plant  Potentilla ovina var. ovina   \n",
      "4446          Mammal      Ovis canadensis sierrae   \n",
      "\n",
      "                                           common_names conservation_status  \\\n",
      "3     Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
      "1139                        Sheep Sorrel, Sheep Sorrell     No Intervention   \n",
      "2233                              Fineleaf Sheep Fescue     No Intervention   \n",
      "3014                       Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
      "3758  Common Sheep Sorrel, Field Sorrel, Red Sorrel,...     No Intervention   \n",
      "3761   Alpine Sheep Sorrel, Fewleaved Dock, Meadow Dock     No Intervention   \n",
      "4091                       Sheep Sedge, Smallhead Sedge     No Intervention   \n",
      "4383                                   Sheep Cinquefoil     No Intervention   \n",
      "4446                        Sierra Nevada Bighorn Sheep          Endangered   \n",
      "\n",
      "      is_protected  is_sheep  \n",
      "3             True      True  \n",
      "1139          True      True  \n",
      "2233          True      True  \n",
      "3014          True      True  \n",
      "3758          True      True  \n",
      "3761          True      True  \n",
      "4091          True      True  \n",
      "4383          True      True  \n",
      "4446          True      True  \n"
     ]
    }
   ],
   "source": [
    "species_is_sheep = species[species.is_sheep]\n",
    "print species_is_sheep"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Many of the results are actually plants.  Select the rows of `species` where `is_sheep` is `True` and `category` is `Mammal`.  Save the results to the variable `sheep_species`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     category          scientific_name  \\\n",
      "3      Mammal               Ovis aries   \n",
      "3014   Mammal          Ovis canadensis   \n",
      "4446   Mammal  Ovis canadensis sierrae   \n",
      "\n",
      "                                           common_names conservation_status  \\\n",
      "3     Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
      "3014                       Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
      "4446                        Sierra Nevada Bighorn Sheep          Endangered   \n",
      "\n",
      "      is_protected  is_sheep  \n",
      "3            False      True  \n",
      "3014          True      True  \n",
      "4446          True      True  \n"
     ]
    }
   ],
   "source": [
    "sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]\n",
    "\n",
    "print sheep_species"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now merge `sheep_species` with `observations` to get a DataFrame with observations of sheep.  Save this DataFrame as `sheep_observations`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            scientific_name                            park_name  \\\n",
      "0           Ovis canadensis            Yellowstone National Park   \n",
      "1           Ovis canadensis                  Bryce National Park   \n",
      "2           Ovis canadensis               Yosemite National Park   \n",
      "3           Ovis canadensis  Great Smoky Mountains National Park   \n",
      "4   Ovis canadensis sierrae            Yellowstone National Park   \n",
      "5   Ovis canadensis sierrae               Yosemite National Park   \n",
      "6   Ovis canadensis sierrae                  Bryce National Park   \n",
      "7   Ovis canadensis sierrae  Great Smoky Mountains National Park   \n",
      "8                Ovis aries               Yosemite National Park   \n",
      "9                Ovis aries  Great Smoky Mountains National Park   \n",
      "10               Ovis aries                  Bryce National Park   \n",
      "11               Ovis aries            Yellowstone National Park   \n",
      "\n",
      "    observations category                                       common_names  \\\n",
      "0            219   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
      "1            109   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
      "2            117   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
      "3             48   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
      "4             67   Mammal                        Sierra Nevada Bighorn Sheep   \n",
      "5             39   Mammal                        Sierra Nevada Bighorn Sheep   \n",
      "6             22   Mammal                        Sierra Nevada Bighorn Sheep   \n",
      "7             25   Mammal                        Sierra Nevada Bighorn Sheep   \n",
      "8            126   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
      "9             76   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
      "10           119   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
      "11           221   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
      "\n",
      "   conservation_status  is_protected  is_sheep  \n",
      "0   Species of Concern          True      True  \n",
      "1   Species of Concern          True      True  \n",
      "2   Species of Concern          True      True  \n",
      "3   Species of Concern          True      True  \n",
      "4           Endangered          True      True  \n",
      "5           Endangered          True      True  \n",
      "6           Endangered          True      True  \n",
      "7           Endangered          True      True  \n",
      "8      No Intervention         False      True  \n",
      "9      No Intervention         False      True  \n",
      "10     No Intervention         False      True  \n",
      "11     No Intervention         False      True  \n"
     ]
    }
   ],
   "source": [
    "sheep_observations = observations.merge(sheep_species)\n",
    "print sheep_observations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many total sheep observations (across all three species) were made at each national park?  Use `groupby` to get the `sum` of `observations` for each `park_name`.  Save your answer to `obs_by_park`.\n",
    "\n",
    "This is the total number of sheep observed in each park over the past 7 days."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                             park_name  observations\n",
      "0                  Bryce National Park           250\n",
      "1  Great Smoky Mountains National Park           149\n",
      "2            Yellowstone National Park           507\n",
      "3               Yosemite National Park           282\n"
     ]
    }
   ],
   "source": [
    "obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()\n",
    "\n",
    "print obs_by_park"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a bar chart showing the different number of observations per week at each park.\n",
    "\n",
    "1. Start by creating a wide figure with `figsize=(16, 4)`\n",
    "1. Start by creating an axes object called `ax` using `plt.subplot`.\n",
    "2. Create a bar chart whose heights are equal to `observations` column of `obs_by_park`.\n",
    "3. Create an x-tick for each of the bars.\n",
    "4. Label each x-tick with the label from `park_name` in `obs_by_park`\n",
    "5. Label the y-axis `Number of Observations`\n",
    "6. Title the graph `Observations of Sheep per Week`\n",
    "7. Plot the grap using `plt.show()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16, 4))\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(obs_by_park)),obs_by_park.observations.values)\n",
    "ax.set_xticks(range(len(obs_by_park)))\n",
    "ax.set_xticklabels(obs_by_park.park_name.values)\n",
    "plt.ylabel('Number of Observations')\n",
    "plt.title('Observations of Sheep per Week')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Our scientists know that 15% of sheep at Bryce National Park have foot and mouth disease.  Park rangers at Yellowstone National Park have been running a program to reduce the rate of foot and mouth disease at that park.  The scientists want to test whether or not this program is working.  They want to be able to detect reductions of at least 5 percentage point.  For instance, if 10% of sheep in Yellowstone have foot and mouth disease, they'd like to be able to know this, with confidence.\n",
    "\n",
    "Use the sample size calculator at <a href=\"https://www.optimizely.com/sample-size-calculator/\">Optimizely</a> to calculate the number of sheep that they would need to observe from each park.  Use the default level of significance (90%).\n",
    "\n",
    "Remember that \"Minimum Detectable Effect\" is a percent of the baseline."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "baseline = 15\n",
    "\n",
    "minimum_detectable_effect = 100*5./15\n",
    "\n",
    "sample_size_per_variant = 870"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many weeks would you need to observe sheep at Bryce National Park in order to observe enough sheep?  How many weeks would you need to observe at Yellowstone National Park to observe enough sheep?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "yellowstone_weeks_observing = sample_size_per_variant/507.\n",
    "\n",
    "bryce_weeks_observing = sample_size_per_variant/250."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
