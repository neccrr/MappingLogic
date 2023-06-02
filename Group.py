import json
import time


def groupMapping():
    # Class mappings
    classMapping = "mappings/processed/class_mappings.json"

    # Opens and read the mapping json file
    with open(classMapping, 'r') as file:
        parsedClassMappingData = json.load(file)

    # Initialize the grouped mapping data list
    groupedMappingData = []

    for classItem in parsedClassMappingData:
        # Class Mappings
        obfuscatedClassName = classItem["obfuscatedClassName"]
        mappedClassName = classItem["mappedClassName"]

        # Field mappings
        fieldMapping = "mappings/processed/field_mappings.json"

        # Opens and reads the mapping json file
        with open(fieldMapping, 'r') as file:
            parsedFieldMappingData = json.load(file)

        # Initialize the fields list for the current class
        fields = []

        for fieldItem in parsedFieldMappingData:
            if fieldItem["obfuscatedOwnerName"] == obfuscatedClassName:
                # Field Mappings
                obfuscatedFieldName = fieldItem["obfuscatedFieldName"]
                obfuscatedFieldOwnerName = fieldItem["obfuscatedOwnerName"]
                obfuscatedFieldFullPathName = fieldItem["obfuscatedFullPathName"]
                obfuscatedFieldObjectType = fieldItem["obfuscatedObjectType"]

                mappedFieldName = fieldItem["mappedFieldName"]
                mappedFieldOwnerName = fieldItem["mappedOwnerName"]
                mappedFieldFullPathName = fieldItem["mappedFullPathName"]
                mappedFieldObjectType = fieldItem["mappedObjectType"]

                # Add the field to the fields list
                fields.append({
                    "obfuscatedFieldName": obfuscatedFieldName,
                    "obfuscatedFieldOwnerName": obfuscatedFieldOwnerName,
                    "obfuscatedFieldFullPathName": obfuscatedFieldFullPathName,
                    "obfuscatedFieldObjectType": obfuscatedFieldObjectType,

                    "mappedFieldName": mappedFieldName,
                    "mappedFieldOwnerName": mappedFieldOwnerName,
                    "mappedFieldFullPathName": mappedFieldFullPathName,
                    "mappedFieldObjectType": mappedFieldObjectType
                })

                print(f"Adding {mappedFieldName} to {mappedFieldOwnerName}")

        # Method mappings
        methodMapping = "mappings/processed/method_mappings.json"

        # Opens and reads the mapping json file
        with open(methodMapping, 'r') as file:
            parsedMethodMappingData = json.load(file)

        # Initialize the methods list for the current class
        methods = []

        for methodItem in parsedMethodMappingData:
            if methodItem["obfuscatedOwnerName"] == obfuscatedClassName:
                # Method Mappings
                obfuscatedMethodName = methodItem["obfuscatedMethodName"]
                obfuscatedMethodOwnerName = methodItem["obfuscatedOwnerName"]
                obfuscatedMethodFullPathName = methodItem["obfuscatedFullPathName"]
                obfuscatedMethodObjectType = methodItem["obfuscatedObjectType"]

                mappedMethodName = methodItem["mappedMethodName"]
                mappedMethodOwnerName = methodItem["mappedOwnerName"]
                mappedMethodFullPathName = methodItem["mappedFullPathName"]
                mappedMethodObjectType = methodItem["mappedObjectType"]

                # Add the method to the methods list
                methods.append({
                    "obfuscatedMethodName": obfuscatedMethodName,
                    "obfuscatedMethodOwnerName": obfuscatedMethodOwnerName,
                    "obfuscatedMethodFullPathName": obfuscatedMethodFullPathName,
                    "obfuscatedMethodObjectType": obfuscatedMethodObjectType,

                    "mappedMethodName": mappedMethodName,
                    "mappedMethodOwnerName": mappedMethodOwnerName,
                    "mappedMethodFullPathName": mappedMethodFullPathName,
                    "mappedMethodObjectType": mappedMethodObjectType
                })

                print(f"Adding {mappedMethodName} to {mappedMethodOwnerName}")

        # Create the class entry with fields and methods
        class_entry = {
            "obfuscatedClassName": obfuscatedClassName,
            "mappedClassName": mappedClassName,
            "fields": fields,
            "methods": methods
        }

        # Add the class entry to the grouped mapping data
        groupedMappingData.append(class_entry)

        print(f"Successfully Grouped {mappedClassName} ({obfuscatedClassName})")

    # Write the merged content to a new JSON file
    with open('mappings/processed/grouped_mappings.json', 'w') as groupedFile:
        json.dump(groupedMappingData, groupedFile, indent=4)


if __name__ == '__main__':
    # Capture the start time
    startTime = time.perf_counter()

    # Starting mapping process
    print("Starting mapping grouping process...")

    groupMapping()

    print("Grouping of JSON mapping completed.")

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
