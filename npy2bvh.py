from pathlib import Path
import numpy as np
from bvh_skeleton import cmu_skeleton

current_dir = Path.cwd()

#parser로 추후 수정
bvh_file = current_dir / "output" / "output.bvh"
npy_file = current_dir / "input" / "X3D.npy"

data = np.load(str(npy_file))

cmu_skel = cmu_skeleton.CMUSkeleton()
_, _ = cmu_skel.poses2bvh(data, output_file = str(bvh_file))
