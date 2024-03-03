# MOTION CHIMPS
WAK ent. motion data preprocessing pipeline  
🎯 objective: extracting mocap via monocular video

---

## 📝 Plan

- [ ] [SOTA - 3d pose estimation](https://github.com/davrempe/contact-human-dynamics): contact+physics-based
- [ ] [SOTA - MotionBERT](https://github.com/Walter0807/MotionBERT)
- [ ] Denoise
- [ ] NPY to BVH [video2bvh](https://github.com/KevinLTT/video2bvh)
- [ ] [fairmotion](https://github.com/facebookresearch/fairmotion)

#### Assignment 🎯 기존 모델(MotionBert)를 개선시키는 것이 관건
- End Effector문제를 estimated 된 결과에서 어떻게 해결?
  - Physics-based(Contact and Human Dynamics from Monocular Video, HuMor)
- Denoise: Estimation time을 고려한다면, Inverse Kinematics로 단순히 해결하거나, Motion DVAE와 같이 autoencoder로 해결
- Motion editing: Motion/Time warping

## 🔑 Preliminary Keyword
- Pose estimation
- Motion data extension: Bio Vision Hierarchy
- Kinematics(Forward kinematics, Inverse Kinematics)
- Transformer, Autoencoder

## 🛳️ Onboarding

### Team AI
- Local: Ubuntu(20.04 and up): 윈도우에서 하고자 한다면 가상환경 사용 권장 [참고](https://ingu627.github.io/tips/install_ubuntu/) ⚠️ 용량 50GB 차지, vscode 18.04 지원 종료 issue
- Colab
- Python ➡️ installation requirement의 경우 [MotionBert](https://github.com/Walter0807/MotionBERT) 참고할 것


### Team Frontend
- Python
- Kivy(GUI)
- PyopenGL
  
## 💁‍♀️ How to MotionBert

MotionBERT는 단안카메라를 입력으로 두기 때문에 multi view와 다르게 epipolar geometry를 사용하지 X  
따라서 2D pose estimation(via Alphapose) 후에 3D pose estimation(MotionBert)를 하게 됨  
문제는 Alphapose의 경우 estimation 시간이 상당히 긺 ➡️ SOTA 2d pose estimation으로 대체해야함

> "일단 비젼 관련이라 그런지 트랜스포머 모델 치고는 굉장히 사이즈가 작아서 고성능 그래픽카드가 아니어도 돌려볼만 하다는 점은 고무적"  

> "파인튜닝용 데이터셋을 만드는 게 관건"

- [Benchmark](https://paperswithcode.com/sota/3d-human-pose-estimation-on-human36m)

1. Alphapose 내 colab example+MotionBert 가이드라인 참고해서 alphapose-result.json 생성하기 (GPU가 아닌 CPU로 돌아가는 문제..)
2. MotionBert infer_wild.py 실행

※ python=3.7 pytorch=1.13 cuda=11.7  
※ ffmpeg 설치해서 파일을 mp4로 변환할 것을 추천함 → 추후 colab에 통합..?

