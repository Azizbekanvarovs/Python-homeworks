from PIL import Image
import numpy as np

# Load image
img = Image.open("images/birds.jpg")
img_np = np.array(img)

# Flip Horizontally and Vertically
flipped_h = np.flip(img_np, axis=1)  # Left-right
flipped_v = np.flip(img_np, axis=0)  # Up-down

# Add Random Noise
noise = np.random.randint(0, 50, img_np.shape, dtype='uint8')
noisy_image = np.clip(img_np + noise, 0, 255)

# Brighten Red Channel by 40
bright_image = img_np.copy()
bright_image[:, :, 0] = np.clip(bright_image[:, :, 0] + 40, 0, 255)  # Red channel

# Mask a 100x100 black rectangle in center
masked_image = img_np.copy()
h, w = masked_image.shape[:2]
center_x, center_y = w // 2, h // 2
masked_image[center_y-50:center_y+50, center_x-50:center_x+50] = [0, 0, 0]

# Save results
Image.fromarray(flipped_h).save("images/birds_flipped_horizontal.jpg")
Image.fromarray(flipped_v).save("images/birds_flipped_vertical.jpg")
Image.fromarray(noisy_image).save("images/birds_noisy.jpg")
Image.fromarray(bright_image).save("images/birds_bright_red.jpg")
Image.fromarray(masked_image).save("images/birds_masked.jpg")