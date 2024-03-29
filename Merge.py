import json
import time

from SystemUtils import SystemUtils


def mergeJsonMapping():
    # Define the order of JSON files to merge
    mappingOrders = ["mappings/processed/class_mappings.json", "mappings/processed/field_mappings.json",
                     "mappings/processed/method_mappings.json"]

    # Initialize an empty dictionary to hold the merged data
    mergedData = []

    # Iterate through file names
    for mapping in mappingOrders:
        with open(mapping, 'r') as file:
            # Load JSON content from the file
            content = json.load(file)

            # Append the content to the merged list
            mergedData.append(content)

    # Write the merged content to a new JSON file
    with open('mappings/processed/mappings.json', 'w') as merged_file:
        json.dump(mergedData, merged_file, indent=4)


# Main process
if __name__ == '__main__':
    # Capture the start time
    startTime = time.perf_counter()

    # Starting mapping process
    print("Starting mapping merging process...")

    mergeJsonMapping()

    print("Merging of JSON Mappings files completed.")

    # Capture the end time
    endTime = time.perf_counter()

    # Calculate the elapsed time
    elapsedTime = endTime - startTime

    # Format the elapsed time
    hours, a = divmod(elapsedTime, 3600)
    minutes, seconds = divmod(a, 60)
    formattedTime = ""
    if hours > 0:
        formattedTime += f"{int(hours)} hours "
    if minutes > 0:
        formattedTime += f"{int(minutes)} minutes "
    formattedTime += f"{seconds:.2f} seconds"

    print(f"Elapsed time: {elapsedTime} seconds ({elapsedTime * 1000} ms)")
    print(f"{formattedTime}")
    print("")
    SystemUtils.printSystemInformation()
