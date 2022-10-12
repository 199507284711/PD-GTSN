# PD-GTSN

This project is for the MDS-UPDRS scores prediction of PD tremors based on video.

## Requirements

****The code is built with following libraries:****

 - PyTorch 1.0 or higher
 - TensorboardX
 - tqdm
 - scikit-learn
 - pandas
 - Python 3.x
 
## Access to Datasets

You must contact us first. Follow the [link](https://zenodo.org/record/7188051) to apply for our dataset!
Please ensure that you satisfy the following application requirements：
- Your institution must be non-profit, non-commercial;
- You must provide proof of relevant medical credentials to show that you are engaged in the same research area;
- We take the patients' privacy very seriously, even if they have signed a consent form with us. Therefore,you must contact us (email:QBX20210094@yjs.fjnu.edu.cn) first so that we can confirm and review your information in detail. You will then be required to sign a contract to ensure that you will not make the dataset public and use it for any commercial or for-profit purposes;
 
## Training

To train the model(s) in the paper, run this command:
```javascript
python main.py <train_video_path> \
     --arch resnet50 --num_segments 8 \
     --lr 0.002 --lr_steps 40 80 --epochs 100 \
     --batch-size 32 -j 16 --dropout 0.3 --consensus_type=avg --eval-freq=1 \
     --shift --shift_div=8 --shift_place=blockres --npb
```     
The results of the training are saved as a **.pth** file format.

## Testing

For example, to test the trained models from PD tremor videos, you can run：
```javascript
python test.py <test_video_path> \
    --weights= <pth_path>\
    --test_segments=8 --batch_size=32
```    
## Contact for Questions

W. Liu, QBX20210094@yjs.fjnu.edu.cn
    
