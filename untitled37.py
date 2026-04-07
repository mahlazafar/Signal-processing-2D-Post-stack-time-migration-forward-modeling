import imageio.v2 as imageio
import os

# پیدا کردن مسیر فعلی که این فایل پایتون در آن قرار دارد
current_dir = os.getcwd()

# تعریف نام پوشه تصاویر (اگر تصاویر مستقیم کنار کد هستند، این را به '' تغییر دهید)
image_folder_name = 'images' 
image_path = os.path.join(current_dir, image_folder_name)

# اگر پوشه images پیدا نشد، فرض می‌کنیم عکس‌ها در همان پوشه اصلی هستند
if not os.path.exists(image_path):
    image_path = current_dir

output_gif = os.path.join(image_path, 'migration_comparison.gif')
filenames = ['3.png', '4.png', '5.png']

try:
    print(f"Searching for images in: {image_path}")
    images = []
    
    for filename in filenames:
        file_full_path = os.path.join(image_path, filename)
        
        if os.path.exists(file_full_path):
            print(f"✅ Found: {filename}")
            images.append(imageio.imread(file_full_path))
        else:
            print(f"❌ Error: {filename} NOT found at {file_full_path}")

    if len(images) == len(filenames):
        print(f"🎬 Creating GIF: {output_gif}...")
        imageio.mimsave(output_gif, images, duration=1.5, loop=0)
        print("🚀 SUCCESS: GIF created successfully in the images folder!")
    else:
        print("⚠️ Could not create GIF. Please check the file names or paths.")

except Exception as e:
    print(f"An error occurred: {e}")