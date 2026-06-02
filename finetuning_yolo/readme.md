# YOLO Fine-tuning (Industrial Use Case)
 
## Objective
Improve detection accuracy for industrial equipment and faults.
 
## Dataset
- ~100 images
- Classes: motor, leakage, wiring_issue
 
## Approach
- Used YOLOv8 pretrained model
- Fine-tuned for 20 epochs
- Evaluated using validation set
 
## Results
- mAP50: ~0.72 (example)
- Good performance on leakage detection
- Limited performance on wiring
 
## Conclusion
Fine-tuning improves domain-specific detection and can be integrated into production pipeline.