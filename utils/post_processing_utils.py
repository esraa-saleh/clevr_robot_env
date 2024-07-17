import json

def compute_confusion_matrix(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    confusion_matrices = []

    for item in data["inputs_and_preds"]:
        answers = item["pred_answers"]
        gt = item["gt_answers"]
        assert (len(answers) == len(gt) == len(item["questions"]))
        
        true_positives = float(sum(1 for a, g in zip(answers, gt) if a == g == True)) 
        false_positives = sum(1 for a, g in zip(answers, gt) if a == True and g == False)
        total_positives = true_positives + false_positives
        
        true_negatives = sum(1 for a, g in zip(answers, gt) if a == g == False)
        false_negatives = sum(1 for a, g in zip(answers, gt) if a == False and g == True)
        total_negatives = true_negatives + false_negatives

        confusion_matrix = {
            "TP": true_positives / total_positives,
            "FP": false_positives / total_positives,
            "TN": true_negatives / total_negatives,
            "FN": false_negatives / total_negatives
        }

        confusion_matrices.append(confusion_matrix)

    return confusion_matrices
