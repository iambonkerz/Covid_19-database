Continue = True
records = {}
while Continue:
    patient_name = input("Enter patient name: ")
    if " " not in patient_name:
        patient_name = input("Please include patient's surname: ")
    if patient_name not in records.keys():
        records[patient_name] = None
        patient_result = input("Enter test result: ")
        records[patient_name] = patient_result
        base = input("Would you like to make any other changes? (Y/N): ")
        if base == 'Y':
            Continue = True
        elif base == 'N':
            Continue = False
        else:
            base = input("Please enter Y for yes, N for no:  ")
            if base == 'Y':
                Continue = True
            elif base == 'N':
                Continue = False
    elif patient_name in records.keys():
        records[patient_name] = input("Enter updated result: ")
        base = input("Would you like to make any other changes? (Y/N): ")
        if base == 'Y':
            Continue = True
        elif base == 'N':
            Continue = False
        else:
            base = input("Please enter Y for yes, N for no:  ")
            if base == 'Y':
                Continue = True
            elif base == 'N':
                Continue = False
for key, value in records.items():
    print(key, ': ', value)
