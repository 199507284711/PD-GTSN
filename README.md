# PD-GTSN

## Requirements

****The code is built with following libraries:****

 - PyTorch 1.0 or higher
 - TensorboardX
 - tqdm
 - scikit-learn
 - pandas
 - Python 3.x
 
## Training

To train the model(s) in the paper, run this command:
```javascript
python main.py <train_video_path> \
     --arch resnet50 --num_segments 8 \
     --lr 0.002 --lr_steps 40 80 --epochs 100 \
     --batch-size 32 -j 16 --dropout 0.3 --consensus_type=avg --eval-freq=1 \
     --shift --shift_div=8 --shift_place=blockres --npb
```     
The results of the training are saved as a **pth** file format.

## Testing

For example, to test the trained models from PD tremor videos, you can run：
```javascript
python test.py <test_video_path> \
    --weights= <pth_path>\
    --test_segments=8 --batch_size=32
```    
## Contact for Questions

W. Liu, QBX20210094@yjs.fjnu.edu.cn
    
