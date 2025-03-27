import os
import shutil

def move_pdfs_to_subs(base_path):
    # Create 'subs' directory if it doesn't exist
    subs_folder = os.path.join(base_path, "subs")
    os.makedirs(subs_folder, exist_ok=True)

    # Iterate over all items in the base directory
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        
        # Process only directories (skip 'subs' to avoid recursion)
        if os.path.isdir(item_path) and item != "subs":
            # Look for PDF files inside the directory
            pdf_files = [f for f in os.listdir(item_path) if f.lower().endswith('.pdf')]

            for pdf_file in pdf_files:
                old_pdf_path = os.path.join(item_path, pdf_file)
                new_pdf_path = os.path.join(subs_folder, pdf_file)

                # Ensure unique filenames to prevent overwriting
                base_name, extension = os.path.splitext(pdf_file)
                counter = 1
                while os.path.exists(new_pdf_path):
                    new_pdf_path = os.path.join(subs_folder, f"{base_name}_{counter}{extension}")
                    counter += 1

                # Move the PDF file
                try:
                    shutil.move(old_pdf_path, new_pdf_path)
                    print(f"Moved: {old_pdf_path} -> {new_pdf_path}")
                except Exception as e:
                    print(f"Failed to move {old_pdf_path}: {e}")

if __name__ == "__main__":
    base_directory = os.path.dirname(os.path.abspath(__file__))  # Current script directory
    move_pdfs_to_subs(base_directory)
