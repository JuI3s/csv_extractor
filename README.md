# csv_extractor
Class to download csv files from a site and get specific fields

The retriever finds all of the links contained in the page that contains a csv file (extension ends with '.csv') and downloads them. Then the user can get specific field records given the input row and field names from the csv reader (return None if a field is missing).
