from PIL import Image

def remove_white_bg(input_path, output_path, tolerance=20):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # Check if pixel is white or near-white
        if item[0] >= 255 - tolerance and item[1] >= 255 - tolerance and item[2] >= 255 - tolerance:
            # Change to transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Saved transparent image to {output_path}")

remove_white_bg('/Users/shayenefreita/.gemini/antigravity-ide/brain/d810dbc7-9ccd-46b3-a074-c05fed1973e7/student_solid_bg_1780345537574.png', 'assets/images/vestibular-student-perfect.png')
