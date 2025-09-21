import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# --- إنشاء الشخصية ---

head = trimesh.creation.icosphere(subdivisions=4, radius=20)

eye1 = trimesh.creation.icosphere(subdivisions=3, radius=3)
eye1.apply_translation([7, 10, 5])

eye2 = trimesh.creation.icosphere(subdivisions=3, radius=3)
eye2.apply_translation([-7, 10, 5])

pupil1 = trimesh.creation.icosphere(subdivisions=2, radius=1.2)
pupil1.apply_translation([7, 10, 7])

pupil2 = trimesh.creation.icosphere(subdivisions=2, radius=1.2)
pupil2.apply_translation([-7, 10, 7])

nose = trimesh.creation.cylinder(radius=2, height=6, sections=16)
nose.apply_translation([0, 15, 0])

mouth = trimesh.creation.capsule(radius=6, height=1)
mouth.apply_translation([0, -5, 12])

character = trimesh.util.concatenate([
    head, eye1, eye2, pupil1, pupil2, nose, mouth
])

# --- دالة للرسم من زاوية معينة ---
def render_view(elev, azim, filename):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection="3d")

    ax.add_collection3d(Poly3DCollection(character.triangles, alpha=0.6))

    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    ax.set_zlim(-30, 30)

    ax.view_init(elev=elev, azim=azim)
    plt.savefig(filename)
    plt.close()
    print(f"✅ تم حفظ الصورة: {filename}")

# --- حفظ صور من زوايا مختلفة ---
render_view(10, 0, "homer_front.png")   # أمام
render_view(10, 90, "homer_side.png")   # جانب
render_view(90, 0, "homer_top.png")     # فوق
