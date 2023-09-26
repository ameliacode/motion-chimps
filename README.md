## mocap pipeline
WAK ent. motion data preprocessing pipeline  
🤺 objective: extracting mocap via monocular video

---

### Plan

- [ ] [SOTA - 3d pose estimation](https://github.com/davrempe/contact-human-dynamics): contact+physics-based
- [ ] [SOTA - MotionBERT](https://github.com/Walter0807/MotionBERT)
- [ ] Denoise
- [ ] NPY to BVH [video2bvh](https://github.com/KevinLTT/video2bvh)
- [ ] [fairmotion](https://github.com/facebookresearch/fairmotion)

### MotionBert

> "일단 비젼 관련이라 그런지 트랜스포머 모델 치고는 굉장히 사이즈가 작아서 고성능 그래픽카드가 아니어도 돌려볼만 하다는 점은 고무적"  

> "파인튜닝용 데이터셋을 만드는 게 관건"

- [Benchmark](https://paperswithcode.com/sota/3d-human-pose-estimation-on-human36m)

1. Alphapose 내 colab example+MotionBert 가이드라인 참고해서 alphapose-result.json 생성하기 (GPU가 아닌 CPU로 돌아가는 문제..)
2. MotionBert infer_wild.py 실행

※ python=3.7 pytorch=1.13 cuda=11.7  
※ ffmpeg 설치해서 파일을 mp4로 변환할 것을 추천함 → 추후 colab에 통합..?